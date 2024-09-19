from pydantic import BaseModel

class ContainerResponse(BaseModel):
    name : str
    location : str

class ContainerCreate(BaseModel):
    name : str
    location : str