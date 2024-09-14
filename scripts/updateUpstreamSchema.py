"""
Updates the pyproject.toml schema_commit with what sendou.nik github repo has
"""

import toml
import aiohttp
import asyncio


async def main():
    with open("./pyproject.toml", "r") as f:
        toml_data = toml.load(f)
        schema_commit = toml_data["tool"]["sendou-py"]["source"]["schema_commit"]
        schema_path = toml_data["tool"]["sendou-py"]["source"]["schema_path"]

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.github.com/repos/sendouc/sendou.ink/commits?path={schema_path}&per_page=1", headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }) as response:
            if response.status != 200:
                raise Exception("Failed to get response from Github API")
            data = await response.json()
            latest_sha = data[0]["sha"]
            if latest_sha ==  schema_commit:
                print("Schema is already up to date ❎")
                exit(0)
            toml_data["tool"]["sendou-py"]["source"]["schema_commit"] = latest_sha

    with open("../pyproject.toml", "w") as f:
        toml.dump(toml_data, f)

    print("Updated schema_commit in pyproject.toml ✅")
    print(f"Sha: {latest_sha}")

asyncio.run(main())
