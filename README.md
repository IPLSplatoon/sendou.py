# sendou.py
An async Python client for Sendou.ink

### **This package is a currently a work in progress.**

## Maintainers
- Vincent Lee

## Dependencies
- aiohttp
- python-dateutil

## Installation
`pip install sendou.py`

## Supported Endpoints
- [x] Get user
- [x] Get Tournament Info
  - [x] Get Tournament Teams
  - [X] Get Tournament Brackets
- [x] Get Tournament Match Info (*by ID not linked to bracket*)

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

