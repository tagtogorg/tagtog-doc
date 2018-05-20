FROM ruby:alpine

RUN apk update && \
    apk add gcc make libc-dev g++ && \
    gem install bundle jekyll

RUN apk add git

# ---

RUN mkdir /my/
WORKDIR /my/

COPY Gemfile* *.gemspec /my/
RUN bundle install

COPY . /my/

# ---

ENTRYPOINT bundle exec jekyll serve
