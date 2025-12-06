from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/users")
async def users():
    return {"users": [
        {
            "id": 1,
            "name": "test"
        }
    ]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
