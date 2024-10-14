from app.container.container_repository import ContainerRepository
from app.container.container_schema import ContainerCreate, ContainerUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException

class ContainerService:
    def __init__(self, db: Session):
        self.repository = ContainerRepository(db)

    def create_container(self, request: ContainerCreate):
        self.check_name(request.name)
        self.repository.create(request)

    def get_container(self, name: str):
        container = self.find_container_by_name(name)
        return container

    def get_all_containers(self):
        return self.repository.get_all()
    
    def search_containers(self, name:str):
        return self.repository.search_by_name(name)

    def update_container(self, name: str, request: ContainerUpdate):
        container = self.find_container_by_name(name)
        self.check_name(request.name)
        self.repository.update(container, request)
    
    def find_container_by_name(self, name: str):
        container = self.repository.find_by_name(name)
        if container is None:
            raise HTTPException(status_code=404, detail="창고를 찾을 수 없습니다.")
        return container
    
    def check_name(self, name: str):
        container = self.repository.find_by_name(name)
        if container:
            raise HTTPException(status_code=400, detail="이미 존재하는 창고 이름입니다.")
