FROM ruby:alpine

# ---

# Install jekyll-system dependencies

RUN apk update && \
    apk add gcc make libc-dev g++ && \
    gem install bundle jekyll

RUN apk add git

# ---

# Install pages and derived dependencies

RUN mkdir /my/
WORKDIR /my/

COPY Gemfile* *.gemspec /my/
RUN bundle install

COPY . /my/

# ---

# Install python dependencies for python script

RUN apk add python3
RUN pip3 install requests

# ---

EXPOSE 4000

ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "--incremental", "--host", "0.0.0.0"]
