

import logging
LOG = logging.getLogger("client")

import asyncio

from websockets.asyncio.client import connect


async def watch():
    async with connect("ws://localhost:8000") as websocket:
        while True:
            LOG.info(await websocket.recv())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(watch())
