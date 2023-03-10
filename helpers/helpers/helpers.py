from asyncio import get_running_loop, Future, Task


class JustinsPythonHelpers:
    __init__ = lambda self, message: None


@staticmethod
async def asyncFromValue(value) -> Future:
    loop = get_running_loop()
    fut = loop.create_future()
    fut.set_result(value)
    return fut
