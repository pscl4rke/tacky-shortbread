

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
Whereas uvicorn is fine, and handles an interrupt with no issue.

