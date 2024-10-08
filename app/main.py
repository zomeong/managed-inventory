from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from app.core.database import Base, engine
from app.models import models
from app.container import container_router
from app.product import product_router
from app.transaction import transaction_router
from app.stock import stock_router

desc = '마크클라우드 사내 재고 관리 시스템'

def get_server():
    server = FastAPI(
        title='markcloud-managed-inventory', 
        docs_url="/docs", redoc_url=None,
        version="1.0.0",
        description=desc,
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

app.include_router(container_router.router, tags=['Container'])
app.include_router(product_router.router, tags=['Product'])
app.include_router(transaction_router.router, tags=['Transaction'])
app.include_router(stock_router.router, tags=['Stock'])