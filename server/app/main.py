from fastapi import FastAPI

from app.database import Base, engine

from app.auth import router as auth_router
from app.chat import router as chat_router
from app.users import router as users_router
from app.groups import router as groups_router
from app.media import router as media_router
from app.notifications import router as notifications_router
from app.devices import router as devices_router
from app.sync import router as sync_router
from app.backup import router as backup_router
from app.sessions import router as sessions_router
from app.settings_sync import router as settings_router


app = FastAPI(
    title="WinMes API",
    version="6.0.0",
    description="WinMes Messenger API"
)


Base.metadata.create_all(bind=engine)


app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(users_router)
app.include_router(groups_router)
app.include_router(media_router)
app.include_router(notifications_router)
app.include_router(devices_router)
app.include_router(sync_router)
app.include_router(backup_router)
app.include_router(sessions_router)
app.include_router(settings_router)


@app.get("/")
def root():

    return {
        "name": "WinMes",
        "version": "6.0.0",
        "status": "online"
    }


@app.get("/health")
def health():

    return {
        "status": "ok"
    }