from sendou import Client
import asyncio


async def run():
    client = Client("2c0980f7bde143658273e77b41148e88")
    resp = await client.get_tournament_match("443")
    print(resp)

asyncio.run(run())
