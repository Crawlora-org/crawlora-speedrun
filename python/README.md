# crawlora-speedrun — Speedrun.com API client for Python

Python client for Crawlora's hosted Speedrun.com API. It exposes 20 API endpoints covering game and category discovery, leaderboards, records, variables, and run metadata. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-python-homepage); the package does not run a browser or scrape
Speedrun.com locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Speedrun.com or its owners.

## Install

```sh
python -m pip install crawlora-speedrun
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_speedrun import SpeedrunClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with SpeedrunClient(api_key=api_key) as client:
    result_1 = client.games(name='Super Mario 64', max=5)
    print(result_1)
    result_2 = client.resource_options()
    print(result_2)
```

The package also exports `Client` as an alias for `SpeedrunClient`. Operation
methods are available directly in snake_case and through the `speedrun`
group. The async package client is `AsyncSpeedrunClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_speedrun import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.games(name='Super Mario 64', max=5)
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/examples/python.py) for a complete usage example.

## Supported Speedrun.com API endpoints

This package exposes every route below through direct snake_case methods and the `speedrun` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/speedrun/catalogs/{kind}` | `speedrun-catalog` | Discover Speedrun.com filter catalogs |
| `GET` | `/speedrun/categories/{id}` | `speedrun-category-detail` | Get Speedrun category detail |
| `GET` | `/speedrun/categories/{id}/records` | `speedrun-category-records` | Get Speedrun category records |
| `GET` | `/speedrun/categories/{id}/variables` | `speedrun-category-variables` | Get Speedrun category variables |
| `GET` | `/speedrun/games` | `speedrun-games` | Search Speedrun.com games |
| `GET` | `/speedrun/games/{id}` | `speedrun-game-detail` | Get Speedrun game detail |
| `GET` | `/speedrun/games/{id}/categories` | `speedrun-categories` | Get native game categories |
| `GET` | `/speedrun/games/{id}/levels` | `speedrun-levels` | Get native game levels |
| `GET` | `/speedrun/games/{id}/records` | `speedrun-records` | Get native top-one game record boards |
| `GET` | `/speedrun/games/{id}/variables` | `speedrun-variables` | Get native game variable definitions |
| `GET` | `/speedrun/leaderboards/{game}/category/{category}` | `speedrun-game-leaderboard` | Get a Speedrun full-game leaderboard |
| `GET` | `/speedrun/leaderboards/{game}/level/{level}/{category}` | `speedrun-level-leaderboard` | Get a Speedrun individual-level leaderboard |
| `GET` | `/speedrun/levels/{id}` | `speedrun-level-detail` | Get Speedrun level detail |
| `GET` | `/speedrun/levels/{id}/categories` | `speedrun-level-categories` | Get Speedrun level categories |
| `GET` | `/speedrun/levels/{id}/records` | `speedrun-level-records` | Get Speedrun level records |
| `GET` | `/speedrun/levels/{id}/variables` | `speedrun-level-variables` | Get Speedrun level variables |
| `GET` | `/speedrun/options` | `speedrun-resource-options` | Discover Speedrun contextual resource options |
| `GET` | `/speedrun/runs` | `speedrun-runs` | List native Speedrun run metadata |
| `GET` | `/speedrun/runs/options` | `speedrun-runs-options` | Discover Speedrun run query options |
| `GET` | `/speedrun/runs/{id}` | `speedrun-run` | Read native Speedrun run metadata |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
