from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelSpeedrunResponseDoc = TypedDict('ModelSpeedrunResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
}, total=False)

ModelSpeedrunRunOptionsResponseDoc = TypedDict('ModelSpeedrunRunOptionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpeedrunRunResourceOptions],
    'msg': NotRequired[str],
}, total=False)

ModelSpeedrunRunResourceOptions = TypedDict('ModelSpeedrunRunResourceOptions', {
    'catalog_paths': NotRequired[dict[str, str]],
    'directions': NotRequired[list[str]],
    'embeds': NotRequired[list[str]],
    'orderby': NotRequired[list[str]],
    'statuses': NotRequired[list[str]],
}, total=False)

ModelSpeedrunOptionsResponseDoc = TypedDict('ModelSpeedrunOptionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, ModelSpeedrunResourceOption]],
    'msg': NotRequired[str],
}, total=False)

ModelSpeedrunResourceOption = TypedDict('ModelSpeedrunResourceOption', {
    'catalog_paths': NotRequired[dict[str, str]],
    'directions': NotRequired[list[str]],
    'embeds': NotRequired[list[str]],
    'orderby': NotRequired[list[str]],
    'timing': NotRequired[list[str]],
}, total=False)

SpeedrunCatalogResponse = ModelSpeedrunResponseDoc
SpeedrunCatalogParams = TypedDict('SpeedrunCatalogParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': Required[Literal['platforms', 'regions', 'gametypes', 'developers', 'publishers', 'genres', 'engines']],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunCategoryDetailResponse = ModelSpeedrunResponseDoc
SpeedrunCategoryDetailParams = TypedDict('SpeedrunCategoryDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'variables']]],
}, total=False)

SpeedrunCategoryRecordsResponse = ModelSpeedrunResponseDoc
SpeedrunCategoryRecordsParams = TypedDict('SpeedrunCategoryRecordsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunCategoryVariablesResponse = ModelSpeedrunResponseDoc
SpeedrunCategoryVariablesParams = TypedDict('SpeedrunCategoryVariablesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game']]],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
}, total=False)

SpeedrunGamesResponse = ModelSpeedrunResponseDoc
SpeedrunGamesParams = TypedDict('SpeedrunGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'name': NotRequired[str],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'gametype': NotRequired[str],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'abbreviation': NotRequired[str],
    'released': NotRequired[int],
    'genre': NotRequired[str],
    'engine': NotRequired[str],
    'developer': NotRequired[str],
    'publisher': NotRequired[str],
    'orderby': NotRequired[Literal['name.int', 'name.jap', 'abbreviation', 'released', 'created', 'similarity']],
    'direction': NotRequired[Literal['asc', 'desc']],
    '_bulk': NotRequired[bool],
    'romhack': NotRequired[bool],
    'embed': NotRequired[list[Literal['categories', 'levels', 'variables', 'platforms', 'regions', 'gametypes', 'genres', 'engines', 'developers', 'publishers']]],
}, total=False)

SpeedrunGameDetailResponse = ModelSpeedrunResponseDoc
SpeedrunGameDetailParams = TypedDict('SpeedrunGameDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['categories', 'levels', 'variables', 'platforms', 'regions', 'gametypes', 'genres', 'engines', 'developers', 'publishers']]],
}, total=False)

SpeedrunCategoriesResponse = ModelSpeedrunResponseDoc
SpeedrunCategoriesParams = TypedDict('SpeedrunCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'miscellaneous': NotRequired[bool],
    'orderby': NotRequired[Literal['name', 'miscellaneous', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['game', 'variables']]],
}, total=False)

SpeedrunLevelsResponse = ModelSpeedrunResponseDoc
SpeedrunLevelsParams = TypedDict('SpeedrunLevelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'orderby': NotRequired[Literal['name', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['categories', 'variables']]],
}, total=False)

SpeedrunRecordsResponse = ModelSpeedrunResponseDoc
SpeedrunRecordsParams = TypedDict('SpeedrunRecordsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
}, total=False)

SpeedrunVariablesResponse = ModelSpeedrunResponseDoc
SpeedrunVariablesParams = TypedDict('SpeedrunVariablesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['game']]],
}, total=False)

SpeedrunGameLeaderboardResponse = ModelSpeedrunResponseDoc
SpeedrunGameLeaderboardParams = TypedDict('SpeedrunGameLeaderboardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[str],
    'category': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulators': NotRequired[bool],
    'video_only': NotRequired[bool],
    'timing': NotRequired[Literal['realtime', 'realtime_noloads', 'ingame']],
    'date': NotRequired[str],
    'variables': NotRequired[str],
}, total=False)

SpeedrunLevelLeaderboardResponse = ModelSpeedrunResponseDoc
SpeedrunLevelLeaderboardParams = TypedDict('SpeedrunLevelLeaderboardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[str],
    'category': Required[str],
    'level': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulators': NotRequired[bool],
    'video_only': NotRequired[bool],
    'timing': NotRequired[Literal['realtime', 'realtime_noloads', 'ingame']],
    'date': NotRequired[str],
    'variables': NotRequired[str],
}, total=False)

SpeedrunLevelDetailResponse = ModelSpeedrunResponseDoc
SpeedrunLevelDetailParams = TypedDict('SpeedrunLevelDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['categories', 'variables']]],
}, total=False)

SpeedrunLevelCategoriesResponse = ModelSpeedrunResponseDoc
SpeedrunLevelCategoriesParams = TypedDict('SpeedrunLevelCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'variables']]],
    'orderby': NotRequired[Literal['name', 'miscellaneous', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'miscellaneous': NotRequired[bool],
}, total=False)

SpeedrunLevelRecordsResponse = ModelSpeedrunResponseDoc
SpeedrunLevelRecordsParams = TypedDict('SpeedrunLevelRecordsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunLevelVariablesResponse = ModelSpeedrunResponseDoc
SpeedrunLevelVariablesParams = TypedDict('SpeedrunLevelVariablesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game']]],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
}, total=False)

