import os

from crawlora_speedrun import SpeedrunClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with SpeedrunClient(api_key=api_key) as client:
    games = client.games(name='Super Mario 64', max=5)
    print('games', games)
    resource_options = client.resource_options()
    print('resource_options', resource_options)
