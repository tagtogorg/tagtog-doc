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
  * The recommended version is >= 18.03
  * To ensure that your docker installation works correctly and that you have the necessary rights to install and run docker images, run: `docker info`. Please ensure that you don't get an error like _permission denied_, and rather as expected see the details of your docker installation.

2. [Docker Compose](https://docs.docker.com/compose/)
  * The recommended version is >= 1.18

3. **IMPORTANT**. The running docker host must have the `vm.max_map_count` setting variable to be at least greater than _262144_. You can check the value by running: `sysctl vm.max_map_count`. If it is too low, **set the value by running**: `sudo sysctl -q -w vm.max_map_count=262144`.

4. [Bash Shell](https://www.gnu.org/software/bash/)
  * Installed in practically all systems by default.
  * Clarification: any other Unix shell should work too, including for Windows the Unix-like environment Cygwin. However, only the Bash shell is officially supported.

5. [cURL](https://en.wikipedia.org/wiki/CURL)
  * Installed in practically all systems by default


### Machine Requirements

Your server (e.g. private one, or on AWS, Azure, or Linode) should meet the following minimum requirements:

* Memory:
  * On-Premises Annotator only: **8GB RAM** (e.g. `t3.large`); recommended **16GB RAM** (e.g. `t3.xlarge`)
  * On-Premises Annotator _+ ML_: **16GB RAM** (e.g. `r5.large`); recommended **32GB RAM** (e.g. `r5.xlarge`)
* Disk: **50 GB of disk space**



## First-time Install

* You will receive a single-line script. This script contains all the information regarding your one-server-only subscription **license**.
* Execute the script in some folder where you will run from now on all tagtog-related commands.
* A helper bash script is installed in this folder. This script assumes an UNIX environment and was tested only on **Linux and macOS**. It should work on Windows with Cygwin too. The script is not mandatory to run tagtog, but it is highly recommended.


## Run

* Choose one full-path folder/volume where all your tagtog data will be stored. For description purposes, let's call this folder `$TAGTOG_HOME` (you can indeed assign it to a global variable, such as: `export TAGTOG_HOME="$PWD/tagtog_home"`). **Important**: always write this as a full path (that is, not as a relative path such ~/tagtog or ./tagtog, but rather `/my/volume/tagtog`).

* Run the application:

```shell
./tagtog_on_premises restart latest $TAGTOG_HOME

# See more parameters in the tagtog_on_premises script
```

* Point your browser now to: `https://<tagtog_running_ip>:<tagtog_https_port>` (defaults to 443).


### HTTPS & SSL

tagtog runs on _https_ only and redirects all http requests to https. We recommend setting your http and https ports to the defaults 80 and 443 but you are free to choose other ones. See the `tagtog_on_premises` script.

By default, tagtog uses a SSL self-signed certificate. To use your own SSL certificate, place the following 2 files in the folder `${TAGTOG_HOME}/ssl`:

* `tagtog_PRIVATE_KEY.key` (you can use a symlink)
* `tagtog_SSL_CERTIFICATE.pem` (you can use a symlink)


### Backups: How and where the data is stored

All tagtog data is stored in the folder: `${TAGTOG_HOME}/persistent_data/`. We recommend that you have periodic backups to avoid data losses. There are other folders in `$TAGTOG_HOME`, which nature, however, is temporary; you can nonetheless back up that too.

### Proxy

The application supports http proxies and automatically recognizes your host variables `$http_proxy` and `$https_proxy` (either written in both all lower or all upper case).

**Important**: the port number must be explicitly written, regardless of whether the port is the default 80 for http or 443 for https. That is, always write something like: `export HTTP_PROXY=IP:PORT`.




## Update

You can manually check for [new tagtog updates on this link](https://docs.tagtog.net/updates.html). Then:

```shell
./tagtog_on_premises update
./tagtog_on_premises restart latest $TAGTOG_HOME
```


## Change License

Might you have required a license change (e.g. to prolong your current installation or to increment the number of seats), you should also have received the new license details. With these, change the license of your system as follows:

```shell
./tagtog_on_premises change_license NEW_LICENSE_NAME NEW_LICENSE_KEY
```


## Troubleshooting

Upon a problem, try one of the following solutions first.

If your issue or question is not resolved yet, shoot us an email: [support@tagtog.net](mailto:support@tagtog.net). We are also happy to open a slack chat team with you for faster communication.

Please provide detailed information of the problem and **send us always the container logs**: `docker logs tagtog_webapp_1` && `docker logs tagtog_taskmanager_1`.


### Conflicts with ports (_0.0.0.0:80: bind: address already in use_ ...)

By default, tagtog runs and exposes http on the port 80, and https on the port 443. You can change these in two ways:

1. Set the special environmental variables:

```shell
export TAGTOG_HTTP_PORT=9080 # For example
export TAGTOG_HTTPS_PORT=9443 # For example
```

2. Pass the ports parameters into the tagtog running script:

```shell
./tagtog_on_premises restart latest $TAGTOG_HOME 9080 9443
```


### Issues with document uploading, or with the docker container `tagtog_taskmanager_1`:

Try:

1. Removing all queued documents for parsing: `rm "$TAGTOG_HOME/tmp/to_process/*"`
2. Restarting the application: `./tagtog_on_premises restart latest $TAGTOG_HOME`


### Issues in an update

Try:


```shell
echo "0" > LATEST_VERSION
./tagtog_on_premises update
./tagtog_on_premises restart latest $TAGTOG_HOME
```


### Wrong entity offsets on the display

On a few rare cases, the entity offsets from the underlying data model (ann.json) may not match those of the interface. This visually results in some seemingly-broken entities. You might try to fix these errors running the following script:

```shell
# PLEASE, BACKUP YOUR DATA FIRST
./tagtog_on_premises fix_documents latest $TAGTOG_HOME
```


### Lack of writing file access

On some rare cases, the docker containers cannot hold writing access to the `$TAGTOG_HOME` folder and file hierarchy.

In this case, figure out why that could be the case. Anything related to your user not having enough rights?

Otherwise, a quick solution is:

1. Grant all permissions to everybody: `chmod 777 -r $TAGTOG_HOME`
2. Restart the application: `./tagtog_on_premises restart ...`



### ml0 tagtog service taking 100% of CPU

Currently, in some cases On-Premises ML can consume too much CPU. You can verify that it's indeed the ml service (`ml0`) the one overloading the CPU by checking `docker stats`, and looking for the `tagtog_ml0_1` container.

We are working on a stable fix. For now, you can quickly liberate the resources by restarting the `ml0` service only (not the entire tagtog app):

```shell
# export TAGTOG_HOME=...
docker-compose -f docker-compose.override.yaml --project-name tagtog restart ml0
```

**Note**: you can add this to a crontab file to run this every 24 or 12 hours, for example. In this case, better write an absolute path to: `docker-compose.override.yaml`.


### tagtog docker images not found, on a new server installation

Chances are that you must re-do a first-time installation on your new server/instance, like this:

```shell
./tagtog_on_premises first_installation LICENSE_NAME LICENSE_KEY
```

Do the above if you encounter something like this:

```
Creating network "tagtog_default" with the default driver
...
Pulling db (tagtog_db:3.2018-W21.0)...
ERROR: The image for the service you're trying to recreate has been removed. If you continue, volume data could be lost. Consider backing up your data before continuing.

Continue with the new image? [yN]y
Pulling db (tagtog_db:3.2018-W21.0)...
ERROR: pull access denied for tagtog_db, repository does not exist or may require 'docker login'
.............................One process could not be started. Check the logs of 'tagtog_jobmanager_1'
```


### The TAGTOG variables are not available when running as sudo

You NEED NOT to run tagtog as the root user. Actually, we recommend against this.

If for any reason, however, you do want to run as sudo, you might also need to expose your user environment variables to the root user with the `-E` parameter, as follows:

```shell
sudo -E ./tagtog_on_premises restart ...
```