SpeedrunResourceOptionsResponse = ModelSpeedrunOptionsResponseDoc
SpeedrunResourceOptionsParams = TypedDict('SpeedrunResourceOptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

SpeedrunRunsResponse = ModelSpeedrunResponseDoc
SpeedrunRunsParams = TypedDict('SpeedrunRunsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[str],
    'category': NotRequired[str],
    'level': NotRequired[str],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulated': NotRequired[bool],
    'status': NotRequired[Literal['new', 'verified', 'rejected']],
    'orderby': NotRequired[Literal['game', 'category', 'level', 'platform', 'region', 'emulated', 'date', 'submitted', 'status', 'verify-date']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platform', 'region']]],
}, total=False)

SpeedrunRunsOptionsResponse = ModelSpeedrunRunOptionsResponseDoc
SpeedrunRunsOptionsParams = TypedDict('SpeedrunRunsOptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

SpeedrunRunResponse = ModelSpeedrunResponseDoc
SpeedrunRunParams = TypedDict('SpeedrunRunParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platform', 'region']]],
}, total=False)

class SpeedrunGroup:
    @overload
    def catalog(self, **params: Unpack[SpeedrunCatalogStreamParams]) -> BinaryIO: ...
    @overload
    def catalog(self, **params: Unpack[SpeedrunCatalogTextResponseParams]) -> str: ...
    @overload
    def catalog(self, **params: Unpack[SpeedrunCatalogDefaultParams]) -> SpeedrunCatalogResponse: ...
    @overload
    def category_detail(self, **params: Unpack[SpeedrunCategoryDetailStreamParams]) -> BinaryIO: ...
    @overload
    def category_detail(self, **params: Unpack[SpeedrunCategoryDetailTextResponseParams]) -> str: ...
    @overload
    def category_detail(self, **params: Unpack[SpeedrunCategoryDetailDefaultParams]) -> SpeedrunCategoryDetailResponse: ...
    @overload
    def category_records(self, **params: Unpack[SpeedrunCategoryRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def category_records(self, **params: Unpack[SpeedrunCategoryRecordsTextResponseParams]) -> str: ...
    @overload
    def category_records(self, **params: Unpack[SpeedrunCategoryRecordsDefaultParams]) -> SpeedrunCategoryRecordsResponse: ...
    @overload
    def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesStreamParams]) -> BinaryIO: ...
    @overload
    def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesTextResponseParams]) -> str: ...
    @overload
    def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesDefaultParams]) -> SpeedrunCategoryVariablesResponse: ...
    @overload
    def games(self, **params: Unpack[SpeedrunGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[SpeedrunGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[SpeedrunGamesDefaultParams]) -> SpeedrunGamesResponse: ...
    @overload
    def game_detail(self, **params: Unpack[SpeedrunGameDetailStreamParams]) -> BinaryIO: ...
    @overload
    def game_detail(self, **params: Unpack[SpeedrunGameDetailTextResponseParams]) -> str: ...
    @overload
    def game_detail(self, **params: Unpack[SpeedrunGameDetailDefaultParams]) -> SpeedrunGameDetailResponse: ...
    @overload
    def categories(self, **params: Unpack[SpeedrunCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[SpeedrunCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[SpeedrunCategoriesDefaultParams]) -> SpeedrunCategoriesResponse: ...
    @overload
    def levels(self, **params: Unpack[SpeedrunLevelsStreamParams]) -> BinaryIO: ...
    @overload
    def levels(self, **params: Unpack[SpeedrunLevelsTextResponseParams]) -> str: ...
    @overload
    def levels(self, **params: Unpack[SpeedrunLevelsDefaultParams]) -> SpeedrunLevelsResponse: ...
    @overload
    def records(self, **params: Unpack[SpeedrunRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def records(self, **params: Unpack[SpeedrunRecordsTextResponseParams]) -> str: ...
    @overload
    def records(self, **params: Unpack[SpeedrunRecordsDefaultParams]) -> SpeedrunRecordsResponse: ...
    @overload
    def variables(self, **params: Unpack[SpeedrunVariablesStreamParams]) -> BinaryIO: ...
    @overload
    def variables(self, **params: Unpack[SpeedrunVariablesTextResponseParams]) -> str: ...
    @overload
    def variables(self, **params: Unpack[SpeedrunVariablesDefaultParams]) -> SpeedrunVariablesResponse: ...
    @overload
    def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardTextResponseParams]) -> str: ...
    @overload
    def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardDefaultParams]) -> SpeedrunGameLeaderboardResponse: ...
    @overload
    def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardTextResponseParams]) -> str: ...
    @overload
    def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardDefaultParams]) -> SpeedrunLevelLeaderboardResponse: ...
    @overload
    def level_detail(self, **params: Unpack[SpeedrunLevelDetailStreamParams]) -> BinaryIO: ...
    @overload
    def level_detail(self, **params: Unpack[SpeedrunLevelDetailTextResponseParams]) -> str: ...
    @overload
    def level_detail(self, **params: Unpack[SpeedrunLevelDetailDefaultParams]) -> SpeedrunLevelDetailResponse: ...
    @overload
    def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesTextResponseParams]) -> str: ...
    @overload
    def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesDefaultParams]) -> SpeedrunLevelCategoriesResponse: ...
    @overload
    def level_records(self, **params: Unpack[SpeedrunLevelRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def level_records(self, **params: Unpack[SpeedrunLevelRecordsTextResponseParams]) -> str: ...
    @overload
    def level_records(self, **params: Unpack[SpeedrunLevelRecordsDefaultParams]) -> SpeedrunLevelRecordsResponse: ...
    @overload
    def level_variables(self, **params: Unpack[SpeedrunLevelVariablesStreamParams]) -> BinaryIO: ...
    @overload
    def level_variables(self, **params: Unpack[SpeedrunLevelVariablesTextResponseParams]) -> str: ...
    @overload
    def level_variables(self, **params: Unpack[SpeedrunLevelVariablesDefaultParams]) -> SpeedrunLevelVariablesResponse: ...
    @overload
    def resource_options(self, **params: Unpack[SpeedrunResourceOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def resource_options(self, **params: Unpack[SpeedrunResourceOptionsTextResponseParams]) -> str: ...
    @overload
    def resource_options(self, **params: Unpack[SpeedrunResourceOptionsDefaultParams]) -> SpeedrunResourceOptionsResponse: ...
    @overload
    def runs(self, **params: Unpack[SpeedrunRunsStreamParams]) -> BinaryIO: ...
    @overload
    def runs(self, **params: Unpack[SpeedrunRunsTextResponseParams]) -> str: ...
    @overload
    def runs(self, **params: Unpack[SpeedrunRunsDefaultParams]) -> SpeedrunRunsResponse: ...
    @overload
    def runs_options(self, **params: Unpack[SpeedrunRunsOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def runs_options(self, **params: Unpack[SpeedrunRunsOptionsTextResponseParams]) -> str: ...
    @overload
    def runs_options(self, **params: Unpack[SpeedrunRunsOptionsDefaultParams]) -> SpeedrunRunsOptionsResponse: ...
    @overload
    def run(self, **params: Unpack[SpeedrunRunStreamParams]) -> BinaryIO: ...
    @overload
    def run(self, **params: Unpack[SpeedrunRunTextResponseParams]) -> str: ...
    @overload
    def run(self, **params: Unpack[SpeedrunRunDefaultParams]) -> SpeedrunRunResponse: ...

OperationId = Literal[
    'speedrun-catalog',
    'speedrun-category-detail',
    'speedrun-category-records',
    'speedrun-category-variables',
    'speedrun-games',
    'speedrun-game-detail',
    'speedrun-categories',
    'speedrun-levels',
    'speedrun-records',
    'speedrun-variables',
    'speedrun-game-leaderboard',
    'speedrun-level-leaderboard',
    'speedrun-level-detail',
    'speedrun-level-categories',
    'speedrun-level-records',
    'speedrun-level-variables',
    'speedrun-resource-options',
    'speedrun-runs',
    'speedrun-runs-options',
    'speedrun-run',
]

class CrawloraClient:
    speedrun: SpeedrunGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-catalog'],
        params: SpeedrunCatalogParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCatalogResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-category-detail'],
        params: SpeedrunCategoryDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCategoryDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-category-records'],
        params: SpeedrunCategoryRecordsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCategoryRecordsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-category-variables'],
        params: SpeedrunCategoryVariablesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCategoryVariablesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-games'],
        params: SpeedrunGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-game-detail'],
        params: SpeedrunGameDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunGameDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-categories'],
        params: SpeedrunCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-levels'],
        params: SpeedrunLevelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-records'],
        params: SpeedrunRecordsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunRecordsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-variables'],
        params: SpeedrunVariablesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunVariablesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-game-leaderboard'],
        params: SpeedrunGameLeaderboardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunGameLeaderboardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-level-leaderboard'],
        params: SpeedrunLevelLeaderboardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelLeaderboardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-level-detail'],
        params: SpeedrunLevelDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-level-categories'],
        params: SpeedrunLevelCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-level-records'],
        params: SpeedrunLevelRecordsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelRecordsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-level-variables'],
        params: SpeedrunLevelVariablesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelVariablesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-resource-options'],
        params: SpeedrunResourceOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunResourceOptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-runs'],
        params: SpeedrunRunsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunRunsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-runs-options'],
        params: SpeedrunRunsOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunRunsOptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['speedrun-run'],
        params: SpeedrunRunParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunRunResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-catalog'],
        params: SpeedrunCatalogParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCatalogResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-category-detail'],
        params: SpeedrunCategoryDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCategoryDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-category-records'],
        params: SpeedrunCategoryRecordsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCategoryRecordsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-category-variables'],
        params: SpeedrunCategoryVariablesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCategoryVariablesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-games'],
        params: SpeedrunGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-game-detail'],
        params: SpeedrunGameDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunGameDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-categories'],
        params: SpeedrunCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-levels'],
        params: SpeedrunLevelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-records'],
        params: SpeedrunRecordsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunRecordsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-variables'],
        params: SpeedrunVariablesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunVariablesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-game-leaderboard'],
        params: SpeedrunGameLeaderboardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunGameLeaderboardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-level-leaderboard'],
        params: SpeedrunLevelLeaderboardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelLeaderboardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-level-detail'],
        params: SpeedrunLevelDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-level-categories'],
        params: SpeedrunLevelCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-level-records'],
        params: SpeedrunLevelRecordsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelRecordsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-level-variables'],
        params: SpeedrunLevelVariablesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunLevelVariablesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-resource-options'],
        params: SpeedrunResourceOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunResourceOptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-runs'],
        params: SpeedrunRunsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunRunsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-runs-options'],
        params: SpeedrunRunsOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunRunsOptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['speedrun-run'],
        params: SpeedrunRunParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpeedrunRunResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class SpeedrunClient(CrawloraClient):
    def __enter__(self) -> SpeedrunClient: ...
    @overload
    def catalog(self, **params: Unpack[SpeedrunCatalogStreamParams]) -> BinaryIO: ...
    @overload
    def catalog(self, **params: Unpack[SpeedrunCatalogTextResponseParams]) -> str: ...
    @overload
    def catalog(self, **params: Unpack[SpeedrunCatalogDefaultParams]) -> SpeedrunCatalogResponse: ...
    @overload
    def category_detail(self, **params: Unpack[SpeedrunCategoryDetailStreamParams]) -> BinaryIO: ...
    @overload
    def category_detail(self, **params: Unpack[SpeedrunCategoryDetailTextResponseParams]) -> str: ...
    @overload
    def category_detail(self, **params: Unpack[SpeedrunCategoryDetailDefaultParams]) -> SpeedrunCategoryDetailResponse: ...
    @overload
    def category_records(self, **params: Unpack[SpeedrunCategoryRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def category_records(self, **params: Unpack[SpeedrunCategoryRecordsTextResponseParams]) -> str: ...
    @overload
    def category_records(self, **params: Unpack[SpeedrunCategoryRecordsDefaultParams]) -> SpeedrunCategoryRecordsResponse: ...
    @overload
    def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesStreamParams]) -> BinaryIO: ...
    @overload
    def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesTextResponseParams]) -> str: ...
    @overload
    def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesDefaultParams]) -> SpeedrunCategoryVariablesResponse: ...
    @overload
    def games(self, **params: Unpack[SpeedrunGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[SpeedrunGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[SpeedrunGamesDefaultParams]) -> SpeedrunGamesResponse: ...
    @overload
    def game_detail(self, **params: Unpack[SpeedrunGameDetailStreamParams]) -> BinaryIO: ...
    @overload
    def game_detail(self, **params: Unpack[SpeedrunGameDetailTextResponseParams]) -> str: ...
    @overload
    def game_detail(self, **params: Unpack[SpeedrunGameDetailDefaultParams]) -> SpeedrunGameDetailResponse: ...
    @overload
    def categories(self, **params: Unpack[SpeedrunCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[SpeedrunCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[SpeedrunCategoriesDefaultParams]) -> SpeedrunCategoriesResponse: ...
    @overload
    def levels(self, **params: Unpack[SpeedrunLevelsStreamParams]) -> BinaryIO: ...
    @overload
    def levels(self, **params: Unpack[SpeedrunLevelsTextResponseParams]) -> str: ...
    @overload
    def levels(self, **params: Unpack[SpeedrunLevelsDefaultParams]) -> SpeedrunLevelsResponse: ...
    @overload
    def records(self, **params: Unpack[SpeedrunRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def records(self, **params: Unpack[SpeedrunRecordsTextResponseParams]) -> str: ...
    @overload
    def records(self, **params: Unpack[SpeedrunRecordsDefaultParams]) -> SpeedrunRecordsResponse: ...
    @overload
    def variables(self, **params: Unpack[SpeedrunVariablesStreamParams]) -> BinaryIO: ...
    @overload
    def variables(self, **params: Unpack[SpeedrunVariablesTextResponseParams]) -> str: ...
    @overload
    def variables(self, **params: Unpack[SpeedrunVariablesDefaultParams]) -> SpeedrunVariablesResponse: ...
    @overload
    def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardTextResponseParams]) -> str: ...
    @overload
    def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardDefaultParams]) -> SpeedrunGameLeaderboardResponse: ...
    @overload
    def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardTextResponseParams]) -> str: ...
    @overload
    def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardDefaultParams]) -> SpeedrunLevelLeaderboardResponse: ...
    @overload
    def level_detail(self, **params: Unpack[SpeedrunLevelDetailStreamParams]) -> BinaryIO: ...
    @overload
    def level_detail(self, **params: Unpack[SpeedrunLevelDetailTextResponseParams]) -> str: ...
    @overload
    def level_detail(self, **params: Unpack[SpeedrunLevelDetailDefaultParams]) -> SpeedrunLevelDetailResponse: ...
    @overload
    def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesTextResponseParams]) -> str: ...
    @overload
    def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesDefaultParams]) -> SpeedrunLevelCategoriesResponse: ...
    @overload
    def level_records(self, **params: Unpack[SpeedrunLevelRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def level_records(self, **params: Unpack[SpeedrunLevelRecordsTextResponseParams]) -> str: ...
    @overload
    def level_records(self, **params: Unpack[SpeedrunLevelRecordsDefaultParams]) -> SpeedrunLevelRecordsResponse: ...
    @overload
    def level_variables(self, **params: Unpack[SpeedrunLevelVariablesStreamParams]) -> BinaryIO: ...
    @overload
    def level_variables(self, **params: Unpack[SpeedrunLevelVariablesTextResponseParams]) -> str: ...
    @overload
    def level_variables(self, **params: Unpack[SpeedrunLevelVariablesDefaultParams]) -> SpeedrunLevelVariablesResponse: ...
    @overload
    def resource_options(self, **params: Unpack[SpeedrunResourceOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def resource_options(self, **params: Unpack[SpeedrunResourceOptionsTextResponseParams]) -> str: ...
    @overload
    def resource_options(self, **params: Unpack[SpeedrunResourceOptionsDefaultParams]) -> SpeedrunResourceOptionsResponse: ...
    @overload
    def runs(self, **params: Unpack[SpeedrunRunsStreamParams]) -> BinaryIO: ...
    @overload
    def runs(self, **params: Unpack[SpeedrunRunsTextResponseParams]) -> str: ...
    @overload
    def runs(self, **params: Unpack[SpeedrunRunsDefaultParams]) -> SpeedrunRunsResponse: ...
    @overload
    def runs_options(self, **params: Unpack[SpeedrunRunsOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def runs_options(self, **params: Unpack[SpeedrunRunsOptionsTextResponseParams]) -> str: ...
    @overload
    def runs_options(self, **params: Unpack[SpeedrunRunsOptionsDefaultParams]) -> SpeedrunRunsOptionsResponse: ...
    @overload
    def run(self, **params: Unpack[SpeedrunRunStreamParams]) -> BinaryIO: ...
    @overload
    def run(self, **params: Unpack[SpeedrunRunTextResponseParams]) -> str: ...
    @overload
    def run(self, **params: Unpack[SpeedrunRunDefaultParams]) -> SpeedrunRunResponse: ...

class AsyncSpeedrunClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncSpeedrunClient: ...
    speedrun: _AsyncSpeedrunGroup
    @overload
    async def catalog(self, **params: Unpack[SpeedrunCatalogStreamParams]) -> BinaryIO: ...
    @overload
    async def catalog(self, **params: Unpack[SpeedrunCatalogTextResponseParams]) -> str: ...
    @overload
    async def catalog(self, **params: Unpack[SpeedrunCatalogDefaultParams]) -> SpeedrunCatalogResponse: ...
    @overload
    async def category_detail(self, **params: Unpack[SpeedrunCategoryDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def category_detail(self, **params: Unpack[SpeedrunCategoryDetailTextResponseParams]) -> str: ...
    @overload
    async def category_detail(self, **params: Unpack[SpeedrunCategoryDetailDefaultParams]) -> SpeedrunCategoryDetailResponse: ...
    @overload
    async def category_records(self, **params: Unpack[SpeedrunCategoryRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def category_records(self, **params: Unpack[SpeedrunCategoryRecordsTextResponseParams]) -> str: ...
    @overload
    async def category_records(self, **params: Unpack[SpeedrunCategoryRecordsDefaultParams]) -> SpeedrunCategoryRecordsResponse: ...
    @overload
    async def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesStreamParams]) -> BinaryIO: ...
    @overload
    async def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesTextResponseParams]) -> str: ...
    @overload
    async def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesDefaultParams]) -> SpeedrunCategoryVariablesResponse: ...
    @overload
    async def games(self, **params: Unpack[SpeedrunGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[SpeedrunGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[SpeedrunGamesDefaultParams]) -> SpeedrunGamesResponse: ...
    @overload
    async def game_detail(self, **params: Unpack[SpeedrunGameDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def game_detail(self, **params: Unpack[SpeedrunGameDetailTextResponseParams]) -> str: ...
    @overload
    async def game_detail(self, **params: Unpack[SpeedrunGameDetailDefaultParams]) -> SpeedrunGameDetailResponse: ...
    @overload
    async def categories(self, **params: Unpack[SpeedrunCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[SpeedrunCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[SpeedrunCategoriesDefaultParams]) -> SpeedrunCategoriesResponse: ...
    @overload
    async def levels(self, **params: Unpack[SpeedrunLevelsStreamParams]) -> BinaryIO: ...
    @overload
    async def levels(self, **params: Unpack[SpeedrunLevelsTextResponseParams]) -> str: ...
    @overload
    async def levels(self, **params: Unpack[SpeedrunLevelsDefaultParams]) -> SpeedrunLevelsResponse: ...
    @overload
    async def records(self, **params: Unpack[SpeedrunRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def records(self, **params: Unpack[SpeedrunRecordsTextResponseParams]) -> str: ...
    @overload
    async def records(self, **params: Unpack[SpeedrunRecordsDefaultParams]) -> SpeedrunRecordsResponse: ...
    @overload
    async def variables(self, **params: Unpack[SpeedrunVariablesStreamParams]) -> BinaryIO: ...
    @overload
    async def variables(self, **params: Unpack[SpeedrunVariablesTextResponseParams]) -> str: ...
    @overload
    async def variables(self, **params: Unpack[SpeedrunVariablesDefaultParams]) -> SpeedrunVariablesResponse: ...
    @overload
    async def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardDefaultParams]) -> SpeedrunGameLeaderboardResponse: ...
    @overload
    async def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardDefaultParams]) -> SpeedrunLevelLeaderboardResponse: ...
    @overload
    async def level_detail(self, **params: Unpack[SpeedrunLevelDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def level_detail(self, **params: Unpack[SpeedrunLevelDetailTextResponseParams]) -> str: ...
    @overload
    async def level_detail(self, **params: Unpack[SpeedrunLevelDetailDefaultParams]) -> SpeedrunLevelDetailResponse: ...
    @overload
    async def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesTextResponseParams]) -> str: ...
    @overload
    async def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesDefaultParams]) -> SpeedrunLevelCategoriesResponse: ...
    @overload
    async def level_records(self, **params: Unpack[SpeedrunLevelRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def level_records(self, **params: Unpack[SpeedrunLevelRecordsTextResponseParams]) -> str: ...
    @overload
    async def level_records(self, **params: Unpack[SpeedrunLevelRecordsDefaultParams]) -> SpeedrunLevelRecordsResponse: ...
    @overload
    async def level_variables(self, **params: Unpack[SpeedrunLevelVariablesStreamParams]) -> BinaryIO: ...
    @overload
    async def level_variables(self, **params: Unpack[SpeedrunLevelVariablesTextResponseParams]) -> str: ...
    @overload
    async def level_variables(self, **params: Unpack[SpeedrunLevelVariablesDefaultParams]) -> SpeedrunLevelVariablesResponse: ...
    @overload
    async def resource_options(self, **params: Unpack[SpeedrunResourceOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def resource_options(self, **params: Unpack[SpeedrunResourceOptionsTextResponseParams]) -> str: ...
    @overload
    async def resource_options(self, **params: Unpack[SpeedrunResourceOptionsDefaultParams]) -> SpeedrunResourceOptionsResponse: ...
    @overload
    async def runs(self, **params: Unpack[SpeedrunRunsStreamParams]) -> BinaryIO: ...
    @overload
    async def runs(self, **params: Unpack[SpeedrunRunsTextResponseParams]) -> str: ...
    @overload
    async def runs(self, **params: Unpack[SpeedrunRunsDefaultParams]) -> SpeedrunRunsResponse: ...
    @overload
    async def runs_options(self, **params: Unpack[SpeedrunRunsOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def runs_options(self, **params: Unpack[SpeedrunRunsOptionsTextResponseParams]) -> str: ...
    @overload
    async def runs_options(self, **params: Unpack[SpeedrunRunsOptionsDefaultParams]) -> SpeedrunRunsOptionsResponse: ...
    @overload
    async def run(self, **params: Unpack[SpeedrunRunStreamParams]) -> BinaryIO: ...
    @overload
    async def run(self, **params: Unpack[SpeedrunRunTextResponseParams]) -> str: ...
    @overload
    async def run(self, **params: Unpack[SpeedrunRunDefaultParams]) -> SpeedrunRunResponse: ...

class _AsyncSpeedrunGroup:
    @overload
    async def catalog(self, **params: Unpack[SpeedrunCatalogStreamParams]) -> BinaryIO: ...
    @overload
    async def catalog(self, **params: Unpack[SpeedrunCatalogTextResponseParams]) -> str: ...
    @overload
    async def catalog(self, **params: Unpack[SpeedrunCatalogDefaultParams]) -> SpeedrunCatalogResponse: ...
    @overload
    async def category_detail(self, **params: Unpack[SpeedrunCategoryDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def category_detail(self, **params: Unpack[SpeedrunCategoryDetailTextResponseParams]) -> str: ...
    @overload
    async def category_detail(self, **params: Unpack[SpeedrunCategoryDetailDefaultParams]) -> SpeedrunCategoryDetailResponse: ...
    @overload
    async def category_records(self, **params: Unpack[SpeedrunCategoryRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def category_records(self, **params: Unpack[SpeedrunCategoryRecordsTextResponseParams]) -> str: ...
    @overload
    async def category_records(self, **params: Unpack[SpeedrunCategoryRecordsDefaultParams]) -> SpeedrunCategoryRecordsResponse: ...
    @overload
    async def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesStreamParams]) -> BinaryIO: ...
    @overload
    async def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesTextResponseParams]) -> str: ...
    @overload
    async def category_variables(self, **params: Unpack[SpeedrunCategoryVariablesDefaultParams]) -> SpeedrunCategoryVariablesResponse: ...
    @overload
    async def games(self, **params: Unpack[SpeedrunGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[SpeedrunGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[SpeedrunGamesDefaultParams]) -> SpeedrunGamesResponse: ...
    @overload
    async def game_detail(self, **params: Unpack[SpeedrunGameDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def game_detail(self, **params: Unpack[SpeedrunGameDetailTextResponseParams]) -> str: ...
    @overload
    async def game_detail(self, **params: Unpack[SpeedrunGameDetailDefaultParams]) -> SpeedrunGameDetailResponse: ...
    @overload
    async def categories(self, **params: Unpack[SpeedrunCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[SpeedrunCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[SpeedrunCategoriesDefaultParams]) -> SpeedrunCategoriesResponse: ...
    @overload
    async def levels(self, **params: Unpack[SpeedrunLevelsStreamParams]) -> BinaryIO: ...
    @overload
    async def levels(self, **params: Unpack[SpeedrunLevelsTextResponseParams]) -> str: ...
    @overload
    async def levels(self, **params: Unpack[SpeedrunLevelsDefaultParams]) -> SpeedrunLevelsResponse: ...
    @overload
    async def records(self, **params: Unpack[SpeedrunRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def records(self, **params: Unpack[SpeedrunRecordsTextResponseParams]) -> str: ...
    @overload
    async def records(self, **params: Unpack[SpeedrunRecordsDefaultParams]) -> SpeedrunRecordsResponse: ...
    @overload
    async def variables(self, **params: Unpack[SpeedrunVariablesStreamParams]) -> BinaryIO: ...
    @overload
    async def variables(self, **params: Unpack[SpeedrunVariablesTextResponseParams]) -> str: ...
    @overload
    async def variables(self, **params: Unpack[SpeedrunVariablesDefaultParams]) -> SpeedrunVariablesResponse: ...
    @overload
    async def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def game_leaderboard(self, **params: Unpack[SpeedrunGameLeaderboardDefaultParams]) -> SpeedrunGameLeaderboardResponse: ...
    @overload
    async def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def level_leaderboard(self, **params: Unpack[SpeedrunLevelLeaderboardDefaultParams]) -> SpeedrunLevelLeaderboardResponse: ...
    @overload
    async def level_detail(self, **params: Unpack[SpeedrunLevelDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def level_detail(self, **params: Unpack[SpeedrunLevelDetailTextResponseParams]) -> str: ...
    @overload
    async def level_detail(self, **params: Unpack[SpeedrunLevelDetailDefaultParams]) -> SpeedrunLevelDetailResponse: ...
    @overload
    async def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesTextResponseParams]) -> str: ...
    @overload
    async def level_categories(self, **params: Unpack[SpeedrunLevelCategoriesDefaultParams]) -> SpeedrunLevelCategoriesResponse: ...
    @overload
    async def level_records(self, **params: Unpack[SpeedrunLevelRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def level_records(self, **params: Unpack[SpeedrunLevelRecordsTextResponseParams]) -> str: ...
    @overload
    async def level_records(self, **params: Unpack[SpeedrunLevelRecordsDefaultParams]) -> SpeedrunLevelRecordsResponse: ...
    @overload
    async def level_variables(self, **params: Unpack[SpeedrunLevelVariablesStreamParams]) -> BinaryIO: ...
    @overload
    async def level_variables(self, **params: Unpack[SpeedrunLevelVariablesTextResponseParams]) -> str: ...
    @overload
    async def level_variables(self, **params: Unpack[SpeedrunLevelVariablesDefaultParams]) -> SpeedrunLevelVariablesResponse: ...
    @overload
    async def resource_options(self, **params: Unpack[SpeedrunResourceOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def resource_options(self, **params: Unpack[SpeedrunResourceOptionsTextResponseParams]) -> str: ...
    @overload
    async def resource_options(self, **params: Unpack[SpeedrunResourceOptionsDefaultParams]) -> SpeedrunResourceOptionsResponse: ...
    @overload
    async def runs(self, **params: Unpack[SpeedrunRunsStreamParams]) -> BinaryIO: ...
    @overload
    async def runs(self, **params: Unpack[SpeedrunRunsTextResponseParams]) -> str: ...
    @overload
    async def runs(self, **params: Unpack[SpeedrunRunsDefaultParams]) -> SpeedrunRunsResponse: ...
    @overload
    async def runs_options(self, **params: Unpack[SpeedrunRunsOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def runs_options(self, **params: Unpack[SpeedrunRunsOptionsTextResponseParams]) -> str: ...
    @overload
    async def runs_options(self, **params: Unpack[SpeedrunRunsOptionsDefaultParams]) -> SpeedrunRunsOptionsResponse: ...
    @overload
    async def run(self, **params: Unpack[SpeedrunRunStreamParams]) -> BinaryIO: ...
    @overload
    async def run(self, **params: Unpack[SpeedrunRunTextResponseParams]) -> str: ...
    @overload
    async def run(self, **params: Unpack[SpeedrunRunDefaultParams]) -> SpeedrunRunResponse: ...

SpeedrunCatalogDefaultParams = TypedDict('SpeedrunCatalogDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'kind': Required[Literal['platforms', 'regions', 'gametypes', 'developers', 'publishers', 'genres', 'engines']],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunCatalogTextResponseParams = TypedDict('SpeedrunCatalogTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'kind': Required[Literal['platforms', 'regions', 'gametypes', 'developers', 'publishers', 'genres', 'engines']],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunCatalogStreamParams = TypedDict('SpeedrunCatalogStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'kind': Required[Literal['platforms', 'regions', 'gametypes', 'developers', 'publishers', 'genres', 'engines']],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunCategoryDetailDefaultParams = TypedDict('SpeedrunCategoryDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'variables']]],
}, total=False)

SpeedrunCategoryDetailTextResponseParams = TypedDict('SpeedrunCategoryDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'variables']]],
}, total=False)

SpeedrunCategoryDetailStreamParams = TypedDict('SpeedrunCategoryDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'variables']]],
}, total=False)

SpeedrunCategoryRecordsDefaultParams = TypedDict('SpeedrunCategoryRecordsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunCategoryRecordsTextResponseParams = TypedDict('SpeedrunCategoryRecordsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunCategoryRecordsStreamParams = TypedDict('SpeedrunCategoryRecordsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunCategoryVariablesDefaultParams = TypedDict('SpeedrunCategoryVariablesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game']]],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
}, total=False)

SpeedrunCategoryVariablesTextResponseParams = TypedDict('SpeedrunCategoryVariablesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game']]],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
}, total=False)

SpeedrunCategoryVariablesStreamParams = TypedDict('SpeedrunCategoryVariablesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game']]],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
}, total=False)

SpeedrunGamesDefaultParams = TypedDict('SpeedrunGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'name': NotRequired[str],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'gametype': NotRequired[str],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'abbreviation': NotRequired[str],
    'released': NotRequired[int],
    'genre': NotRequired[str],
    'engine': NotRequired[str],
    'developer': NotRequired[str],
    'publisher': NotRequired[str],
    'orderby': NotRequired[Literal['name.int', 'name.jap', 'abbreviation', 'released', 'created', 'similarity']],
    'direction': NotRequired[Literal['asc', 'desc']],
    '_bulk': NotRequired[bool],
    'romhack': NotRequired[bool],
    'embed': NotRequired[list[Literal['categories', 'levels', 'variables', 'platforms', 'regions', 'gametypes', 'genres', 'engines', 'developers', 'publishers']]],
}, total=False)

SpeedrunGamesTextResponseParams = TypedDict('SpeedrunGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'name': NotRequired[str],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'gametype': NotRequired[str],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'abbreviation': NotRequired[str],
    'released': NotRequired[int],
    'genre': NotRequired[str],
    'engine': NotRequired[str],
    'developer': NotRequired[str],
    'publisher': NotRequired[str],
    'orderby': NotRequired[Literal['name.int', 'name.jap', 'abbreviation', 'released', 'created', 'similarity']],
    'direction': NotRequired[Literal['asc', 'desc']],
    '_bulk': NotRequired[bool],
    'romhack': NotRequired[bool],
    'embed': NotRequired[list[Literal['categories', 'levels', 'variables', 'platforms', 'regions', 'gametypes', 'genres', 'engines', 'developers', 'publishers']]],
}, total=False)

SpeedrunGamesStreamParams = TypedDict('SpeedrunGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'name': NotRequired[str],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'gametype': NotRequired[str],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'abbreviation': NotRequired[str],
    'released': NotRequired[int],
    'genre': NotRequired[str],
    'engine': NotRequired[str],
    'developer': NotRequired[str],
    'publisher': NotRequired[str],
    'orderby': NotRequired[Literal['name.int', 'name.jap', 'abbreviation', 'released', 'created', 'similarity']],
    'direction': NotRequired[Literal['asc', 'desc']],
    '_bulk': NotRequired[bool],
    'romhack': NotRequired[bool],
    'embed': NotRequired[list[Literal['categories', 'levels', 'variables', 'platforms', 'regions', 'gametypes', 'genres', 'engines', 'developers', 'publishers']]],
}, total=False)

SpeedrunGameDetailDefaultParams = TypedDict('SpeedrunGameDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['categories', 'levels', 'variables', 'platforms', 'regions', 'gametypes', 'genres', 'engines', 'developers', 'publishers']]],
}, total=False)

SpeedrunGameDetailTextResponseParams = TypedDict('SpeedrunGameDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['categories', 'levels', 'variables', 'platforms', 'regions', 'gametypes', 'genres', 'engines', 'developers', 'publishers']]],
}, total=False)

SpeedrunGameDetailStreamParams = TypedDict('SpeedrunGameDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['categories', 'levels', 'variables', 'platforms', 'regions', 'gametypes', 'genres', 'engines', 'developers', 'publishers']]],
}, total=False)

SpeedrunCategoriesDefaultParams = TypedDict('SpeedrunCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'miscellaneous': NotRequired[bool],
    'orderby': NotRequired[Literal['name', 'miscellaneous', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['game', 'variables']]],
}, total=False)

SpeedrunCategoriesTextResponseParams = TypedDict('SpeedrunCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'miscellaneous': NotRequired[bool],
    'orderby': NotRequired[Literal['name', 'miscellaneous', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['game', 'variables']]],
}, total=False)

SpeedrunCategoriesStreamParams = TypedDict('SpeedrunCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'miscellaneous': NotRequired[bool],
    'orderby': NotRequired[Literal['name', 'miscellaneous', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['game', 'variables']]],
}, total=False)

SpeedrunLevelsDefaultParams = TypedDict('SpeedrunLevelsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'orderby': NotRequired[Literal['name', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['categories', 'variables']]],
}, total=False)

SpeedrunLevelsTextResponseParams = TypedDict('SpeedrunLevelsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'orderby': NotRequired[Literal['name', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['categories', 'variables']]],
}, total=False)

SpeedrunLevelsStreamParams = TypedDict('SpeedrunLevelsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'orderby': NotRequired[Literal['name', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['categories', 'variables']]],
}, total=False)

SpeedrunRecordsDefaultParams = TypedDict('SpeedrunRecordsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
}, total=False)

