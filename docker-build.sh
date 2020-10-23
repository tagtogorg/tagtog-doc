#!/bin/sh

cd "$(dirname "$0")"

version=$(cat VERSION)

docker build --tag tagtog-doc:"$version" .
