import logging
import traceback
from fastapi import HTTPException
from functools import wraps

# 공통 예외 처리 데코레이터
def exception_handler(func):
    @wraps(func)  # wraps로 원래 함수의 메타데이터를 유지
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        
        # 발생한 HTTPException 클라이언트에 전달
        except HTTPException as he:
            raise he
        
        # 스택 트레이스를 로깅
        except Exception as e:
            logging.error(f"Unhandled exception: {str(e)}")
            logging.error(traceback.format_exc())
            raise HTTPException(status_code=500, detail="서버 내부 오류가 발생하였습니다.")     # 클라이언트에게는 정보를 숨김
    
    return wrapper