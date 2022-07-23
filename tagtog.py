#!/usr/bin/env python3

import sys
import os
import glob
import fnmatch
from itertools import islice, chain
import argparse
from argparse import RawTextHelpFormatter
import getpass
import json
import re

try:
    import requests
except Exception:
    print("ERROR - You need to install requests: pip install requests")
    sys.exit(-1)

assert sys.version_info.major == 3, "This script requires Python 3"

# ---------------------------------------------------------------------------------------------------------------------

__author__ = "tagtog.com (tagtog Sp. z o.o.)"
__version__ = "0.3.2"
__doc__ = \
    """
    tagtog official script to Upload & Search & Download & Delete documents.

    Version: {}
    Author: {}

    Website: https://www.tagtog.com
    API documentation: https://docs.tagtog.com/API_documents_v1.html
    """.format(__version__, __author__)

# ---------------------------------------------------------------------------------------------------------------------

DEFAULT_DOMAIN = os.environ.get('TAGTOG_DOMAIN') or "https://www.tagtog.com/"
CONTENT_DISPOSITION_HEADER_FILENAME_RGX = re.compile('filename="(.+?)"')

# ---------------------------------------------------------------------------------------------------------------------


def parse_arguments(argv=[]):
    parser = argparse.ArgumentParser(prog="tagtog", description=__doc__, formatter_class=RawTextHelpFormatter)
    subparsers = parser.add_subparsers(dest="action")

    def parse_verify_ssl_argument(x):
        if os.path.exists(x):
            return x
        elif x.lower() in {'yes', 'true', 't', 'y', '1'}:
            return True
        elif x.lower() in {'no', 'false', 'f', 'n', '0'}:
            return False
        else:
            raise ValueError

    # -----------------------------------------------------------------------------------------------------------------

    def add_common_arguments(parser, default_output):
        parser.add_argument("--domain", "-d", default=DEFAULT_DOMAIN, help="tagtog domain, e.g. https://localhost:443. You can set the default with the environment variable `TAGTOG_DOMAIN`")
        parser.add_argument("--entrypoint", default="-api/documents/v1")

        parser.add_argument("--user", "-u", required=True, help="tagtog username making the request")
        parser.add_argument('--password', "-w", default=None, help="User's password -- if not given, the password is prompted")
        parser.add_argument("--owner", "-o", help="Project owner in tagtog -- defaults to the user")
        parser.add_argument("--project", "-p", required=True, help="Project name in tagtog to operate on")
        parser.add_argument("--member", "-m", required=False, help='(Optional) Project member name to operate documents on -- defaults to "master"')
        parser.add_argument("--verify_ssl", type=parse_verify_ssl_argument, default=True, help="(Optional) Choose to verify, and if so how, or not to verify the SSL/TLS certificate of the endpoint domain when making http requests. Possible values: True (default), False, or a path with trusted SSL/TLS certificate/s (either a single file or a directory).")

        parser.add_argument("--output", "-t", default=default_output, help="Output format of tagtog's response")

        return parser

    # -----------------------------------------------------------------------------------------------------------------

    upload_parser = subparsers.add_parser("upload", help='Upload files to tagtog')
    upload_parser = add_common_arguments(upload_parser, default_output="null")
    upload_parser.set_defaults(func=print_upload)

    upload_parser.add_argument("paths", nargs="+", help="paths of files or folders containing (recursively) the files to upload or otherwise the ids in the external repository (see idType) of documents to upload")

    upload_parser.add_argument("--folder", default=None, help='Folder in tagtog to upload to; refer a folder by index (e.g. 0), or by path (e.g. "pool/mySubFolder"), or by name (e.g. "mySubFolder")')
    upload_parser.add_argument("--format", "--input", default=None, help="Input format for tagtog's request. If not given, this is guessed by the tagtog server")
    upload_parser.add_argument("--batch_size", type=int, default=10, help="Number of documents to upload to tagtog at once in batches. The number must be even if you are uploading annotated documents")
    upload_parser.add_argument("--extension", "-e", default="", help="Extension of files to upload when recursively reading files from a folder, e.g. .json or .txt. Leave it as the default, i.e. the empty string, to upload all files")
    upload_parser.add_argument("--idType", "-i", choices=["PMID", "PMCID"], help="(Optional) id type of external repositories to use for document upload. See tagtog API")

    # -----------------------------------------------------------------------------------------------------------------

    search_parser = subparsers.add_parser("search", help='Search documents by query, e.g. `*` (all)')
    search_parser = add_common_arguments(search_parser, default_output="search")
    search_parser.set_defaults(func=print_search)

    search_parser.add_argument("search", nargs="+", help="search query (a same string used on the GUI)")

    # -----------------------------------------------------------------------------------------------------------------

    downld_parser = subparsers.add_parser("download", help='Download documents by search query, e.g. `updated:[NOW-1DAY to NOW]')
    downld_parser = add_common_arguments(downld_parser, default_output="ann.json")
    downld_parser.set_defaults(func=print_download)

    downld_parser.add_argument("search", nargs="+", help="search query (a same string used on the GUI)")
    downld_parser.add_argument("--output_folder", default=".", help="(Optional; defaults to '.') folder path where to store the result files to")

    # -----------------------------------------------------------------------------------------------------------------

    search_parser = subparsers.add_parser("delete", help='Delete documents that match a search query, e.g. `docid:aZ8wXRHvqyw7tjBQW8NXMTPQ0S.C-test.md` (to delete a specific doc)')
    search_parser = add_common_arguments(search_parser, default_output="null")  # Stub output
    search_parser.set_defaults(func=print_delete)

    search_parser.add_argument("search", nargs="+", help="search query (a same string used on the GUI)")

    # -----------------------------------------------------------------------------------------------------------------

    args = parser.parse_args(argv)

    if args.action is None:
        parser.print_help()
        sys.exit(-1)

    if not args.domain.endswith("/"):
        args.domain += "/"

    if args.password is None:
        args.password = getpass.getpass(prompt="tagtog password: ")

    if args.owner is None:
        args.owner = args.user

    args.req_url = args.domain + args.entrypoint
    args.req_auth = requests.auth.HTTPBasicAuth(username=args.user, password=args.password)
    args.password = None  # Hide
    args.req_params = {"owner": args.owner, "project": args.project, "output": args.output}
    if args.member:
        args.req_params["member"] = args.member

    # -----------------------------------------------------------------------------------------------------------------

    if args.action in ["upload"]:

        if args.folder:
            args.req_params["folder"] = args.folder

        if args.format:
            args.req_params["format"] = args.format

        if args.idType:
            args.func = print_ids_upload
            args.req_params["idType"] = args.idType
            args.req_params["ids"] = ",".join(args.paths)



    # -----------------------------------------------------------------------------------------------------------------

    if args.action in ["search", "download", "delete"]:
        args.search = " ".join(args.search)
        args.req_params["search"] = args.search

    # -----------------------------------------------------------------------------------------------------------------

    return args


