import asyncio


async def print_words():
    print('starting printing words')
    await asyncio.sleep(2)
    print('stopped printing words')
    return 'RETURN FROM PRINT WORDS'


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(print_words())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2

asyncio.run(main())


