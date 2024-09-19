from app.container.container_repository import ContainerRepository
from app.container.container_schema import ContainerCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

class ContainerService:
    def __init__(self, db: Session):
        self.repository = ContainerRepository(db)

    def create_container(self, createReq: ContainerCreate):
        self.check_name(createReq.name)
        self.repository.create(createReq)

    def get_container(self, id: int):
        container = self.find_container(id)
        return container

    def get_all_containers(self):
        return self.repository.get_all()
    
    def search_container(self, name:str):
        containers = self.repository.search_by_name(name)

        if not containers:
            raise HTTPException(status_code=404, detail="검색 결과가 존재하지 않습니다")
        return containers

    def update_container(self, id:int, updateReq: ContainerCreate):
        container = self.find_container(id)
        self.check_name(updateReq.name)
        self.repository.update(container, updateReq)

    def find_container(self, id):
        container = self.repository.find_by_id(id)
        if not container:
            raise HTTPException(status_code=404, detail="컨테이너를 찾을 수 없습니다")
        return container
    
    def check_name(self, name):
        container = self.repository.find_by_name(name)
        if container:
            raise HTTPException(status_code=400, detail="이미 존재하는 창고 이름입니다.")
