require "json"
require "net/http"
require "uri"

module Crawlora
  module Speedrun
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"speedrun-catalog": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-catalog", "method": "GET", "params": [{"description": "Native metadata collection", "enum": ["platforms", "regions", "gametypes", "developers", "publishers", "genres", "engines"], "in": "path", "name": "kind", "required": true, "type": "string"}, {"description": "Native page size from 1 to 200", "in": "query", "name": "max", "type": "integer"}, {"description": "Native zero-based result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/speedrun/catalogs/{kind}", "pathParams": ["kind"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "speedrun-categories": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-categories", "method": "GET", "params": [{"description": "Native opaque alphanumeric game ID", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Source miscellaneous selector; explicit false preserved", "in": "query", "name": "miscellaneous", "type": "boolean"}, {"description": "Native category order", "enum": ["name", "miscellaneous", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "description": "Metadata embeds", "in": "query", "items": {"enum": ["game", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}/categories", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "miscellaneous", "type": "boolean"}, {"enum": ["name", "miscellaneous", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "enum": ["game", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-category-detail": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-category-detail", "method": "GET", "params": [{"description": "Native category ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/categories/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-category-records": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-category-records", "method": "GET", "params": [{"description": "Native category ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Top places, not runs; API budget 1–200; native default 3", "in": "query", "name": "top", "type": "integer"}, {"description": "Omit empty boards when true; explicit false is retained", "in": "query", "name": "skip_empty", "type": "boolean"}, {"description": "Native page size 1–200", "in": "query", "name": "max", "type": "integer"}, {"description": "Native offset, nonnegative", "in": "query", "name": "offset", "type": "integer"}], "path": "/speedrun/categories/{id}/records", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "skip_empty", "type": "boolean"}, {"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "speedrun-category-variables": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-category-variables", "method": "GET", "params": [{"description": "Native category ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Native contextual order", "enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}], "path": "/speedrun/categories/{id}/variables", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game"], "in": "query", "name": "embed", "type": "array"}, {"enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}], "security": ["ApiKeyAuth"]}, "speedrun-game-detail": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-game-detail", "method": "GET", "params": [{"description": "Native game ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-game-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-game-leaderboard", "method": "GET", "params": [{"description": "Native game ID", "in": "path", "name": "game", "required": true, "type": "string"}, {"description": "Native category ID appropriate to this board", "in": "path", "name": "category", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"default": 1, "description": "Top places, 1–200; API response-budget limit, ties can return more runs", "in": "query", "name": "top", "type": "integer"}, {"description": "Native platform ID from catalogs", "in": "query", "name": "platform", "type": "string"}, {"description": "Native region ID from catalogs", "in": "query", "name": "region", "type": "string"}, {"description": "Omit for both; true for emulators, false for real devices", "in": "query", "name": "emulators", "type": "boolean"}, {"description": "Require a video when true; omission uses source default", "in": "query", "name": "video_only", "type": "boolean"}, {"description": "Native timing method; omission uses source default", "enum": ["realtime", "realtime_noloads", "ingame"], "in": "query", "name": "timing", "type": "string"}, {"description": "Run date cutoff YYYY-MM-DD", "in": "query", "name": "date", "type": "string"}, {"description": "JSON object mapping native variable IDs to value IDs", "in": "query", "name": "variables", "type": "string"}], "path": "/speedrun/leaderboards/{game}/category/{category}", "pathParams": ["game", "category"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "platform", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "emulators", "type": "boolean"}, {"in": "query", "name": "video_only", "type": "boolean"}, {"enum": ["realtime", "realtime_noloads", "ingame"], "in": "query", "name": "timing", "type": "string"}, {"in": "query", "name": "date", "type": "string"}, {"in": "query", "name": "variables", "type": "string"}], "security": ["ApiKeyAuth"]}, "speedrun-games": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-games", "method": "GET", "params": [{"description": "Native game name search", "in": "query", "name": "name", "type": "string"}, {"description": "Platform ID from the platforms catalog", "in": "query", "name": "platform", "type": "string"}, {"description": "Region ID from the regions catalog", "in": "query", "name": "region", "type": "string"}, {"description": "Game-type ID from the gametypes catalog", "in": "query", "name": "gametype", "type": "string"}, {"description": "Native page size1–200, or1–1000 with _bulk=true", "in": "query", "name": "max", "type": "integer"}, {"description": "Native zero-based result offset", "in": "query", "name": "offset", "type": "integer"}, {"description": "Exact native abbreviation", "in": "query", "name": "abbreviation", "type": "string"}, {"description": "Native release year, including0 for unknown", "in": "query", "name": "released", "type": "integer"}, {"description": "Native genre ID from catalog", "in": "query", "name": "genre", "type": "string"}, {"description": "Native engine ID from catalog", "in": "query", "name": "engine", "type": "string"}, {"description": "Native developer ID from catalog", "in": "query", "name": "developer", "type": "string"}, {"description": "Native publisher ID from catalog", "in": "query", "name": "publisher", "type": "string"}, {"description": "Native game order; similarity requires name", "enum": ["name.int", "name.jap", "abbreviation", "released", "created", "similarity"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"description": "Native compact page mode, max up to1000; disables embeds", "in": "query", "name": "_bulk", "type": "boolean"}, {"description": "Legacy inclusion: true only typed games, false only untyped; omission includes both", "in": "query", "name": "romhack", "type": "boolean"}, {"collectionFormat": "csv", "description": "Native metadata embeds", "in": "query", "items": {"enum": ["categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "name", "type": "string"}, {"in": "query", "name": "platform", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "gametype", "type": "string"}, {"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "abbreviation", "type": "string"}, {"in": "query", "name": "released", "type": "integer"}, {"in": "query", "name": "genre", "type": "string"}, {"in": "query", "name": "engine", "type": "string"}, {"in": "query", "name": "developer", "type": "string"}, {"in": "query", "name": "publisher", "type": "string"}, {"enum": ["name.int", "name.jap", "abbreviation", "released", "created", "similarity"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"in": "query", "name": "_bulk", "type": "boolean"}, {"in": "query", "name": "romhack", "type": "boolean"}, {"collectionFormat": "csv", "enum": ["categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-level-categories": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-categories", "method": "GET", "params": [{"description": "Native level ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Native contextual order", "enum": ["name", "miscellaneous", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"description": "Select source miscellaneous flag, preserving explicit false", "in": "query", "name": "miscellaneous", "type": "boolean"}], "path": "/speedrun/levels/{id}/categories", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "variables"], "in": "query", "name": "embed", "type": "array"}, {"enum": ["name", "miscellaneous", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"in": "query", "name": "miscellaneous", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "speedrun-level-detail": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-detail", "method": "GET", "params": [{"description": "Native level ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["categories", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/levels/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["categories", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-level-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-leaderboard", "method": "GET", "params": [{"description": "Native game ID", "in": "path", "name": "game", "required": true, "type": "string"}, {"description": "Native category ID appropriate to this board", "in": "path", "name": "category", "required": true, "type": "string"}, {"description": "Native level ID from game level discovery", "in": "path", "name": "level", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"default": 1, "description": "Top places, 1–200; API response-budget limit, ties can return more runs", "in": "query", "name": "top", "type": "integer"}, {"description": "Native platform ID from catalogs", "in": "query", "name": "platform", "type": "string"}, {"description": "Native region ID from catalogs", "in": "query", "name": "region", "type": "string"}, {"description": "Omit for both; true for emulators, false for real devices", "in": "query", "name": "emulators", "type": "boolean"}, {"description": "Require a video when true; omission uses source default", "in": "query", "name": "video_only", "type": "boolean"}, {"description": "Native timing method; omission uses source default", "enum": ["realtime", "realtime_noloads", "ingame"], "in": "query", "name": "timing", "type": "string"}, {"description": "Run date cutoff YYYY-MM-DD", "in": "query", "name": "date", "type": "string"}, {"description": "JSON object mapping native variable IDs to value IDs", "in": "query", "name": "variables", "type": "string"}], "path": "/speedrun/leaderboards/{game}/level/{level}/{category}", "pathParams": ["game", "category", "level"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "platform", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "emulators", "type": "boolean"}, {"in": "query", "name": "video_only", "type": "boolean"}, {"enum": ["realtime", "realtime_noloads", "ingame"], "in": "query", "name": "timing", "type": "string"}, {"in": "query", "name": "date", "type": "string"}, {"in": "query", "name": "variables", "type": "string"}], "security": ["ApiKeyAuth"]}, "speedrun-level-records": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-records", "method": "GET", "params": [{"description": "Native level ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Top places, not runs; API budget 1–200; native default 3", "in": "query", "name": "top", "type": "integer"}, {"description": "Omit empty boards when true; explicit false is retained", "in": "query", "name": "skip_empty", "type": "boolean"}, {"description": "Native page size 1–200", "in": "query", "name": "max", "type": "integer"}, {"description": "Native offset, nonnegative", "in": "query", "name": "offset", "type": "integer"}], "path": "/speedrun/levels/{id}/records", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "skip_empty", "type": "boolean"}, {"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "speedrun-level-variables": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-level-variables", "method": "GET", "params": [{"description": "Native level ID, opaque alphanumeric", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game"], "type": "string"}, "name": "embed", "type": "array"}, {"description": "Native contextual order", "enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}], "path": "/speedrun/levels/{id}/variables", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game"], "in": "query", "name": "embed", "type": "array"}, {"enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}], "security": ["ApiKeyAuth"]}, "speedrun-levels": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-levels", "method": "GET", "params": [{"description": "Native opaque alphanumeric game ID", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native level order", "enum": ["name", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "description": "Metadata embeds", "in": "query", "items": {"enum": ["categories", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}/levels", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["name", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "enum": ["categories", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-records": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-records", "method": "GET", "params": [{"description": "Native opaque alphanumeric game ID", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native page size from 1 to 200", "in": "query", "name": "max", "type": "integer"}, {"description": "Native zero-based result offset", "in": "query", "name": "offset", "type": "integer"}, {"default": 1, "description": "Top places, API budget1–200; compatibility default1", "in": "query", "name": "top", "type": "integer"}, {"description": "Omit empty boards when true; explicit false preserved", "in": "query", "name": "skip_empty", "type": "boolean"}, {"collectionFormat": "csv", "description": "Metadata embeds", "in": "query", "items": {"enum": ["game", "category", "level", "platforms", "regions", "variables"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}/records", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "top", "type": "integer"}, {"in": "query", "name": "skip_empty", "type": "boolean"}, {"collectionFormat": "csv", "enum": ["game", "category", "level", "platforms", "regions", "variables"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-resource-options": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-resource-options", "method": "GET", "params": [], "path": "/speedrun/options", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "speedrun-run": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-run", "method": "GET", "params": [{"description": "Opaque native run ID from runs, records or leaderboards", "in": "path", "name": "id", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "category", "level", "platform", "region"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/runs/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"collectionFormat": "csv", "enum": ["game", "category", "level", "platform", "region"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-runs": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-runs", "method": "GET", "params": [{"description": "Native game ID from games discovery", "in": "query", "name": "game", "type": "string"}, {"description": "Native category ID from category discovery", "in": "query", "name": "category", "type": "string"}, {"description": "Native level ID from level discovery", "in": "query", "name": "level", "type": "string"}, {"description": "Native platform ID from platforms catalog", "in": "query", "name": "platform", "type": "string"}, {"description": "Native region ID from regions catalog", "in": "query", "name": "region", "type": "string"}, {"description": "Omit for both; explicit true or false selects the native device kind", "in": "query", "name": "emulated", "type": "boolean"}, {"description": "Native verification status", "enum": ["new", "verified", "rejected"], "in": "query", "name": "status", "type": "string"}, {"description": "Native ordering", "enum": ["game", "category", "level", "platform", "region", "emulated", "date", "submitted", "status", "verify-date"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native ordering direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"description": "Native page size, 1..200", "in": "query", "maximum": 200, "minimum": 1, "name": "max", "type": "integer"}, {"description": "Native zero-based offset", "in": "query", "minimum": 0, "name": "offset", "type": "integer"}, {"collectionFormat": "csv", "description": "Native metadata embeds, comma-separated", "in": "query", "items": {"enum": ["game", "category", "level", "platform", "region"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/runs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "level", "type": "string"}, {"in": "query", "name": "platform", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "emulated", "type": "boolean"}, {"enum": ["new", "verified", "rejected"], "in": "query", "name": "status", "type": "string"}, {"enum": ["game", "category", "level", "platform", "region", "emulated", "date", "submitted", "status", "verify-date"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"in": "query", "name": "max", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"collectionFormat": "csv", "enum": ["game", "category", "level", "platform", "region"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}, "speedrun-runs-options": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-runs-options", "method": "GET", "params": [], "path": "/speedrun/runs/options", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "speedrun-variables": {"bodyParam": null, "bodyRequired": false, "id": "speedrun-variables", "method": "GET", "params": [{"description": "Native opaque alphanumeric game ID", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native variable order", "enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"description": "Native order direction", "enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "description": "Metadata embed", "in": "query", "items": {"enum": ["game"], "type": "string"}, "name": "embed", "type": "array"}], "path": "/speedrun/games/{id}/variables", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["name", "mandatory", "user-defined", "pos"], "in": "query", "name": "orderby", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "direction", "type": "string"}, {"collectionFormat": "csv", "enum": ["game"], "in": "query", "name": "embed", "type": "array"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["speedrun-catalog", "speedrun-categories", "speedrun-category-detail", "speedrun-category-records", "speedrun-category-variables", "speedrun-game-detail", "speedrun-game-leaderboard", "speedrun-games", "speedrun-level-categories", "speedrun-level-detail", "speedrun-level-leaderboard", "speedrun-level-records", "speedrun-level-variables", "speedrun-levels", "speedrun-records", "speedrun-resource-options", "speedrun-run", "speedrun-runs", "speedrun-runs-options", "speedrun-variables"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-speedrun-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('catalog') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-catalog', params, response_type: response_type)
      end
      define_method('category_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-category-detail', params, response_type: response_type)
      end
      define_method('category_records') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-category-records', params, response_type: response_type)
      end
      define_method('category_variables') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-category-variables', params, response_type: response_type)
      end
      define_method('games') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-games', params, response_type: response_type)
      end
      define_method('game_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-game-detail', params, response_type: response_type)
      end
      define_method('categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-categories', params, response_type: response_type)
      end
      define_method('levels') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-levels', params, response_type: response_type)
      end
      define_method('records') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-records', params, response_type: response_type)
      end
      define_method('variables') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-variables', params, response_type: response_type)
      end
      define_method('game_leaderboard') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-game-leaderboard', params, response_type: response_type)
      end
      define_method('level_leaderboard') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-level-leaderboard', params, response_type: response_type)
      end
      define_method('level_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-level-detail', params, response_type: response_type)
      end
      define_method('level_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-level-categories', params, response_type: response_type)
      end
      define_method('level_records') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-level-records', params, response_type: response_type)
      end
      define_method('level_variables') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-level-variables', params, response_type: response_type)
      end
      define_method('resource_options') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-resource-options', params, response_type: response_type)
      end
      define_method('runs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-runs', params, response_type: response_type)
      end
      define_method('runs_options') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-runs-options', params, response_type: response_type)
      end
      define_method('run') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('speedrun-run', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
