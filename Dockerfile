FROM ruby:alpine

RUN apk update && \
    apk add gcc make libc-dev g++ && \
    gem install bundle jekyll

RUN apk add git

# ---

COPY . /my/
WORKDIR /my/

RUN bundle install

# ---

ENTRYPOINT bundle exec jekyll serve
