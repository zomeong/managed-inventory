from fastapi import APIRouter, Query, Depends
from app.container.container_service import ContainerService
from app.container.container_schema import ContainerCreate
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter(
    prefix="/api/container",
)

def get_container_service(db: Session = Depends(get_db)):
    return ContainerService(db)

@router.post("")
def create_container(container: ContainerCreate, service: ContainerService = Depends(get_container_service)):
    service.create_container(container)
    return "컨테이너 생성이 완료되었습니다."