SpeedrunRecordsTextResponseParams = TypedDict('SpeedrunRecordsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
}, total=False)

SpeedrunRecordsStreamParams = TypedDict('SpeedrunRecordsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
}, total=False)

SpeedrunVariablesDefaultParams = TypedDict('SpeedrunVariablesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['game']]],
}, total=False)

SpeedrunVariablesTextResponseParams = TypedDict('SpeedrunVariablesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['game']]],
}, total=False)

SpeedrunVariablesStreamParams = TypedDict('SpeedrunVariablesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'embed': NotRequired[list[Literal['game']]],
}, total=False)

SpeedrunGameLeaderboardDefaultParams = TypedDict('SpeedrunGameLeaderboardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[str],
    'category': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulators': NotRequired[bool],
    'video_only': NotRequired[bool],
    'timing': NotRequired[Literal['realtime', 'realtime_noloads', 'ingame']],
    'date': NotRequired[str],
    'variables': NotRequired[str],
}, total=False)

SpeedrunGameLeaderboardTextResponseParams = TypedDict('SpeedrunGameLeaderboardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[str],
    'category': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulators': NotRequired[bool],
    'video_only': NotRequired[bool],
    'timing': NotRequired[Literal['realtime', 'realtime_noloads', 'ingame']],
    'date': NotRequired[str],
    'variables': NotRequired[str],
}, total=False)

