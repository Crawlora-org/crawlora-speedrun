# Crawlora Speedrun.com API client for PHP (`crawlora/speedrun`)

This PHP package calls Crawlora's hosted Speedrun.com API at `https://api.crawlora.net/api/v1`. It exposes 20 endpoints covering game and category discovery, leaderboards, records, variables, and run metadata. It does not call or scrape Speedrun.com directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/speedrun
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Speedrun\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("speedrun-catalog", ['kind' => 'platforms']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 20 API operations.

## Supported Speedrun.com API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-speedrun). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/docs/usage.md).
