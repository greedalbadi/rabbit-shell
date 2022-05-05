"""
MIT License

Copyright (c) 2022 greed albadi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import datetime
import sys
import threading

sys.path.insert(0, '..')
from src.controller import server_side
from src.data import data
from src.data.banners import banner
from src.data import basic,  about
from src.background import backstuff
filetrans = server_side.filetrans()
server_side = server_side.server_side()
class server:

    def __init__(self, host: str, port: int):
        """

        called when class is requested
        :param host: server address
        :param port: server port

        """
        self.clients = []
        self.filetrans_clients = []
        self.joined_date = []
        self.addresses = []
        self.current_client = None
        self.server = server_side.create_socket(host, port)
        self.filetrans_server = filetrans.create_filetrans_socket(str(host), int(int(port) - int(data.FILETRANS_PORT)))
        self.port = port
        self.input_mode = data.INPUT_MODE
        self.host = host
        """
        
        self{
        
            :var clients: main server clients list
            :var filetrans_clients: filetrans server clients list
            :var addresses: main server client list
            :var current_client: current seted client
            :var server: main server
            :var filetrans_server: file transfer server
            :var port: server port
            :var input_mode: input title input("title")
            :var host: server address
            
        }
        """


    def accept_clients(self):

        while True:

            """

            loop - wait for clients to accept them to main server
            :return None
            """
            try:

                """
                
                :var client: server client
                :var address: ip address
                
                appends client to clients list
                and address to adresses list
                
                """

                client, address = self.server.accept()
                print(f"Client connected: {address}")
                self.clients.append(client)
                self.addresses.append(address)
                self.joined_date.append(str(datetime.datetime.now()))
            except:
                pass

    def accept_filetrans(self):

        while True:
            """

            loop - wait for clients to accept them to filetrans server
            :return None
            """
            try:
                """

                :var client: server client
                :var address: ip address

                start listening to client

                """
                client, address = self.filetrans_server.accept()
                self.filetrans_clients.append(client)
                threading.Thread(target=filetrans.recvfile, args=[client]).start()
            except:
                pass


    def clients_list(self):
        """
        list online and offline clients

        :return: table
        """
        return server_side.checkon_clients(self.clients, self.addresses, self.joined_date)


    def sendcommand(self, data: str):
        """

        :param data: data - command
        :return: sends the data to the current client

        """
        return server_side.sendcommand(self.current_client, data)

    def response(self):
        """
        :var self.input_mode: is the current path of the client
        :var res: clients response
        :return: response
        """
        self.input_mode, res = server_side.response(self.current_client)
        return res
    def default_input(self, default=data.INPUT_MODE):
        """

        :param default: default input mode
        :return: return to default input
        """
        self.input_mode = default
    def main(self):
        """
        starts with accepting clients
        :return: None
        """
        threading.Thread(target=self.accept_clients).start()
        threading.Thread(target=self.accept_filetrans).start()
        while True:
            try:
                '''
                :ivar command: input command
                
                proces the command and check if it's for
                server side or client
                '''
                command = input(self.input_mode)

                if len(command) == 0:
                    continue
                """
                
                about if elif
                
                -   list online and offline clients
                -   set client
                -   quit current client
                -   send file
                -   clear console
                -   server info            
                    else:
                -   send data to current client
                """
                if command == data.LIST_CLIENTS:
                    self.server.settimeout(int(data.TIMEOUT))

                    print(self.clients_list())

                elif command[:len(data.SET_CLIENT)] == data.SET_CLIENT:

                    try:

                        self.current_client = self.clients[int(command.split()[1])]
                        self.input_mode = server_side.recvpath(self.current_client)
                    except:
                        pass

                elif command == data.QUIT:
                    self.current_client = None
                    self.default_input()

                elif command[:len(data.SEND_FILE)] == data.SEND_FILE:
                    index = self.clients.index(self.current_client)
                    client = self.filetrans_clients[int(index)]
                    filetrans.sendfile(client, command[len(data.SEND_FILE):])

                elif command in data.CLEAR:
                    backstuff.clear()

                elif command == data.BANNER_CLEAR:
                        backstuff.clear()
                        BANNER = banner.main_banner(self.host, self.port, about.__version__, about.__name__)
                        print(BANNER)
                elif command == data.SERVERINFO:
                    dic = {
                        "name": about.__name__,
                        "version": about.__version__,
                        "host": self.host,
                        "port": self.port
                    }
                    print(dic)

                else:
                    if self.current_client != None:
                        self.sendcommand(command)
                        try:
                            res = self.response()
                            if len(res) != 0:
                                print(res, end="")
                        except:
                            pass
            except:
                continue

