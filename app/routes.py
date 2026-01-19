from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import get_chat, create_chat, delete_chat, post_message
from app.database import get_db
from app.models import Chat, Message
from app.schemas import (
    ChatCreate,
    ChatResponse,
    MessageResponse,
    ChatWithMessagesResponse,
    MessageCreate,
)

router = APIRouter(prefix="/chats")


@router.get("/{chat_id}", response_model=ChatWithMessagesResponse)
async def get_chat_with_messages(
    chat_id: int, db: AsyncSession = Depends(get_db), limit: int = 20
):
    chat = await get_chat(db, chat_id, limit)
    if not chat:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    return chat


@router.post("", response_model=ChatResponse, status_code=status.HTTP_201_CREATED)
async def add_chat(chat: ChatCreate, db: AsyncSession = Depends(get_db)):
    return await create_chat(db, chat)


@router.post(
    "/{chat_id}/messages",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED,
)
async def add_message(
    message: MessageCreate, chat_id: int, db: AsyncSession = Depends(get_db)
):
    chat = await get_chat(db, chat_id)
    if not chat:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    return await post_message(db, message, chat_id)


@router.delete("/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_chat(chat_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await delete_chat(db, chat_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
