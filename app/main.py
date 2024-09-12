from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from app.core.database import Base, engine
from app.models import models

def get_server():
    server = FastAPI(
        title='markcloud-managed-inventory', 
        docs_url="/docs", redoc_url=None,
        version="1.0.0",
        openapi_url="/openapi.json"
    )
    server.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    server.add_middleware(
        GZipMiddleware, minimum_size=1000
    )

    return server

app = get_server()

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['Root'])
def ping():
    return 200

# app.include_router(user_router.router, tags=['User'])