"""Typed Speedrun.com client for the Crawlora hosted API."""

from .platform import SpeedrunClient, AsyncSpeedrunClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = SpeedrunClient
AsyncClient = AsyncSpeedrunClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Speedrun.com'
PLATFORM = 'speedrun'
CONTRACT_REVISION = 'sha256:4103d70f5315c5a4204de3e136abadb3b08fe8c6a11f9447323a0619f0237be8'

__all__ = [
    "SpeedrunClient", "AsyncSpeedrunClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
