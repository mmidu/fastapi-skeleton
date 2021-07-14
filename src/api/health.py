from fastapi import APIRouter
from utils.settings import settings
from pydantic import BaseModel

router = APIRouter()

class Status(BaseModel):
    serviceID: str = settings.service_id
    status: str = 'pass'
    version: str = settings.version
    releaseID: str = settings.release_id
    environment: str = settings.environment

@router.get('/', response_model=Status)
async def healthcheck():
    content = Status()
        
    logstring = 'HEALTH:'.ljust(10)
    logstring += str(content)
    print(logstring)
    return content