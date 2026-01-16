from datetime import datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base


class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    message: Mapped[list["Message"]] = relationship(
        back_populates="chat", lazy="selectin", cascade="all, delete"
    )


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    chat: Mapped["Chat"] = relationship(back_populates="message", lazy="joined")
