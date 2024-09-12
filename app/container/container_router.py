from fastapi import APIRouter, Query, Depends
from app.container.container_service import ContainerService

router = APIRouter(
    prefix="/api/container",
)
container_service = ContainerService()
