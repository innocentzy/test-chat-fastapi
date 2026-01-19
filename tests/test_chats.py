import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_chat_with_messages(client: AsyncClient, test_chat, test_messages):
    response = await client.get(f"/chats/{test_chat.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Chat"
    assert "messages" in data


@pytest.mark.asyncio
async def test_get_chat_with_limit(client: AsyncClient, test_chat, test_messages):
    response = await client.get(f"/chats/{test_chat.id}?limit=1")
    assert response.status_code == 200
    data = response.json()
    assert len(data["messages"]) == 1


@pytest.mark.asyncio
async def test_get_chat_not_found(client: AsyncClient):
    response = await client.get("/chats/999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_create_chat(client: AsyncClient):
    response = await client.post(
        "/chats",
        json={"title": "New Test Chat"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "New Test Chat"


@pytest.mark.asyncio
async def test_long_title_chat(client: AsyncClient):
    response = await client.post(
        "/chats",
        json={"title": "a" * 201},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_short_title_chat(client: AsyncClient):
    response = await client.post(
        "/chats",
        json={"title": ""},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_trim_chat_title(client: AsyncClient):
    response = await client.post(
        "/chats",
        json={"title": "  test  "},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "test"


@pytest.mark.asyncio
async def test_delete_chat(client: AsyncClient, test_chat):
    response = await client.delete(f"/chats/{test_chat.id}")
    assert response.status_code == 204
    response = await client.get(f"/chats/{test_chat.id}")
    assert response.status_code == 404
