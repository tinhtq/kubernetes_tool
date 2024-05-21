from fastapi import APIRouter
from typing import List

from app.dto.host import HostInfo
from app.services.telnet_service import multi_host_telnet_session

router = APIRouter()


@router.post("/telnet")
async def handle_telnet(host_list: List[HostInfo]):
    try:
        response = await multi_host_telnet_session(host_list)
        return {"failed_connection": response}
    except Exception as e:
        return {"error": str(e)}
