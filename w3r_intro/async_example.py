import asyncio

async def async_sample_task(task_name):
    print(f'{task_name} starting...')
    await asyncio.sleep(2)
    print(f'{task_name} finished.')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(async_sample_task('Task 1')),
        loop.create_task(async_sample_task('Task 2')),
        loop.create_task(async_sample_task('Task 3'))
    ]

    loop.run_until_complete(asyncio.wait(tasks))
