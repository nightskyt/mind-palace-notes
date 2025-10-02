from contextlib import asynccontextmanager

import uvicorn
from auth.routes import router as auth_router
from core.database import create_db_and_tables
from fastapi import FastAPI
import fastapi_cdn_host


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
fastapi_cdn_host.patch_docs(app)
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
