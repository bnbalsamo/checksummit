A RESTful API for computing checksums and hashes

## Endpoints

### /

Supported Methods: POST

Accepts file like objects and supported hash=X form elements

e.g.

```
curl -F 'file1=@file1.txt'  -F 'hash=md5' http://127.0.0.1:5000
```

Returns
```
{"file1": {"md5": "84dcc94da3adb52b53ae4fa38fe49e5d"}}
```

---

```
curl -F 'file1=@LICENSE' -F 'file2=@debug.sh' -F 'hash=sha256' -F 'hash=md5' http://127.0.0.1:5000
```

Returns
```
{"file1": {"sha256": "589ed823e9a84c56feb95ac58e7cf384626b9cbf4fda2a907bc36e103de1bad2", "md5": "84dcc94da3adb52b53ae4fa38fe49e5d"}, "file2": {"sha256": "a0d393fb1b3de368a3cf52736723b18516ca4c697c9c43e07a3bbcb3560071ed", "md5": "ae98c59b5e3e0954d21d26bcd7c3f102"}}
```
