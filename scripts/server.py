import socket
import asyncio

global loop

"""
    Handle request over a single connection. It simply echoes back what it receives
"""
async def handle(c_socket):
    while True:
        data = await loop.sock_recv(c_socket, 1024)
        print(data.decode("ascii"))


"""
    Start server that can handle multiple concurrent connections
"""
async def start():
    host = '127.0.0.1'
    port = 8080

    # Server side socket jazz -> create, bind, listen and accept followed by receive and send
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((host, port))
    s_socket.listen(20)
    s_socket.setblocking(False)

    while True:
        c_socket, _ = await loop.sock_accept(s_socket)
        loop.create_task(handle(c_socket))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start())
    loop.close()
