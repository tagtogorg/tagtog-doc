#!/bin/sh

cd "$(dirname "$0")"

./docker-build.sh && ./docker-run.sh
