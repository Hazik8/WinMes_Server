from pydantic import BaseModel


class RegisterRequest(BaseModel):

    username: str
    nickname: str
    password: str


class LoginRequest(BaseModel):

    id: str
    password: str


class MessageRequest(BaseModel):

    receiver: str
    text: str


class UserResponse(BaseModel):

    id: str
    username: str
    nickname: str
    avatar: str
    bio: str