---
layout: page
title: Installation
sidebar_link: true
id: on_premises_readme
toc: true
---

Copyright © tagtog Sp. z o.o.

# tagtog installation using Docker

The tagtog system runs as a mixture of **Docker** containers. This **works on Linux, macOS, and Windows**.


# HOWTO

## Requirements

Your system must have installed:

1. [Docker](https://www.docker.com)
  * **Must be version >= 18.03**. Check your version with: `docker -v`
  * To ensure that your docker installation works correctly and that you have the necessary rights to install and run docker images, run: `docker info`. Please ensure that you don't get an error like _permission denied_, and rather as expected see the details of your docker installation.

2. [Docker Compose](https://docs.docker.com/compose/)
  * Should be version >= 1.18

3. The running docker host must have the `vm.max_map_count` setting variable to be at least greater than _262144_. You can check the value by running: `sysctl vm.max_map_count`. If it is too low, set the value by running: `sudo sysctl -q -w vm.max_map_count=262144`.

4. [Bash Shell](https://www.gnu.org/software/bash/)
  * Installed in practically all systems by default.
  * Clarification: any other Unix shell should work too, including for Windows the Unix-like environment Cygwin. However, only the Bash shell is officially supported.

5. [cURL](https://en.wikipedia.org/wiki/CURL)
  * Installed in practically all systems by default




## First-time Install

* You will receive, from your person contact at tagtog, a single-line script to do a first time installation. This script will contain all the information regarding your one-server-only **license** .
* Execute it in a folder where you will run from now on all tagtog-related commands.
* A helper bash script is installed in this folder. This script assumes an UNIX environment and was tested only on **Linux and macOS**. It should work on Windows with Cygwin too. The script is not mandatory to run tagtog, but it is highly recommended.


## Run

* Choose one full-path folder/volume where all your tagtog data will be stored. For description purposes, let's call this folder `$TAGTOG_HOME` (you can indeed assign it to a global variable, such as: `export TAGTOG_HOME="$PWD/tagtog_home"`). **Important**: always write this as a full path (that is, not as a relative path such ~/tagtog or ./tagtog, but rather `/my/volume/tagtog`).

* Run the application:

```shell
./tagtog_on_premises restart latest $TAGTOG_HOME

# See more options in the tagtog_on_premises script
```

* Point your browser now to: `https://<tagtog_running_ip>:<tagtog_https_port>`.


### HTTPS & SSL

tagtog runs on _https_ only and redirects all http requests to https. We recommend setting your http and https ports to the defaults 80 and 443 but you are free to choose other ones. See the `tagtog_on_premises` script.

By default, tagtog uses a SSL self-signed certificate. To use your own SSL certificate, place the following 2 files in the folder `${TAGTOG_HOME}/ssl`:

* `tagtog_PRIVATE_KEY.key` (you can use a symlink)
* `tagtog_SSL_CERTIFICATE.pem` (you can use a symlink)


### How and where the data is stored

All tagtog data is stored in the folder: `${TAGTOG_HOME}/persistent_data/`. We recommend that you have periodic backups to avoid data losses. There are other folders in `$TAGTOG_HOME`, which nature, however, is temporary; you can nonetheless back up that too.

### Proxy

The application supports http proxies and automatically recognizes your host variables `$http_proxy` and `$https_proxy` (either written in both all lower or all upper case).




## Update

You can manually check for [new tagtog updates on this link](http://docs.tagtog.net/updates.html). Then:

```shell
./tagtog_on_premises update
./tagtog_on_premises restart latest $TAGTOG_HOME
```


## Troubleshooting

Upon any question or issue, always feel free to write a description of the problem on our [GitHub issues page](https://github.com/tagtog/tagtog-doc/issues), or shoot us directly an email: [info@tagtog.net](mailto:info@tagtog.net).

You can also check the following possible solutions.

### Problems with docker container `tagtog_taskmanager_1` or document uploading:

Try:

1. Removing all queued documents for parsing: `rm "$TAGTOG_HOME/tmp/to_process/*"`
2. Restarting the application: `./tagtog_on_premises restart latest $TAGTOG_HOME`


### Problems in an update

Try:


```shell
echo "0" > LATEST_VERSION
./tagtog_on_premises update
./tagtog_on_premises restart latest $TAGTOG_HOME
```
