from pydantic import BaseModel
from typing import Optional

class ContainerBase(BaseModel):
    name : str
    location : str

class ContainerCreate(ContainerBase):
    pass

class ContainerUpdate(ContainerBase):
    name: Optional[str] = None
    location: Optional[str] = None

class ContainerResponse(ContainerBase):
    _id: int