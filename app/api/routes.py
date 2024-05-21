from fastapi import APIRouter

from app.api.telnet import router as TelnetRouter

routers = APIRouter()

router_list = [TelnetRouter]

for router in router_list:
    routers.include_router(router)
