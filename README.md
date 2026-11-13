# Speedrun.com clients for Crawlora

Official Crawlora client packages for the hosted Speedrun.com API. Access 20 API endpoints covering game and category discovery, leaderboards, records, variables, and run metadata from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Speedrun.com locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Speedrun.com or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/speedrun`](javascript/README.md)
- Python: [`crawlora-speedrun`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-speedrun`](go.mod)
- Ruby: [`crawlora-speedrun`](ruby/README.md)
- Java: [`net.crawlora:crawlora-speedrun:0.1.0`](java/README.md)
- PHP: [`crawlora/speedrun`](php/README.md)
- Rust: [`crawlora-speedrun`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 20 selected public Speedrun.com API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
