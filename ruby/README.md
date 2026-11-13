# Crawlora Speedrun.com API client for Ruby (`crawlora-speedrun`)

This Ruby gem calls Crawlora's hosted Speedrun.com API at `https://api.crawlora.net/api/v1`. It exposes 20 endpoints covering game and category discovery, leaderboards, records, variables, and run metadata; it does not call or scrape Speedrun.com directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-speedrun"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/speedrun"

client = Crawlora::Speedrun::Client.new
result = client.request("speedrun-catalog", JSON.parse("{\"kind\": \"platforms\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 20 API operations.

```ruby
client = Crawlora::Speedrun::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Speedrun.com API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-speedrun) for account setup, the API operation reference, and release history.
