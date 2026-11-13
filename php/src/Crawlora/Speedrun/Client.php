<?php

declare(strict_types=1);

namespace Crawlora\Speedrun;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'speedrun';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 20;
    public const OPERATION_IDS = ["speedrun-catalog", "speedrun-categories", "speedrun-category-detail", "speedrun-category-records", "speedrun-category-variables", "speedrun-game-detail", "speedrun-game-leaderboard", "speedrun-games", "speedrun-level-categories", "speedrun-level-detail", "speedrun-level-leaderboard", "speedrun-level-records", "speedrun-level-variables", "speedrun-levels", "speedrun-records", "speedrun-resource-options", "speedrun-run", "speedrun-runs", "speedrun-runs-options", "speedrun-variables"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"speedrun-catalog": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-catalog", "method": "GET", "params": [{"description": "Native metadata collection", "enum": ["platforms", "regions", "gametypes", "developers", "publishers", "genres", "engines"], "in": "path", "name": "kind", "required": true, "type": "string"}, {"description": "Native page size from 1 to 200", "in": "query", "name": "max", "type": "integer"}, {"description": "Native zero-based result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/speedrun/catalogs/{kind}", "pathParams": ["kind"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "speedrun-categories": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-categories", "method": "GET", "params": [{"description": "Native opaque alphanumeric game ID", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Source miscellaneous selector; explicit false preserved", "in": "query", "name": "miscellaneous", "type": "boolean"}, {"description": "Native category order", "enum": ["name", "miscellaneous", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "description": "Metadata embeds", "in": "query", "items": {"enum": ["game", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}/categories", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "miscellaneous", "type": "boolean"}, {"enum": ["name", "miscellaneous", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "enum": ["game", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-category-detail": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-category-detail", "method": "GET", "params": [{"description": "Native category ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/categories/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-category-records": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-category-records", "method": "GET", "params": [{"description": "Native category ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Top places, not runs; API budget 1–200; native default 3", "in": "query", "name": "top", "type": "integer"}, {"description": "Omit empty boards when true; explicit false is retained", "in": "query", "name": "skip_empty", "type": "boolean"}, {"description": "Native page size 1–200", "in": "query", "name": "max", "type": "integer"}, {"description": "Native offset, nonnegative", "in": "query", "name": "offset", "type": "integer"}], "path": "/speedrun/categories/{id}/records", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "skip_empty", "type": "boolean"}, {"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "speedrun-category-variables": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-category-variables", "method": "GET", "params": [{"description": "Native category ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Native contextual order", "enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}], "path": "/speedrun/categories/{id}/variables", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game"], "in": "query", "name": "embed", "type": "array"}, {"enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}], "security": ["ApiKeyAuth"]}, "speedrun-game-detail": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-game-detail", "method": "GET", "params": [{"description": "Native game ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-game-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-game-leaderboard", "method": "GET", "params": [{"description": "Native game ID", "in": "path", "name": "game", "required": true, "type": "string"}, {"description": "Native category ID appropriate to this board", "in": "path", "name": "category", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"default": 1, "description": "Top places, 1–200; API response-budget limit, ties can return more runs", "in": "query", "name": "top", "type": "integer"}, {"description": "Native platform ID from catalogs", "in": "query", "name": "platform", "type": "string"}, {"description": "Native region ID from catalogs", "in": "query", "name": "region", "type": "string"}, {"description": "Omit for both; true for emulators, false for real devices", "in": "query", "name": "emulators", "type": "boolean"}, {"description": "Require a video when true; omission uses source default", "in": "query", "name": "video_only", "type": "boolean"}, {"description": "Native timing method; omission uses source default", "enum": ["realtime", "realtime_noloads", "ingame"], "in": "query", "name": "timing", "type": "string"}, {"description": "Run date cutoff YYYY-MM-DD", "in": "query", "name": "date", "type": "string"}, {"description": "JSON object mapping native variable IDs to value IDs", "in": "query", "name": "variables", "type": "string"}], "path": "/speedrun/leaderboards/{game}/category/{category}", "pathParams": ["game", "category"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "platform", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "emulators", "type": "boolean"}, {"in": "query", "name": "video_only", "type": "boolean"}, {"enum": ["realtime", "realtime_noloads", "ingame"], "in": "query", "name": "timing", "type": "string"}, {"in": "query", "name": "date", "type": "string"}, {"in": "query", "name": "variables", "type": "string"}], "security": ["ApiKeyAuth"]}, "speedrun-games": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-games", "method": "GET", "params": [{"description": "Native game name search", "in": "query", "name": "name", "type": "string"}, {"description": "Platform ID from the platforms catalog", "in": "query", "name": "platform", "type": "string"}, {"description": "Region ID from the regions catalog", "in": "query", "name": "region", "type": "string"}, {"description": "Game-type ID from the gametypes catalog", "in": "query", "name": "gametype", "type": "string"}, {"description": "Native page size1–200, or1–1000 with _bulk=true", "in": "query", "name": "max", "type": "integer"}, {"description": "Native zero-based result offset", "in": "query", "name": "offset", "type": "integer"}, {"description": "Exact native abbreviation", "in": "query", "name": "abbreviation", "type": "string"}, {"description": "Native release year, including0 for unknown", "in": "query", "name": "released", "type": "integer"}, {"description": "Native genre ID from catalog", "in": "query", "name": "genre", "type": "string"}, {"description": "Native engine ID from catalog", "in": "query", "name": "engine", "type": "string"}, {"description": "Native developer ID from catalog", "in": "query", "name": "developer", "type": "string"}, {"description": "Native publisher ID from catalog", "in": "query", "name": "publisher", "type": "string"}, {"description": "Native game order; similarity requires name", "enum": ["name.int", "name.jap", "abbreviation", "released", "created", "similarity"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"description": "Native compact page mode, max up to1000; disables embeds", "in": "query", "name": "_bulk", "type": "boolean"}, {"description": "Legacy inclusion: true only typed games, false only untyped; omission includes both", "in": "query", "name": "romhack", "type": "boolean"}, {"collectionFormat": "csv", "description": "Native metadata embeds", "in": "query", "items": {"enum": ["categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "name", "type": "string"}, {"in": "query", "name": "platform", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "gametype", "type": "string"}, {"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "abbreviation", "type": "string"}, {"in": "query", "name": "released", "type": "integer"}, {"in": "query", "name": "genre", "type": "string"}, {"in": "query", "name": "engine", "type": "string"}, {"in": "query", "name": "developer", "type": "string"}, {"in": "query", "name": "publisher", "type": "string"}, {"enum": ["name.int", "name.jap", "abbreviation", "released", "created", "similarity"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"in": "query", "name": "_bulk", "type": "boolean"}, {"in": "query", "name": "romhack", "type": "boolean"}, {"collectionFormat": "csv", "enum": ["categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-level-categories": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-categories", "method": "GET", "params": [{"description": "Native level ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Native contextual order", "enum": ["name", "miscellaneous", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"description": "Select source miscellaneous flag, preserving explicit false", "in": "query", "name": "miscellaneous", "type": "boolean"}], "path": "/speedrun/levels/{id}/categories", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "variables"], "in": "query", "name": "embed", "type": "array"}, {"enum": ["name", "miscellaneous", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"in": "query", "name": "miscellaneous", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "speedrun-level-detail": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-detail", "method": "GET", "params": [{"description": "Native level ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["categories", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/levels/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["categories", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-level-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-leaderboard", "method": "GET", "params": [{"description": "Native game ID", "in": "path", "name": "game", "required": true, "type": "string"}, {"description": "Native category ID appropriate to this board", "in": "path", "name": "category", "required": true, "type": "string"}, {"description": "Native level ID from game level discovery", "in": "path", "name": "level", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"default": 1, "description": "Top places, 1–200; API response-budget limit, ties can return more runs", "in": "query", "name": "top", "type": "integer"}, {"description": "Native platform ID from catalogs", "in": "query", "name": "platform", "type": "string"}, {"description": "Native region ID from catalogs", "in": "query", "name": "region", "type": "string"}, {"description": "Omit for both; true for emulators, false for real devices", "in": "query", "name": "emulators", "type": "boolean"}, {"description": "Require a video when true; omission uses source default", "in": "query", "name": "video_only", "type": "boolean"}, {"description": "Native timing method; omission uses source default", "enum": ["realtime", "realtime_noloads", "ingame"], "in": "query", "name": "timing", "type": "string"}, {"description": "Run date cutoff YYYY-MM-DD", "in": "query", "name": "date", "type": "string"}, {"description": "JSON object mapping native variable IDs to value IDs", "in": "query", "name": "variables", "type": "string"}], "path": "/speedrun/leaderboards/{game}/level/{level}/{category}", "pathParams": ["game", "category", "level"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "platform", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "emulators", "type": "boolean"}, {"in": "query", "name": "video_only", "type": "boolean"}, {"enum": ["realtime", "realtime_noloads", "ingame"], "in": "query", "name": "timing", "type": "string"}, {"in": "query", "name": "date", "type": "string"}, {"in": "query", "name": "variables", "type": "string"}], "security": ["ApiKeyAuth"]}, "speedrun-level-records": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-records", "method": "GET", "params": [{"description": "Native level ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Top places, not runs; API budget 1–200; native default 3", "in": "query", "name": "top", "type": "integer"}, {"description": "Omit empty boards when true; explicit false is retained", "in": "query", "name": "skip_empty", "type": "boolean"}, {"description": "Native page size 1–200", "in": "query", "name": "max", "type": "integer"}, {"description": "Native offset, nonnegative", "in": "query", "name": "offset", "type": "integer"}], "path": "/speedrun/levels/{id}/records", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "skip_empty", "type": "boolean"}, {"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "speedrun-level-variables": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-variables", "method": "GET", "params": [{"description": "Native level ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Native contextual order", "enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}], "path": "/speedrun/levels/{id}/variables", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game"], "in": "query", "name": "embed", "type": "array"}, {"enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}], "security": ["ApiKeyAuth"]}, "speedrun-levels": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-levels", "method": "GET", "params": [{"description": "Native opaque alphanumeric game ID", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native level order", "enum": ["name", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "description": "Metadata embeds", "in": "query", "items": {"enum": ["categories", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}/levels", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["name", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "enum": ["categories", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-records": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-records", "method": "GET", "params": [{"description": "Native opaque alphanumeric game ID", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native page size from 1 to 200", "in": "query", "name": "max", "type": "integer"}, {"description": "Native zero-based result offset", "in": "query", "name": "offset", "type": "integer"}, {"default": 1, "description": "Top places, API budget1–200; compatibility default1", "in": "query", "name": "top", "type": "integer"}, {"description": "Omit empty boards when true; explicit false preserved", "in": "query", "name": "skip_empty", "type": "boolean"}, {"collectionFormat": "csv", "description": "Metadata embeds", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}/records", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "skip_empty", "type": "boolean"}, {"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-resource-options": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-resource-options", "method": "GET", "params": [], "path": "/speedrun/options", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "speedrun-run": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-run", "method": "GET", "params": [{"description": "Opaque native run ID from runs, records or leaderboards", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "category", "level", "platform", "region"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/runs/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platform", "region"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-runs": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-runs", "method": "GET", "params": [{"description": "Native game ID from games discovery", "in": "query", "name": "game", "type": "string"}, {"description": "Native category ID from category discovery", "in": "query", "name": "category", "type": "string"}, {"description": "Native level ID from level discovery", "in": "query", "name": "level", "type": "string"}, {"description": "Native platform ID from platforms catalog", "in": "query", "name": "platform", "type": "string"}, {"description": "Native region ID from regions catalog", "in": "query", "name": "region", "type": "string"}, {"description": "Omit for both; explicit true or false selects the native device kind", "in": "query", "name": "emulated", "type": "boolean"}, {"description": "Native verification status", "enum": ["new", "verified", "rejected"], "in": "query", "name": "status", "type": "string"}, {"description": "Native ordering", "enum": ["game", "category", "level", "platform", "region", "emulated", "date", "submitted", "status", "verify-date"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native ordering direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"description": "Native page size, 1..200", "in": "query", "maximum": 200, "minimum": 1, "name": "max", "type": "integer"}, {"description": "Native zero-based offset", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "category", "level", "platform", "region"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/runs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "level", "type": "string"}, {"in": "query", "name": "platform", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "emulated", "type": "boolean"}, {"enum": ["new", "verified", "rejected"], "in": "query", "name": "status", "type": "string"}, {"enum": ["game", "category", "level", "platform", "region", "emulated", "date", "submitted", "status", "verify-date"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"collectionFormat": "csv", "enum": ["game", "category", "level", "platform", "region"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-runs-options": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-runs-options", "method": "GET", "params": [], "path": "/speedrun/runs/options", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "speedrun-variables": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-variables", "method": "GET", "params": [{"description": "Native opaque alphanumeric game ID", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native variable order", "enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "description": "Metadata embed", "in": "query", "items": {"enum": ["game"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}/variables", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "enum": ["game"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-speedrun-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function catalog(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-catalog", $params, $responseType);
    }
    public function category_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-category-detail", $params, $responseType);
    }
    public function category_records(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-category-records", $params, $responseType);
    }
    public function category_variables(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-category-variables", $params, $responseType);
    }
    public function games(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-games", $params, $responseType);
    }
    public function game_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-game-detail", $params, $responseType);
    }
    public function categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-categories", $params, $responseType);
    }
    public function levels(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-levels", $params, $responseType);
    }
    public function records(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-records", $params, $responseType);
    }
    public function variables(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-variables", $params, $responseType);
    }
    public function game_leaderboard(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-game-leaderboard", $params, $responseType);
    }
    public function level_leaderboard(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-level-leaderboard", $params, $responseType);
    }
    public function level_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-level-detail", $params, $responseType);
    }
    public function level_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-level-categories", $params, $responseType);
    }
    public function level_records(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-level-records", $params, $responseType);
    }
    public function level_variables(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-level-variables", $params, $responseType);
    }
    public function resource_options(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-resource-options", $params, $responseType);
    }
    public function runs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-runs", $params, $responseType);
    }
    public function runs_options(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-runs-options", $params, $responseType);
    }
    public function run(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("speedrun-run", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