SpeedrunGameLeaderboardStreamParams = TypedDict('SpeedrunGameLeaderboardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[str],
    'category': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulators': NotRequired[bool],
    'video_only': NotRequired[bool],
    'timing': NotRequired[Literal['realtime', 'realtime_noloads', 'ingame']],
    'date': NotRequired[str],
    'variables': NotRequired[str],
}, total=False)

SpeedrunLevelLeaderboardDefaultParams = TypedDict('SpeedrunLevelLeaderboardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[str],
    'category': Required[str],
    'level': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulators': NotRequired[bool],
    'video_only': NotRequired[bool],
    'timing': NotRequired[Literal['realtime', 'realtime_noloads', 'ingame']],
    'date': NotRequired[str],
    'variables': NotRequired[str],
}, total=False)

SpeedrunLevelLeaderboardTextResponseParams = TypedDict('SpeedrunLevelLeaderboardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[str],
    'category': Required[str],
    'level': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulators': NotRequired[bool],
    'video_only': NotRequired[bool],
    'timing': NotRequired[Literal['realtime', 'realtime_noloads', 'ingame']],
    'date': NotRequired[str],
    'variables': NotRequired[str],
}, total=False)

SpeedrunLevelLeaderboardStreamParams = TypedDict('SpeedrunLevelLeaderboardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[str],
    'category': Required[str],
    'level': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulators': NotRequired[bool],
    'video_only': NotRequired[bool],
    'timing': NotRequired[Literal['realtime', 'realtime_noloads', 'ingame']],
    'date': NotRequired[str],
    'variables': NotRequired[str],
}, total=False)

