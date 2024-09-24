from fastapi import APIRouter, Depends, HTTPException
from app.container.container_service import ContainerService
from app.container.container_schema import ContainerCreate, ContainerUpdate, ContainerResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
import logging
import traceback

router = APIRouter(
    prefix="/containers",
)
logging.basicConfig(level=logging.INFO)

def get_container_service(db: Session = Depends(get_db)):
    return ContainerService(db)

@router.post("")
def create_container(container: ContainerCreate, service: ContainerService = Depends(get_container_service)):
    try:
        service.create_container(container)
        return "컨테이너 생성이 완료되었습니다."
    
    # 발생한 HTTPException 클라이언트에 전달
    except HTTPException as he:
        raise he    

    # 스택 트레이스를 로깅
    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")     # 클라이언트에게는 정보를 숨김

@router.get("/{container_id}", response_model=ContainerResponse)
def get_container(container_id: int, service: ContainerService = Depends(get_container_service)):
    try: 
        return service.get_container(container_id)
    
    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")

@router.get("", response_model=list[ContainerResponse])
def get_all_containers(service: ContainerService = Depends(get_container_service)):
    try:
        return service.get_all_containers()
    
    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")

@router.get("/{container_name}/search", response_model=list[ContainerResponse])
def search_containers(container_name: str, service: ContainerService = Depends(get_container_service)):
    try:
        return service.search_containers(container_name)
    
    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")

@router.post("/{container_id}/update")
def update_container(container_id: int, container: ContainerUpdate,
                    service: ContainerService = Depends(get_container_service)):
    try:
        service.update_container(container_id, container)
        return "컨테이너 정보 수정이 완료되었습니다."
    
    except HTTPException as he:
        raise he    

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")