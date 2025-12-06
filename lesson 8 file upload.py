from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse

app = FastAPI()


@app.post("/files/")
async def create_file(uploaded_file: UploadFile):
    file = uploaded_file.file
    filename = uploaded_file.filename
    with open(f"test_{filename}", "wb") as buffer:
        buffer.write(file.read())


@app.post("/multiple-files/")
async def create_file(uploaded_files: list[UploadFile]):
    for uploaded_file in uploaded_files:
        file = uploaded_file.file
        filename = uploaded_file.filename
        with open(f"test_{filename}", "wb") as buffer:
            buffer.write(file.read())


@app.get("/files/{file_path}")
async def get_file(file_path: str):
    return FileResponse(f"test_{file_path}")


def iterfile(file_path: str):
    with open(f"test_{file_path}", "rb") as f:
        while chunk := f.read(1024 * 1024):
            yield chunk


@app.get("/stream-file/{file_path}")
async def get_file(file_path: str):
    return StreamingResponse(iterfile(file_path), media_type="pdf")
