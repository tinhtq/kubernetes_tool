from fastapi import FastAPI
from app.telnet import multi_host_telnet_session
from app.template.host import Host_Info
from typing import List, Dict

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/telnet")
async def handle_telnet(host_list: List[Host_Info]):
    try:
        response = await multi_host_telnet_session(host_list)
        return response
    except Exception as e:
        return {"error": str(e)}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
