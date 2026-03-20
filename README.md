

## Goals:

* Show all levels `DEBUG` to `CRITICAL`, *except* for messages from
the  standard library's `asyncio`, which shouldn't include `DEBUG`.
* Prefix all lines with a priority level for journald,
as per [priorityprefix](https://pypi.org/project/priorityprefix/).
* Shut down tidily when sent a `SIGINT`,
even if handling websockets that will never end.

## Findings:

* I have completely failed to get Hypercorn to shut down if there
are websockets open.
The same is true of palfrey.
Whereas uvicorn and daphne are fine, and handles an interrupt with no issue.
* Hmm... daphne's gives warnings if a websocket client disconnects,
complaining that the task took too long to shut down.
I should investigate more generally if my handlers get tidily shut down.
* Gunicorn really, *really* resisted any kind of non-CLI (API) use.
* Gunicorn also threw `RuntimeError`s if a websocket client disconnected.
* Aiohttp needed a third-party adaptor, and everything was very buggy.

