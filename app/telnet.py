import asyncio
import telnetlib3


async def telnet_session(host, port):
    telnet_connection = True
    try:
        await telnetlib3.open_connection(host, port)
    except (asyncio.exceptions.TimeoutError, OSError):
        telnet_connection = False
    return telnet_connection


# message = asyncio.run(telnet_welcome_message("10.0.3.183", 22))
# print(message)

failed_connection = []

with open("server.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        info = line.split(",")
        host = info[0]
        port = int(info[1])
        connection = asyncio.run(telnet_session(host, port))
        if not connection:
            failed_connection.append({"host": host, "port": port})

print(failed_connection)