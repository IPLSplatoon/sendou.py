# Cache Configuration

## Setting Expiry

You can set the expiry time for requests when creating a client. The default expiry time is 30 minutes.

The expiry time is in seconds.

- `-1`: No expiry
- `0`: Don't cache
- *Any other number*: Cache for that many seconds

```python
import sendou
import asyncio

async def run():
    client = sendou.Client("API_KEY", expiry=60)
    player = await client.get_user("USER_ID")
    print(player.name)

asyncio.run(run())
```

## Advanced Configuration

Caching in this module is handled by [aiohttp-client-cache](https://pypi.org/project/aiohttp-client-cache/).

You can pass any aiohttp-client-cache CacheBackend to the client. 
Once you've instantiated the client by passing it through.

You can see the full list of backends [here](https://aiohttp-client-cache.readthedocs.io/en/stable/backends.html).

```python
import sendou
import asyncio
from aiohttp_client_cache import SQLiteBackend

async def run():
    client = sendou.Client("API_KEY", expiry=60)
    client.cache = SQLiteBackend('demo_cache')
    player = await client.get_user("USER_ID")
    print(player.name)

asyncio.run(run())
```