A RESTful API for computing checksums and hashes

## Endpoints

### /

Supported Methods: POST

Accepts file like objects and supported hash=X form elements

```
$ curl 127.0.0.1:8910 -X POST -F "file"=@file1.txt -F hash=sha256 -F hash=md5
{"md5": "0039ee16ab0d1b77de1e300241c780b9", "sha256": "aff6d8d3665493e2e1be2a05b8b9cc1df8bba6e6c1d10e8d931bb4b6099922d8"}
```
