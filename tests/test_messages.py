import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_post_message(client: AsyncClient, test_chat):
    response = await client.post(
        f"/chats/{test_chat.id}/messages", json={"text": "New Test Message"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["text"] == "New Test Message"


@pytest.mark.asyncio
async def test_post_message_invalid_chat(client: AsyncClient):
    response = await client.post(
        "/chats/999/messages", json={"text": "New Test Message"}
    )
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_short_message(client: AsyncClient, test_chat):
    response = await client.post(f"/chats/{test_chat.id}/messages", json={"text": ""})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_long_message(client: AsyncClient, test_chat):
    response = await client.post(
        f"/chats/{test_chat.id}/messages", json={"text": "a" * 5001}
    )
    assert response.status_code == 422