def print_upload(args):
    filepath_iterator = gen_filepaths_generator(args.paths, args.extension)

    batch_size = args.batch_size if args.output == "null" else 1
    MAX_NUM_CONSECUTIVE_ERRORS = 3

    num_uploaded_files = 0
    num_consecutive_errors = 0

    batch_index = 0
    while True:
        batch_index += 1
        batch = islice(filepath_iterator, batch_size)
        first = next(batch, None)

        if first is None:
            print("\nFinished; num uploaded files:", num_uploaded_files)
            return
        else:
            batch = chain([first], batch)

        files = []
        filepaths = []
        for filepath in batch:
            filepaths.append(filepath)
            files.append(("files", open(filepath, "rb")))

        response = requests.put(args.req_url, params=args.req_params, auth=args.req_auth, files=files, verify=args.verify_ssl)
        print("batch", batch_index, response.status_code, response.reason)
        print("\t" + response.text)

        if response.ok:
            num_consecutive_errors = 0
            num_uploaded_files += response.json()["ok"] if args.output == "null" else batch_size

        else:
            print("\tERROR; could not upload the files:", filepaths)

            num_consecutive_errors += 1
            if num_consecutive_errors == MAX_NUM_CONSECUTIVE_ERRORS:
                print("FATAL; too many consecutive failed requireds")
                sys.exit(-1)


