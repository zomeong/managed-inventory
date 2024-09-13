from app.container.container_repository import ContainerRepository
from app.container.container_schema import ContainerCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

class ContainerService:
    def __init__(self, db: Session):
        self.repository = ContainerRepository(db)

    def create_container(self, createReq: ContainerCreate):
        container = self.repository.find_by_name(createReq.name)
        if container:
            raise HTTPException(status_code=400, detail="이미 존재하는 창고 이름입니다.")

        self.repository.create(createReq)

    def get_container(self, id: int):
        container = self.repository.find_by_id(id)
        if container is None:
            raise ValueError("컨테이너를 찾을 수 없습니다")
        return container

    def get_all_containers(self):
        return self.repository.get_all()