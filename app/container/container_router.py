from fastapi import APIRouter, Query, Depends
from app.container.container_service import ContainerService
from app.container.container_schema import ContainerCreate, ContainerResponse
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter(
    prefix="/containers",
)

def get_container_service(db: Session = Depends(get_db)):
    return ContainerService(db)

@router.post("")
def create_container(container: ContainerCreate, service: ContainerService = Depends(get_container_service)):
    service.create_container(container)
    return "컨테이너 생성이 완료되었습니다."

@router.get("/{container_id}", response_model=ContainerResponse)
def get_container(container_id: str, service: ContainerService = Depends(get_container_service)):
    return service.get_container(container_id)

@router.get("", response_model=list[ContainerResponse])
def get_all_container(service: ContainerService = Depends(get_container_service)):
    return service.get_all_containers()

@router.get("/{container_name}/search", response_model=list[ContainerResponse])
def search_container(container_name: str, service: ContainerService = Depends(get_container_service)):
    return service.search_container(container_name)

@router.post("/{container_id}/update")
def update_container(container_id: str, container: ContainerCreate,
                    service: ContainerService = Depends(get_container_service)):
    service.update_container(container_id, container)
    return "컨테이너 정보 수정이 완료되었습니다."