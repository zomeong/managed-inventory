from fastapi import APIRouter, Depends
from app.container.container_service import ContainerService
from app.container.container_schema import ContainerCreate, ContainerUpdate, ContainerResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exception_handler import exception_handler

router = APIRouter(
    prefix="/containers",
)

def get_container_service(db: Session = Depends(get_db)):
    return ContainerService(db)

@router.post("")
@exception_handler
def create_container(container: ContainerCreate, service: ContainerService = Depends(get_container_service)):
    """
        컨테이너 생성
    """
    service.create_container(container)
    return "컨테이너 생성이 완료되었습니다."

@router.get("/{container_id}", response_model=ContainerResponse)
@exception_handler
def get_container(container_id: int, service: ContainerService = Depends(get_container_service)):
    return service.get_container(container_id)

@router.get("", response_model=list[ContainerResponse])
@exception_handler
def get_all_containers(service: ContainerService = Depends(get_container_service)):
    return service.get_all_containers()
    
@router.get("/{container_name}/search", response_model=list[ContainerResponse])
@exception_handler
def search_containers(container_name: str, service: ContainerService = Depends(get_container_service)):
    return service.search_containers(container_name)

@router.post("/{container_id}/update")
@exception_handler
def update_container(container_id: int, container: ContainerUpdate,
                    service: ContainerService = Depends(get_container_service)):
    service.update_container(container_id, container)
    return "컨테이너 정보 수정이 완료되었습니다."
