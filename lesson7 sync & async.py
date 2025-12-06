from fastapi import FastAPI, BackgroundTasks
import time
import asyncio

app = FastAPI()


def sync_task():
    time.sleep(3)
    print("email sent")


async def async_task():
    await asyncio.sleep(3)
    print("email sent")


@app.get("/")
async def root(background_tasks: BackgroundTasks):
    background_tasks.add_task(sync_task)
    # asyncio.create_task(async_task())
    return {"message": "Hello World"}