SpeedrunLevelDetailDefaultParams = TypedDict('SpeedrunLevelDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['categories', 'variables']]],
}, total=False)

SpeedrunLevelDetailTextResponseParams = TypedDict('SpeedrunLevelDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['categories', 'variables']]],
}, total=False)

SpeedrunLevelDetailStreamParams = TypedDict('SpeedrunLevelDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['categories', 'variables']]],
}, total=False)

SpeedrunLevelCategoriesDefaultParams = TypedDict('SpeedrunLevelCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'variables']]],
    'orderby': NotRequired[Literal['name', 'miscellaneous', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'miscellaneous': NotRequired[bool],
}, total=False)

SpeedrunLevelCategoriesTextResponseParams = TypedDict('SpeedrunLevelCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'variables']]],
    'orderby': NotRequired[Literal['name', 'miscellaneous', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'miscellaneous': NotRequired[bool],
}, total=False)

SpeedrunLevelCategoriesStreamParams = TypedDict('SpeedrunLevelCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'variables']]],
    'orderby': NotRequired[Literal['name', 'miscellaneous', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'miscellaneous': NotRequired[bool],
}, total=False)

SpeedrunLevelRecordsDefaultParams = TypedDict('SpeedrunLevelRecordsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunLevelRecordsTextResponseParams = TypedDict('SpeedrunLevelRecordsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunLevelRecordsStreamParams = TypedDict('SpeedrunLevelRecordsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platforms', 'regions', 'variables']]],
    'top': NotRequired[int],
    'skip_empty': NotRequired[bool],
    'max': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SpeedrunLevelVariablesDefaultParams = TypedDict('SpeedrunLevelVariablesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game']]],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
}, total=False)

