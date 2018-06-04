#!/bin/sh

new_version=$1

cd "$(dirname "$0")"

printf "$new_version" | tee "VERSION"
sed -i '' "s/version: .*/version: $new_version/" _config.yml
