"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class SpeedrunClient(CrawloraClient):
    """Synchronous Speedrun.com API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-speedrun-python/0.1.0')
        super().__init__(*args, **kwargs)

    def catalog(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-catalog', params, response_type=response_type, timeout=timeout, headers=headers)

    def category_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-category-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def category_records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-category-records', params, response_type=response_type, timeout=timeout, headers=headers)

    def category_variables(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-category-variables', params, response_type=response_type, timeout=timeout, headers=headers)

    def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def game_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-game-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def levels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-levels', params, response_type=response_type, timeout=timeout, headers=headers)

    def records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-records', params, response_type=response_type, timeout=timeout, headers=headers)

    def variables(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-variables', params, response_type=response_type, timeout=timeout, headers=headers)

    def game_leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-game-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)

    def level_leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-level-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)

    def level_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-level-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def level_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-level-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def level_records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-level-records', params, response_type=response_type, timeout=timeout, headers=headers)

    def level_variables(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-level-variables', params, response_type=response_type, timeout=timeout, headers=headers)

    def resource_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-resource-options', params, response_type=response_type, timeout=timeout, headers=headers)

    def runs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-runs', params, response_type=response_type, timeout=timeout, headers=headers)

    def runs_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-runs-options', params, response_type=response_type, timeout=timeout, headers=headers)

    def run(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('speedrun-run', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncSpeedrunClient(AsyncCrawloraClient):
    """Asynchronous Speedrun.com API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-speedrun-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def catalog(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-catalog', params, response_type=response_type, timeout=timeout, headers=headers)

    async def category_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-category-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def category_records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-category-records', params, response_type=response_type, timeout=timeout, headers=headers)

    async def category_variables(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-category-variables', params, response_type=response_type, timeout=timeout, headers=headers)

    async def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def game_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-game-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def levels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-levels', params, response_type=response_type, timeout=timeout, headers=headers)

    async def records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-records', params, response_type=response_type, timeout=timeout, headers=headers)

    async def variables(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-variables', params, response_type=response_type, timeout=timeout, headers=headers)

    async def game_leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-game-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)

    async def level_leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-level-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)

    async def level_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-level-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def level_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-level-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def level_records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-level-records', params, response_type=response_type, timeout=timeout, headers=headers)

    async def level_variables(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-level-variables', params, response_type=response_type, timeout=timeout, headers=headers)

    async def resource_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-resource-options', params, response_type=response_type, timeout=timeout, headers=headers)

    async def runs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-runs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def runs_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-runs-options', params, response_type=response_type, timeout=timeout, headers=headers)

    async def run(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('speedrun-run', params, response_type=response_type, timeout=timeout, headers=headers)