SpeedrunLevelVariablesTextResponseParams = TypedDict('SpeedrunLevelVariablesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game']]],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
}, total=False)

SpeedrunLevelVariablesStreamParams = TypedDict('SpeedrunLevelVariablesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game']]],
    'orderby': NotRequired[Literal['name', 'mandatory', 'user-defined', 'pos']],
    'direction': NotRequired[Literal['asc', 'desc']],
}, total=False)

SpeedrunResourceOptionsDefaultParams = TypedDict('SpeedrunResourceOptionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

SpeedrunResourceOptionsTextResponseParams = TypedDict('SpeedrunResourceOptionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

SpeedrunResourceOptionsStreamParams = TypedDict('SpeedrunResourceOptionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

SpeedrunRunsDefaultParams = TypedDict('SpeedrunRunsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[str],
    'category': NotRequired[str],
    'level': NotRequired[str],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulated': NotRequired[bool],
    'status': NotRequired[Literal['new', 'verified', 'rejected']],
    'orderby': NotRequired[Literal['game', 'category', 'level', 'platform', 'region', 'emulated', 'date', 'submitted', 'status', 'verify-date']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platform', 'region']]],
}, total=False)

SpeedrunRunsTextResponseParams = TypedDict('SpeedrunRunsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[str],
    'category': NotRequired[str],
    'level': NotRequired[str],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulated': NotRequired[bool],
    'status': NotRequired[Literal['new', 'verified', 'rejected']],
    'orderby': NotRequired[Literal['game', 'category', 'level', 'platform', 'region', 'emulated', 'date', 'submitted', 'status', 'verify-date']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platform', 'region']]],
}, total=False)

SpeedrunRunsStreamParams = TypedDict('SpeedrunRunsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[str],
    'category': NotRequired[str],
    'level': NotRequired[str],
    'platform': NotRequired[str],
    'region': NotRequired[str],
    'emulated': NotRequired[bool],
    'status': NotRequired[Literal['new', 'verified', 'rejected']],
    'orderby': NotRequired[Literal['game', 'category', 'level', 'platform', 'region', 'emulated', 'date', 'submitted', 'status', 'verify-date']],
    'direction': NotRequired[Literal['asc', 'desc']],
    'max': NotRequired[int],
    'offset': NotRequired[int],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platform', 'region']]],
}, total=False)

SpeedrunRunsOptionsDefaultParams = TypedDict('SpeedrunRunsOptionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

SpeedrunRunsOptionsTextResponseParams = TypedDict('SpeedrunRunsOptionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

SpeedrunRunsOptionsStreamParams = TypedDict('SpeedrunRunsOptionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

SpeedrunRunDefaultParams = TypedDict('SpeedrunRunDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platform', 'region']]],
}, total=False)

SpeedrunRunTextResponseParams = TypedDict('SpeedrunRunTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platform', 'region']]],
}, total=False)

SpeedrunRunStreamParams = TypedDict('SpeedrunRunStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'embed': NotRequired[list[Literal['game', 'category', 'level', 'platform', 'region']]],
}, total=False)
