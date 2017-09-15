# checksummit

v0.0.1

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
### GET
#### Parameters
* None
#### Returns
* JSON: {"status": "Not broken!"}

# Environmental Variables
* None

# Author
Brian Balsamo <brian@brianbalsamo.com>
