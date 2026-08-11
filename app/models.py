from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer

from sqlalchemy.sql import func

from app.database import Base



class User(Base):

    __tablename__ = "users"


    id = Column(
        String,
        primary_key=True
    )


    username = Column(
        String,
        unique=True,
        nullable=False
    )


    nickname = Column(
        String,
        nullable=False
    )


    password = Column(
        String,
        nullable=False
    )


    avatar = Column(
        String,
        default="default.png"
    )


    bio = Column(
        String,
        default=""
    )


    online = Column(
        Boolean,
        default=False
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )



class Message(Base):

    __tablename__ = "messages"


    id = Column(
        String,
        primary_key=True
    )


    sender = Column(
        String
    )


    receiver = Column(
        String
    )


    text = Column(
        String
    )


    attachment = Column(
        String,
        default=None
    )


    is_read = Column(
        Boolean,
        default=False
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )



class Group(Base):

    __tablename__ = "groups"


    id = Column(
        String,
        primary_key=True
    )


    name = Column(
        String
    )


    owner = Column(
        String
    )


    avatar = Column(
        String,
        default="group.png"
    )



class GroupMember(Base):

    __tablename__ = "group_members"


    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


    group_id = Column(
        String
    )


    user_id = Column(
        String
    )


    role = Column(
        String,
        default="member"
    )



class Media(Base):

    __tablename__ = "media"


    id = Column(
        String,
        primary_key=True
    )


    owner = Column(
        String
    )


    filename = Column(
        String
    )


    path = Column(
        String
    )


    type = Column(
        String
    )



class Reaction(Base):

    __tablename__ = "reactions"


    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


    message_id = Column(
        String
    )


    user_id = Column(
        String
    )


    emoji = Column(
        String
    )

class Device(Base):

    __tablename__ = "devices"


    id = Column(
        String,
        primary_key=True
    )


    user_id = Column(
        String,
        nullable=False
    )


    device_name = Column(
        String,
        nullable=False
    )


    device_type = Column(
        String,
        nullable=False
    )


    push_token = Column(
        String,
        default=""
    )


    last_online = Column(
        DateTime,
        server_default=func.now()
    )


    active = Column(
        Boolean,
        default=True
    )

class UserSettings(Base):

    __tablename__ = "user_settings"


    id = Column(
        String,
        primary_key=True
    )


    user_id = Column(
        String
    )


    theme = Column(
        String,
        default="dark"
    )


    language = Column(
        String,
        default="ru"
    )


    notifications = Column(
        Boolean,
        default=True
    )