def print_ids_upload(args):
    response = requests.put(args.req_url, params=args.req_params, auth=args.req_auth, verify=args.verify_ssl)
    print(response)


def gen_filepaths_generator(paths, extension):
    generator = []
    for path in paths:
        generator = chain(generator, gen_filespath_generator(path, extension))
    return generator


def gen_filespath_generator(path, extension):
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        if sys.version_info.minor >= 5:  # >= Python 3.5
            return (subpath for subpath in glob.iglob(path + "/**/*" + extension, recursive=True) if os.path.isfile(subpath))
        else:
            return (os.path.join(root, filename) for root, dirnames, filenames in os.walk(path) for filename in fnmatch.filter(filenames, "*" + extension))
    else:
        print("warning, cannot read:", path)
        return []  # resilient


# -----------------------------------------------------------------------------------------------------------------


def print_search(args):
    (json_string, response) = search(args)

    if json_string:
        print(json_string)
    else:
        print("ERROR;", response.status_code, response.reason)


def search(args):
    response = requests.get(args.req_url, params=args.req_params, auth=args.req_auth, verify=args.verify_ssl)

    if response.ok:
        return (response.text, response)  # NOTE: return as json string. Dont' want to return as .json(), as otherwise in print_search we would have to do a double conversion
    else:
        return (None, response)


# -----------------------------------------------------------------------------------------------------------------


def print_delete(args):
    (txt, response) = delete(args)

    if txt:
        print(txt)
    else:
        print("ERROR;", response.status_code, response.reason)


def delete(args):
    response = requests.delete(args.req_url, params=args.req_params, auth=args.req_auth, verify=args.verify_ssl)

    if response.ok:
        return (response.text, response)
    else:
        return (None, response)


# -----------------------------------------------------------------------------------------------------------------


def print_download(args):
    next_page = 0
    download_output = args.output
    os.makedirs(args.output_folder, exist_ok=True)  # Make sure the output folder exists

    while next_page != -1:
        args.req_params["output"] = "search"
        args.req_params["page"] = next_page
        (json_string, response) = search(args)

        if json_string:
            json_dict = json.loads(json_string)

            next_page = json_dict["pages"]["next"]
            args.req_params["output"] = download_output

            for doc in json_dict["docs"]:
                args.req_params["ids"] = doc["id"]
                response = requests.get(args.req_url, params=args.req_params, auth=args.req_auth, verify=args.verify_ssl)
                del args.req_params["ids"]

                if response.ok:
                    if download_output == "orig" or download_output == "original":
                        filename = doc["id"]
                    else:
                        # Example 1: filename="aVqgBChe0bUw_mP1ti_ypKdrg2gC-PCM000600172907.json"
                        # Example 2: inline; filename="a.qMG9WVGlFtV9f5JOR64JTxQ.ei-20680818"; filename*=utf-8\'\'a.qMG9WVGlFtV9f5JOR64JTxQ.ei-20680818'
                        content_disposition = response.headers.get("Content-Disposition", "")
                        match_result = CONTENT_DISPOSITION_HEADER_FILENAME_RGX.search(content_disposition)

                        if match_result:
                            filename = match_result.group(1)
                        else:
                            filename = doc["id"] + "." + download_output

                    filepath = os.path.join(args.output_folder, filename)
                    with open(filepath, "wb") as f:
                        f.write(response.content)
                        print("downloaded:", filepath)

        else:
            print("ERROR;", response.status_code, response.reason, response.text)
            sys.exit(-1)


# -----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    args = parse_arguments(sys.argv[1:])
    args.func(args)
