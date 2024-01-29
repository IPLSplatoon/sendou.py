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
- [x] Get Tournament Match Info

## Usage
```python
import sendou

client = sendou.Client("API_KEY")
# Get Sendou's user object
await client.get_user("79237403620945920")
```

## Getting an API Key
To use this library, you must have an API key. You need to DM Sendou for an API Key currently.

