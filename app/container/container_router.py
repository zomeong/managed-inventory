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

@router.post("",
    description="""
    창고 생성 API

    Input
    - name: 창고 이름
    - location: 창고 위치
    """)
@exception_handler
def create_container(container: ContainerCreate, service: ContainerService = Depends(get_container_service)):
    service.create_container(container)
    return "컨테이너 생성이 완료되었습니다."

@router.get("/{container_name}", response_model=ContainerResponse,
            description="창고 조회 API")
@exception_handler
def get_container(container_name: str, service: ContainerService = Depends(get_container_service)):
    return service.get_container(container_name)

@router.get("", response_model=list[ContainerResponse],
            description="창고 전체 조회 API")
@exception_handler
def get_all_containers(service: ContainerService = Depends(get_container_service)):
    return service.get_all_containers()

@router.post("/{container_name}/update",
    description="""
    창고 정보 수정 API<br>
    * name / location 중 하나만 입력하여 수정 가능

    Parameter
    - container_name: 창고 이름

    Input
    - name: 창고 이름
    - location: 창고 위치
    """)
@exception_handler
def update_container(container_name: int, container: ContainerUpdate,
                    service: ContainerService = Depends(get_container_service)):
    service.update_container(container_name, container)
    return "컨테이너 정보 수정이 완료되었습니다."
    
# @router.get("/{container_name}/search", response_model=list[ContainerResponse])
# @exception_handler
# def search_containers(container_name: str, service: ContainerService = Depends(get_container_service)):
#     return service.search_containers(container_name)
