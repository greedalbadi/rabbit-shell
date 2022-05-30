import pickle
import socket
from rabbit_shell.controller import client_side, server_side
from rabbit_shell.data import data, about
from rabbit_shell.background import backstuff
from rabbit_shell.data.banners import banner

filetrans = server_side.filetrans()
client_side = client_side.client_side()
server_side = server_side.server_side()

class Auther:

    def __init__(self, host: str, port: int, key: str):

        self.key = key

        self.port = port
        self.host = host

        self.index = None

        self.server = client_side.formate_socket()

        self.filetrans_server = client_side.formate_socket()

        self.input_mode = data.INPUT_MODE


    def connect(self, key, host, port):


        client_side.connect(self.server, host, port)

        key = f"root:{key}"

        self.server.send(key.encode(data.CODE_FORMATE))

    def connect_tofiletrans(self, host, port):
        """
        host arg and port from main fun

        """
        to = (host, port)
        return client_side.connect(self.filetrans_server, host, port)


    def send(self, server, index, dt):

        ls = [index, dt]

        dt = pickle.dumps(ls)

        return server.send(dt)

    def response(self, server):
        while True:
            resp = server.recv(data.BUFFER_SIZE)

            return pickle.loads(resp)

    def filetrans_recv(self):

        try:

            res = self.filetrans_server.recv(data.BUFFER_SIZE)
            client_side.filetrans_recv(response=res)
            """
            when file is received it goes to
            the process of building it

            """
        except:
            """

            :except if there was exception it'll just continue \ new round of the loop
            mostly of server timeout

            """
    def runtime(self):
        """

        connect to main server
        connect to filetrans server

        """
        self.connect(self.key, self.host, self.port)

        self.connect_tofiletrans(self.host, self.port - data.FILETRANS_PORT)

        while True:


            command = input(self.input_mode)




            if command[:len(data.SET_CLIENT)] == data.SET_CLIENT:
                self.index = int(command.split()[1])



            else:
                if len(command) != 0:

                    self.send(self.server, self.index, command)

                    if command == data.LIST_CLIENTS:
                        _ , table = self.response(self.server)
                        print(table)

                    elif command == "key":
                        print(self.key)


                    elif command[:8] == data.FILE_REQUEST:



                        self.send(self.server, self.index, command)
                        _, byte = self.response(self.server)

                        with open(command[8:], "wb") as file:
                            file.write(byte)
                            file.flush()
                            file.close()
                        print(f"received: {command[8:]}")




                    elif command[:len(data.SEND_FILE)] == data.SEND_FILE:

                        with open(command[len(data.SEND_FILE):], "rb") as file:

                            byte = file.read()
                            file.close()
                        ls = [command[len(data.SEND_FILE):], byte]
                        dt = pickle.dumps(ls)
                        self.filetrans_server.send(dt)
                        print(f"sent {command[len(data.SEND_FILE):]}")


                    elif command == data.BANNER_CLEAR:
                        backstuff.clear()
                        BANNER = banner.main_banner()
                        print(BANNER)


                    elif command in data.CLEAR:
                        backstuff.clear()


                    elif command == data.SERVERINFO:
                        dt = backstuff.server_info()
                        print(dt)


                    else:
                        input_mode, resp = self.response(self.server)
                        if len(input_mode) > 2:
                            self.input_mode = input_mode
                        if len(resp) != 0:
                            print(resp)



