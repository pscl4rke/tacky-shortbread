

import logging
LOG = logging.getLogger("app")

import asyncio
import time


async def application(scope, receive, send):
    LOG.debug("I am a debug message")
    LOG.info("I am an info message")
    LOG.warning("I am a warning message")
    LOG.error("I am an error message")
    LOG.critical("I am a critical message")
    event = await receive()
    print(event)
    if event["type"] == "lifespan.startup":
        await send({
            "type": "lifespan.startup.complete",
        })
    elif event["type"] == "lifespan.shutdown":
        await send({
            "type": "lifespan.shutdown.complete",
        })
    elif event["type"] == "http.request":
        await send({
            "type": "http.response.start",
            "status": 200,
            #"headers": [],  # technically optional, except for granian
        })
        await send({
            "type": "http.response.body",
            "body": b"Hello World",
        })
    elif event["type"] == "websocket.connect":
        await send({
            "type": "websocket.accept",
        })
        while True:
            await asyncio.sleep(1)
            await send({
                "type": "websocket.send",
                "text": "Hello as of %i" % time.time(),
            })
    else:
        raise Exception("Unknown %r" % event)
