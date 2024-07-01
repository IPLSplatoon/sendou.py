# Sendou.py

An async Python library for interacting with the [Sendou.ink](https://sendou.ink) API.

**Not an official library!**

This library is maintained by [Inkling Performance Labs Productions](https://github.com/iplsplatoon)

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
