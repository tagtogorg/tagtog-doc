#!/bin/sh

# "--incremental" builds are faster but might not livereload as much -- remove if necessary
bundle exec jekyll serve --host "0.0.0.0" --livereload --incremental
