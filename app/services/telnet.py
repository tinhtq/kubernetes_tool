import asyncio
import telnetlib3

from typing import List
from app.dto.host import HostInfo


async def telnet_session(telnet_host, telnet_port):
    telnet_connection = True
    try:
        await asyncio.wait_for(telnetlib3.open_connection(telnet_host, telnet_port), 5)
    except (asyncio.exceptions.TimeoutError, OSError) as e:
        telnet_connection = False
        print(e)
    return telnet_connection


async def multi_host_telnet_session(hosts: List[HostInfo]):
    failed_connection_host = []
    for telnet_host in hosts:
        connection = await telnet_session(telnet_host["host"], telnet_host["port"])
        if not connection:
            failed_connection_host.append({"host": telnet_host["host"], "port": telnet_host["port"]})
    return failed_connection_host
