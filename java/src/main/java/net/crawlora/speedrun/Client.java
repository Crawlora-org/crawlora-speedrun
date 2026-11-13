package net.crawlora.speedrun;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Speedrun.com endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 20;
    public static final List<String> OPERATION_IDS = List.of(
            "speedrun-catalog",
            "speedrun-categories",
            "speedrun-category-detail",
            "speedrun-category-records",
            "speedrun-category-variables",
            "speedrun-game-detail",
            "speedrun-game-leaderboard",
            "speedrun-games",
            "speedrun-level-categories",
            "speedrun-level-detail",
            "speedrun-level-leaderboard",
            "speedrun-level-records",
            "speedrun-level-variables",
            "speedrun-levels",
            "speedrun-records",
            "speedrun-resource-options",
            "speedrun-run",
            "speedrun-runs",
            "speedrun-runs-options",
            "speedrun-variables"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("speedrun-catalog", new Operation("speedrun-catalog", "GET", "/speedrun/catalogs/{kind}", Map.ofEntries(Map.entry("kind", new Param("kind", "path", true, "string", List.of("platforms", "regions", "gametypes", "developers", "publishers", "genres", "engines"), "csv")), Map.entry("max", new Param("max", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("speedrun-category-detail", new Operation("speedrun-category-detail", "GET", "/speedrun/categories/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "variables"), "csv"))), List.of("application/json")));
        operations.put("speedrun-category-records", new Operation("speedrun-category-records", "GET", "/speedrun/categories/{id}/records", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "category", "level", "platforms", "regions", "variables"), "csv")), Map.entry("top", new Param("top", "query", false, "integer", List.of(), "csv")), Map.entry("skip_empty", new Param("skip_empty", "query", false, "boolean", List.of(), "csv")), Map.entry("max", new Param("max", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("speedrun-category-variables", new Operation("speedrun-category-variables", "GET", "/speedrun/categories/{id}/variables", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game"), "csv")), Map.entry("orderby", new Param("orderby", "query", false, "string", List.of("name", "mandatory", "user-defined", "pos"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("asc", "desc"), "csv"))), List.of("application/json")));
        operations.put("speedrun-games", new Operation("speedrun-games", "GET", "/speedrun/games", Map.ofEntries(Map.entry("name", new Param("name", "query", false, "string", List.of(), "csv")), Map.entry("platform", new Param("platform", "query", false, "string", List.of(), "csv")), Map.entry("region", new Param("region", "query", false, "string", List.of(), "csv")), Map.entry("gametype", new Param("gametype", "query", false, "string", List.of(), "csv")), Map.entry("max", new Param("max", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("abbreviation", new Param("abbreviation", "query", false, "string", List.of(), "csv")), Map.entry("released", new Param("released", "query", false, "integer", List.of(), "csv")), Map.entry("genre", new Param("genre", "query", false, "string", List.of(), "csv")), Map.entry("engine", new Param("engine", "query", false, "string", List.of(), "csv")), Map.entry("developer", new Param("developer", "query", false, "string", List.of(), "csv")), Map.entry("publisher", new Param("publisher", "query", false, "string", List.of(), "csv")), Map.entry("orderby", new Param("orderby", "query", false, "string", List.of("name.int", "name.jap", "abbreviation", "released", "created", "similarity"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("_bulk", new Param("_bulk", "query", false, "boolean", List.of(), "csv")), Map.entry("romhack", new Param("romhack", "query", false, "boolean", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"), "csv"))), List.of("application/json")));
        operations.put("speedrun-game-detail", new Operation("speedrun-game-detail", "GET", "/speedrun/games/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("categories", "levels", "variables", "platforms", "regions", "gametypes", "genres", "engines", "developers", "publishers"), "csv"))), List.of("application/json")));
        operations.put("speedrun-categories", new Operation("speedrun-categories", "GET", "/speedrun/games/{id}/categories", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("miscellaneous", new Param("miscellaneous", "query", false, "boolean", List.of(), "csv")), Map.entry("orderby", new Param("orderby", "query", false, "string", List.of("name", "miscellaneous", "pos"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "variables"), "csv"))), List.of("application/json")));
        operations.put("speedrun-levels", new Operation("speedrun-levels", "GET", "/speedrun/games/{id}/levels", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("orderby", new Param("orderby", "query", false, "string", List.of("name", "pos"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("categories", "variables"), "csv"))), List.of("application/json")));
        operations.put("speedrun-records", new Operation("speedrun-records", "GET", "/speedrun/games/{id}/records", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("max", new Param("max", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("top", new Param("top", "query", false, "integer", List.of(), "csv")), Map.entry("skip_empty", new Param("skip_empty", "query", false, "boolean", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "category", "level", "platforms", "regions", "variables"), "csv"))), List.of("application/json")));
        operations.put("speedrun-variables", new Operation("speedrun-variables", "GET", "/speedrun/games/{id}/variables", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("orderby", new Param("orderby", "query", false, "string", List.of("name", "mandatory", "user-defined", "pos"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game"), "csv"))), List.of("application/json")));
        operations.put("speedrun-game-leaderboard", new Operation("speedrun-game-leaderboard", "GET", "/speedrun/leaderboards/{game}/category/{category}", Map.ofEntries(Map.entry("game", new Param("game", "path", true, "string", List.of(), "csv")), Map.entry("category", new Param("category", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "category", "level", "platforms", "regions", "variables"), "csv")), Map.entry("top", new Param("top", "query", false, "integer", List.of(), "csv")), Map.entry("platform", new Param("platform", "query", false, "string", List.of(), "csv")), Map.entry("region", new Param("region", "query", false, "string", List.of(), "csv")), Map.entry("emulators", new Param("emulators", "query", false, "boolean", List.of(), "csv")), Map.entry("video_only", new Param("video_only", "query", false, "boolean", List.of(), "csv")), Map.entry("timing", new Param("timing", "query", false, "string", List.of("realtime", "realtime_noloads", "ingame"), "csv")), Map.entry("date", new Param("date", "query", false, "string", List.of(), "csv")), Map.entry("variables", new Param("variables", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("speedrun-level-leaderboard", new Operation("speedrun-level-leaderboard", "GET", "/speedrun/leaderboards/{game}/level/{level}/{category}", Map.ofEntries(Map.entry("game", new Param("game", "path", true, "string", List.of(), "csv")), Map.entry("category", new Param("category", "path", true, "string", List.of(), "csv")), Map.entry("level", new Param("level", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "category", "level", "platforms", "regions", "variables"), "csv")), Map.entry("top", new Param("top", "query", false, "integer", List.of(), "csv")), Map.entry("platform", new Param("platform", "query", false, "string", List.of(), "csv")), Map.entry("region", new Param("region", "query", false, "string", List.of(), "csv")), Map.entry("emulators", new Param("emulators", "query", false, "boolean", List.of(), "csv")), Map.entry("video_only", new Param("video_only", "query", false, "boolean", List.of(), "csv")), Map.entry("timing", new Param("timing", "query", false, "string", List.of("realtime", "realtime_noloads", "ingame"), "csv")), Map.entry("date", new Param("date", "query", false, "string", List.of(), "csv")), Map.entry("variables", new Param("variables", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("speedrun-level-detail", new Operation("speedrun-level-detail", "GET", "/speedrun/levels/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("categories", "variables"), "csv"))), List.of("application/json")));
        operations.put("speedrun-level-categories", new Operation("speedrun-level-categories", "GET", "/speedrun/levels/{id}/categories", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "variables"), "csv")), Map.entry("orderby", new Param("orderby", "query", false, "string", List.of("name", "miscellaneous", "pos"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("miscellaneous", new Param("miscellaneous", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("speedrun-level-records", new Operation("speedrun-level-records", "GET", "/speedrun/levels/{id}/records", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "category", "level", "platforms", "regions", "variables"), "csv")), Map.entry("top", new Param("top", "query", false, "integer", List.of(), "csv")), Map.entry("skip_empty", new Param("skip_empty", "query", false, "boolean", List.of(), "csv")), Map.entry("max", new Param("max", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("speedrun-level-variables", new Operation("speedrun-level-variables", "GET", "/speedrun/levels/{id}/variables", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game"), "csv")), Map.entry("orderby", new Param("orderby", "query", false, "string", List.of("name", "mandatory", "user-defined", "pos"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("asc", "desc"), "csv"))), List.of("application/json")));
        operations.put("speedrun-resource-options", new Operation("speedrun-resource-options", "GET", "/speedrun/options", Map.of(), List.of("application/json")));
        operations.put("speedrun-runs", new Operation("speedrun-runs", "GET", "/speedrun/runs", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of(), "csv")), Map.entry("category", new Param("category", "query", false, "string", List.of(), "csv")), Map.entry("level", new Param("level", "query", false, "string", List.of(), "csv")), Map.entry("platform", new Param("platform", "query", false, "string", List.of(), "csv")), Map.entry("region", new Param("region", "query", false, "string", List.of(), "csv")), Map.entry("emulated", new Param("emulated", "query", false, "boolean", List.of(), "csv")), Map.entry("status", new Param("status", "query", false, "string", List.of("new", "verified", "rejected"), "csv")), Map.entry("orderby", new Param("orderby", "query", false, "string", List.of("game", "category", "level", "platform", "region", "emulated", "date", "submitted", "status", "verify-date"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("max", new Param("max", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "category", "level", "platform", "region"), "csv"))), List.of("application/json")));
        operations.put("speedrun-runs-options", new Operation("speedrun-runs-options", "GET", "/speedrun/runs/options", Map.of(), List.of("application/json")));
        operations.put("speedrun-run", new Operation("speedrun-run", "GET", "/speedrun/runs/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("embed", new Param("embed", "query", false, "array", List.of("game", "category", "level", "platform", "region"), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Speedrun.com operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object catalog(Map<String, ?> params) { return request("speedrun-catalog", params); }
    public Object categoryDetail(Map<String, ?> params) { return request("speedrun-category-detail", params); }
    public Object categoryRecords(Map<String, ?> params) { return request("speedrun-category-records", params); }
    public Object categoryVariables(Map<String, ?> params) { return request("speedrun-category-variables", params); }
    public Object games(Map<String, ?> params) { return request("speedrun-games", params); }
    public Object gameDetail(Map<String, ?> params) { return request("speedrun-game-detail", params); }
    public Object categories(Map<String, ?> params) { return request("speedrun-categories", params); }
    public Object levels(Map<String, ?> params) { return request("speedrun-levels", params); }
    public Object records(Map<String, ?> params) { return request("speedrun-records", params); }
    public Object variables(Map<String, ?> params) { return request("speedrun-variables", params); }
    public Object gameLeaderboard(Map<String, ?> params) { return request("speedrun-game-leaderboard", params); }
    public Object levelLeaderboard(Map<String, ?> params) { return request("speedrun-level-leaderboard", params); }
    public Object levelDetail(Map<String, ?> params) { return request("speedrun-level-detail", params); }
    public Object levelCategories(Map<String, ?> params) { return request("speedrun-level-categories", params); }
    public Object levelRecords(Map<String, ?> params) { return request("speedrun-level-records", params); }
    public Object levelVariables(Map<String, ?> params) { return request("speedrun-level-variables", params); }
    public Object resourceOptions(Map<String, ?> params) { return request("speedrun-resource-options", params); }
    public Object runs(Map<String, ?> params) { return request("speedrun-runs", params); }
    public Object runsOptions(Map<String, ?> params) { return request("speedrun-runs-options", params); }
    public Object run(Map<String, ?> params) { return request("speedrun-run", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
