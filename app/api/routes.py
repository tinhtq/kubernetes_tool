from fastapi import APIRouter

from app.api.telnet import router as TelnetRouter
from app.api.copy_file import router as CopyFileRouter

routers = APIRouter()

router_list = [TelnetRouter, CopyFileRouter]

for router in router_list:
    routers.include_router(router)
