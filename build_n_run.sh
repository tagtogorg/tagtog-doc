#!/bin/sh

version=$(cat VERSION)

docker build --tag tagtog-doc:"$version" .

# Just remove the -v volume allocation to serve static files from docker image
docker run -ti --rm -p 4000:4000 -v "$PWD":/my/ tagtog-doc:"$version"
