import asyncio
import telnetlib3
from template.host import  Host_Info
from typing import List


async def telnet_session(telnet_host, telnet_port):
    telnet_connection = True
    try:
        await telnetlib3.open_connection(telnet_host, telnet_port)
    except (asyncio.exceptions.TimeoutError, OSError):
        telnet_connection = False
    return telnet_connection



async def multi_host_telnet_session(hosts: List[Host_Info]):
    failed_connection_host = []
    for telnet_host in hosts:
        connection = telnet_session(telnet_host.host, telnet_host.port)
        if not connection:
            failed_connection_host.append({"host": telnet_host.host, "port": telnet_host.port})

