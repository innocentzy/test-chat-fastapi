from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="API чатов и сообщений")


app.include_router(router)


@app.get("/")
async def root():
    return {"message": "API чатов и сообщений", "docs": "/docs"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
