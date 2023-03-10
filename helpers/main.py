import asyncio
from helpers import asyncFromValue


def main():
    async def sayHello():
        print((await asyncFromValue("Hello, world!")).result())

    asyncio.run(sayHello())


if __name__ == "__main__":
    main()
