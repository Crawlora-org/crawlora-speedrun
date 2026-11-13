# @crawlora-org/speedrun — Speedrun.com API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Speedrun.com API.
It exposes 20 API endpoints for game and category discovery, leaderboards, records, variables, and run metadata through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-javascript-homepage). It does not run a browser or scrape Speedrun.com locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Speedrun.com or its owners.

## Install

```sh
npm install @crawlora-org/speedrun
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { SpeedrunClient } from "@crawlora-org/speedrun";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new SpeedrunClient({ apiKey });
const result1 = await client.games({ name: "Super Mario 64", max: 5 });
console.log(result1);
const result2 = await client.resourceOptions({});
console.log(result2);
```

The client also exports `Client` as an alias for `SpeedrunClient`. Operation
methods are available directly in camelCase and through the `speedrun`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Speedrun.com API endpoints

This package exposes each route below as a direct method and through the `speedrun` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
