

import logging
LOG = logging.getLogger("app")


async def application(scope, receive, send):
    LOG.debug("I am a debug message")
    LOG.info("I am an info message")
    LOG.warning("I am a warning message")
    LOG.error("I am an error message")
    LOG.critical("I am a critical message")
    event = await receive()
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
        })
        await send({
            "type": "http.response.body",
            "body": b"Hello World",
        })
    else:
        raise Exception("Unknown %r" % event)
