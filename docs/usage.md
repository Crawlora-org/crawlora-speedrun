# Speedrun.com API endpoint reference and client usage

This reference lists all 20 public Speedrun.com API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/speedrun`, `crawlora-speedrun`, and `crawlora-speedrun` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Speedrun.com locally; Crawlora is independent from and not endorsed by Speedrun.com or its owners.

The package tracks the public API contract revision `sha256:4103d70f5315c5a4204de3e136abadb3b08fe8c6a11f9447323a0619f0237be8` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `speedrun`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `catalog` | `catalog` | `speedrun.catalog` | `GET /speedrun/catalogs/{kind}` | `kind` (path, required; values: `platforms`, `regions`, `gametypes`, `developers`, `publishers`, `genres`, `engines`), `max` (query, optional), `offset` (query, optional) | Discover Speedrun.com filter catalogs |
| `categories` | `categories` | `speedrun.categories` | `GET /speedrun/games/{id}/categories` | `id` (path, required), `miscellaneous` (query, optional), `orderby` (query, optional; values: `name`, `miscellaneous`, `pos`), `direction` (query, optional; values: `asc`, `desc`), `embed` (query, optional; values: `game`, `variables`) | Get native game categories |
| `categoryDetail` | `category_detail` | `speedrun.category_detail` | `GET /speedrun/categories/{id}` | `id` (path, required), `embed` (query, optional; values: `game`, `variables`) | Get Speedrun category detail |
| `categoryRecords` | `category_records` | `speedrun.category_records` | `GET /speedrun/categories/{id}/records` | `id` (path, required), `embed` (query, optional; values: `game`, `category`, `level`, `platforms`, `regions`, `variables`), `top` (query, optional), `skip_empty` (query, optional), `max` (query, optional), `offset` (query, optional) | Get Speedrun category records |
| `categoryVariables` | `category_variables` | `speedrun.category_variables` | `GET /speedrun/categories/{id}/variables` | `id` (path, required), `embed` (query, optional; values: `game`), `orderby` (query, optional; values: `name`, `mandatory`, `user-defined`, `pos`), `direction` (query, optional; values: `asc`, `desc`) | Get Speedrun category variables |
| `gameDetail` | `game_detail` | `speedrun.game_detail` | `GET /speedrun/games/{id}` | `id` (path, required), `embed` (query, optional; values: `categories`, `levels`, `variables`, `platforms`, `regions`, `gametypes`, `genres`, `engines`, `developers`, `publishers`) | Get Speedrun game detail |
| `gameLeaderboard` | `game_leaderboard` | `speedrun.game_leaderboard` | `GET /speedrun/leaderboards/{game}/category/{category}` | `game` (path, required), `category` (path, required), `embed` (query, optional; values: `game`, `category`, `level`, `platforms`, `regions`, `variables`), `top` (query, optional), `platform` (query, optional), `region` (query, optional), `emulators` (query, optional), `video_only` (query, optional), `timing` (query, optional; values: `realtime`, `realtime_noloads`, `ingame`), `date` (query, optional), `variables` (query, optional) | Get a Speedrun full-game leaderboard |
| `games` | `games` | `speedrun.games` | `GET /speedrun/games` | `name` (query, optional), `platform` (query, optional), `region` (query, optional), `gametype` (query, optional), `max` (query, optional), `offset` (query, optional), `abbreviation` (query, optional), `released` (query, optional), `genre` (query, optional), `engine` (query, optional), `developer` (query, optional), `publisher` (query, optional), `orderby` (query, optional; values: `name.int`, `name.jap`, `abbreviation`, `released`, `created`, `similarity`), `direction` (query, optional; values: `asc`, `desc`), `_bulk` (query, optional), `romhack` (query, optional), `embed` (query, optional; values: `categories`, `levels`, `variables`, `platforms`, `regions`, `gametypes`, `genres`, `engines`, `developers`, `publishers`) | Search Speedrun.com games |
| `levelCategories` | `level_categories` | `speedrun.level_categories` | `GET /speedrun/levels/{id}/categories` | `id` (path, required), `embed` (query, optional; values: `game`, `variables`), `orderby` (query, optional; values: `name`, `miscellaneous`, `pos`), `direction` (query, optional; values: `asc`, `desc`), `miscellaneous` (query, optional) | Get Speedrun level categories |
| `levelDetail` | `level_detail` | `speedrun.level_detail` | `GET /speedrun/levels/{id}` | `id` (path, required), `embed` (query, optional; values: `categories`, `variables`) | Get Speedrun level detail |
| `levelLeaderboard` | `level_leaderboard` | `speedrun.level_leaderboard` | `GET /speedrun/leaderboards/{game}/level/{level}/{category}` | `game` (path, required), `category` (path, required), `level` (path, required), `embed` (query, optional; values: `game`, `category`, `level`, `platforms`, `regions`, `variables`), `top` (query, optional), `platform` (query, optional), `region` (query, optional), `emulators` (query, optional), `video_only` (query, optional), `timing` (query, optional; values: `realtime`, `realtime_noloads`, `ingame`), `date` (query, optional), `variables` (query, optional) | Get a Speedrun individual-level leaderboard |
| `levelRecords` | `level_records` | `speedrun.level_records` | `GET /speedrun/levels/{id}/records` | `id` (path, required), `embed` (query, optional; values: `game`, `category`, `level`, `platforms`, `regions`, `variables`), `top` (query, optional), `skip_empty` (query, optional), `max` (query, optional), `offset` (query, optional) | Get Speedrun level records |
| `levels` | `levels` | `speedrun.levels` | `GET /speedrun/games/{id}/levels` | `id` (path, required), `orderby` (query, optional; values: `name`, `pos`), `direction` (query, optional; values: `asc`, `desc`), `embed` (query, optional; values: `categories`, `variables`) | Get native game levels |
| `levelVariables` | `level_variables` | `speedrun.level_variables` | `GET /speedrun/levels/{id}/variables` | `id` (path, required), `embed` (query, optional; values: `game`), `orderby` (query, optional; values: `name`, `mandatory`, `user-defined`, `pos`), `direction` (query, optional; values: `asc`, `desc`) | Get Speedrun level variables |
| `records` | `records` | `speedrun.records` | `GET /speedrun/games/{id}/records` | `id` (path, required), `max` (query, optional), `offset` (query, optional), `top` (query, optional), `skip_empty` (query, optional), `embed` (query, optional; values: `game`, `category`, `level`, `platforms`, `regions`, `variables`) | Get native top-one game record boards |
| `resourceOptions` | `resource_options` | `speedrun.resource_options` | `GET /speedrun/options` | — | Discover Speedrun contextual resource options |
| `run` | `run` | `speedrun.run` | `GET /speedrun/runs/{id}` | `id` (path, required), `embed` (query, optional; values: `game`, `category`, `level`, `platform`, `region`) | Read native Speedrun run metadata |
| `runs` | `runs` | `speedrun.runs` | `GET /speedrun/runs` | `game` (query, optional), `category` (query, optional), `level` (query, optional), `platform` (query, optional), `region` (query, optional), `emulated` (query, optional), `status` (query, optional; values: `new`, `verified`, `rejected`), `orderby` (query, optional; values: `game`, `category`, `level`, `platform`, `region`, `emulated`, `date`, `submitted`, `status`, `verify-date`), `direction` (query, optional; values: `asc`, `desc`), `max` (query, optional), `offset` (query, optional), `embed` (query, optional; values: `game`, `category`, `level`, `platform`, `region`) | List native Speedrun run metadata |
| `runsOptions` | `runs_options` | `speedrun.runs_options` | `GET /speedrun/runs/options` | — | Discover Speedrun run query options |
| `variables` | `variables` | `speedrun.variables` | `GET /speedrun/games/{id}/variables` | `id` (path, required), `orderby` (query, optional; values: `name`, `mandatory`, `user-defined`, `pos`), `direction` (query, optional; values: `asc`, `desc`), `embed` (query, optional; values: `game`) | Get native game variable definitions |

## Client forms

- JavaScript: import `SpeedrunClient` (also exported as `Client`) from `@crawlora-org/speedrun`; use `new SpeedrunClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `SpeedrunClient` (also exported as `Client`) from `crawlora_speedrun`; use `with SpeedrunClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncSpeedrunClient`, used with `async with` and `await`.
- Rust: add `crawlora-speedrun` with Cargo; import `Client` and the generated operation parameter struct, then call `client.speedrun.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
