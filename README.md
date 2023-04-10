# static assets for fastapi_amis_admin

make fastapi & amis-admin work offline without CDN.

## Features

this package provide following static assets used by fastapi & amis_admin to make them work without CDN:
- swagger
- redoc
- amis

## Install

 `pip install fastapi-amis-admin-offline`

## Usage examples
```python
from fastapi import FastAPI
from fastapi_amis_admin_offline import patch_offline


app = FastAPI(debug=settings.debug)
patch_offline(app)
```
if fastapi_amis_admin is installed, it will also patch the Page and App components to use local static assets.
