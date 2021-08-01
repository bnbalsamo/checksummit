# ARCHIVED

This repository is archived. I am no longer actively developing/supporting it.

If you are interested in discussing the contents of this repository feel free to contact me
via the contact details provided in the "Author" section below.

A quick note, from me several years in the future (and with considerably more software experience): 
This project was, generally speaking, not written correctly and was not a sound idea.
It doesn't use the proper streaming APIs, and introducing network latency into a hashing operation,
which frequently occurs in tight loops, is pretty terrible.

# checksummit

v0.2.2

[![Build Status](https://travis-ci.org/bnbalsamo/checksummit.svg?branch=master)](https://travis-ci.org/bnbalsamo/checksummit) [![Coverage Status](https://coveralls.io/repos/github/bnbalsamo/checksummit/badge.svg?branch=master)](https://coveralls.io/github/bnbalsamo/checksummit?branch=master)

An API for computing checksums and hashes

# Debug Quickstart
Set environmental variables appropriately
```
./debug.sh
```

# Docker Quickstart
Inject environmental variables appropriately at either buildtime or runtime
```
# docker build . -t checksummit
# docker run -p 5000:80 checksummit --name my_checksummit
```

# Endpoints
## /
### POST
#### Parameters
* file: The file to hash
* hash (repeatable): The algorithms to use
#### Returns
* JSON: {"$hashname": "$hash_hex_digest" for each hash requested}
## /text
### POST
#### Paramters
* text: The text to hash
* hash (repeatable): The algorithms to use
#### Returns
* JSON: {"$hashname": "$hash_hex_digest" for each hash requested}
## /available
### GET
#### Paramters
* None
#### Returns
* JSON: A list of all available hasher names

# Environmental Variables
* CHECKSUMMIT_DISALLOWED_ALGOS: A comma separated list of algorithms to prevent from running
    * Examples
        * md5,
        * md5,sha256,MD5,adler32

# Author
Brian Balsamo <brian@brianbalsamo.com>
