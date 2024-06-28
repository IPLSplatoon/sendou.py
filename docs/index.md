# Sendou.py

An async Python library for interacting with the [Sendou.ink](https://sendou.ink) API.

**Not an official library!**

This library is maintained by [Inkling Performance Labs Productions](https://github.com/iplsplatoon)

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

client = sendou.Client("API_KEY")
# Get Sendou's user object
await client.get_user("79237403620945920")
```

## Getting an API Key
To use this library, you must have an API key. You need to DM Sendou for an API Key currently.
