import pprint

import pytest
from httpx import AsyncClient, ASGITransport
from .main import app


@pytest.mark.asyncio
async def test_get_books():
    async with AsyncClient(
            transport=ASGITransport(app),
            base_url="http://127.0.0.1:8000",
    ) as ac:
        response = await ac.get("/books")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 6
        pprint.pprint(data)


@pytest.mark.asyncio
async def test_add_books():
    async with AsyncClient(
            transport=ASGITransport(app),
            base_url="http://127.0.0.1:8000",
    ) as ac:
        response = await ac.post("/books", json={"title": "test", "author": "test"})
        assert response.status_code == 200
        data = response.json()
        assert data == {"message": "Book added successfully"}
