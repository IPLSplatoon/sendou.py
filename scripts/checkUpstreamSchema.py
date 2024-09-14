"""
Check Upstream Schema

This script checks the version store in pyproject.toml with the latest schema SHA in the sendou.ink Github repo
and raises an error if there is a mismatch.
"""

import tomllib
import asyncio
import aiohttp


async def main():
    # Open TOML and get data
    with open("./pyproject.toml", "rb") as f:
        data = tomllib.load(f)
        schema_commit = data["tool"]["sendou-py"]["source"]["schema_commit"]
        schema_path = data["tool"]["sendou-py"]["source"]["schema_path"]

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.github.com/repos/sendouc/sendou.ink/commits?path={schema_path}&per_page=1", headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }) as response:
            if response.status != 200:
                raise Exception("Failed to get response from Github API")
            data = await response.json()
            latest_sha = data[0]["sha"]
            if schema_commit != latest_sha:
                print(f"Schema is not up to date. Project SHA: {schema_commit}, Latest SHA: {latest_sha}")
                exit(1)
            print("Schema is up to date ✅")
            exit(0)

asyncio.run(main())
