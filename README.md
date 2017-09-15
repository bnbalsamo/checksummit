# checksummit

v0.1.0

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
