# sendou.py
An async Python client for Sendou.ink

[![Documentation Status](https://readthedocs.org/projects/sendoupy/badge/?version=latest)](https://sendoupy.readthedocs.io/latest/?badge=latest)

- [Documentation](https://sendou.opensource.iplabs.work/)
- [PyPi](https://pypi.org/project/sendou.py/)

## Maintainers
- Vincent Lee

## Dependencies
- aiohttp
- [aiohttp-client-cache](https://pypi.org/project/aiohttp-client-cache/)
- python-dateutil

## Installation
`pip install sendou.py`

## Supported Endpoints
- [x] Get user
- [x] Get Calendar Entries
- [x] Get Tournament Info
  - [x] Get Tournament Teams
  - [X] Get Tournament Brackets
    - [x] Get Tournament Match Info

## Usage
```python
import sendou
import asyncio

async def run():
    client = sendou.Client("API_KEY")
    player = await client.get_user("USER_ID")
    print(player.name)

asyncio.run(run())
```

## Getting an API Key
To use this library, you must have an API key. You need to DM Sendou for an API Key currently.

## Development
For development, you'll need [Poetry](https://python-poetry.org) installed for dependency management and building distributions

### Dev Dependencies
When install dependencies for development run

```bash
poetry install --with=dev
```

*In CI you way want to run `poetry install --with=dev,ci` that includes CI dependencies for GitHub Actions*

### Testing
This package has *some* tests, these are written with pytest and can be run with

```bash
pytest
```

*You likely need to run `poetry install` before executing pytest*

### Tracking Upstream Schema
This package uses sendou.ink's [Public API Schema](https://github.com/Sendouc/sendou.ink/blob/rewrite/app/features/api-public/schema.ts) 
file to design the models uses in the package. To keep track of where the package is in relation to the upstream schema, 
the commit sha of the upstream schema is kept in the `pyproject.toml` file under `tool.sendou-py.source`.

There are 2 scripts that help keep this package inline with the upstream schema.

#### Upstream Schema Commit SHA checker
This script uses the GitHub API to check that the SHA stored in `tool.sendou-py.source` matches the latest commit for 
for the upstream schema.

```bash
python3 python3 scripts/checkUpstreamSchema.py
```


#### Update local SHA with Upstream Schema Commit SHA
This script pulls down the latest SHA hash for the upstream schema and saves it to the `pyproject.toml` file

```bash
python3 scripts/updateUpstreamSchema.py
```

**This should only be run after dev has checked their changes match the upstream schema**