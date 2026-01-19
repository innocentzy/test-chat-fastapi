from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ChatBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        return v.strip()


class ChatCreate(ChatBase):
    pass


class ChatResponse(ChatBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


class MessageBase(BaseModel):
    chat_id: int
    text: str = Field(..., min_length=1, max_length=5000)


class MessageCreate(MessageBase):
    pass


class MessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    chat_id: int
    text: str
    created_at: datetime


class MessageListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    chat_id: int
    text: str
    created_at: datetime


class ChatWithMessagesResponse(ChatResponse):
    messages = list[MessageListResponse] = []
