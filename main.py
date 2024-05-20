from fastapi import FastAPI
from app.telnet import telnet_session
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/telnet")
async def handle_telnet(host: str, port: int, username: str, password: str, command: str):
    try:
        session = telnet_session(host, port)
        return {"result": "hello"}
    except Exception as e:
        return {"error": str(e)}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
