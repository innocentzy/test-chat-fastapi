from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload


from app.models import Chat, Message
from app.schemas import ChatCreate, MessageCreate


async def get_chat(db: AsyncSession, chat_id: int, limit: int = 20) -> Chat | None:
    result = await db.execute(
        select(Chat)
        .options(joinedload(Chat.message))
        .where(Chat.id == chat_id)
        .limit(limit)
    )
    return result.scalar_one_or_none()


async def create_chat(db: AsyncSession, chat: ChatCreate) -> Chat:
    db_chat = Chat(**chat.model_dump())
    db.add(db_chat)
    await db.flush()
    await db.refresh(db_chat)
    return db_chat


async def post_message(
    db: AsyncSession, message: MessageCreate, chat_id: int
) -> Message:
    db_message = Message(**message.model_dump(), chat_id=chat_id)
    db.add(db_message)
    await db.flush()
    await db.refresh(db_message)
    return db_message


async def delete_chat(db: AsyncSession, chat_id: int) -> bool:
    db_chat = await get_chat(db, chat_id)
    if not db_chat:
        return False
    await db.delete(db_chat)
    await db.flush()
    return True
