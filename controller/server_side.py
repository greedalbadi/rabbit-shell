import socket
import pickle
import prettytable
import sys
sys.path.insert(0, '..')

from data import data




class server_side:



    def create_socket(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, int(port)))
        server.listen()
        return server
    def response(self, client):
        res = client.recv(data.BUFFER_SIZE)
        return pickle.loads(res)


    def encode_data(self, data, formate: str=data.CODE_FORMATE):

        return data.encode(formate)


    def checkon_clients(self, clients, addresses):
        table = prettytable.PrettyTable()
        table.field_names = [data.USENUM, data.IP_ADDRESS, data.STATUS]


        for client in clients:
            index = clients.index(client)
            address = addresses[int(index)]
            try:
                ping_data = self.encode_data(data.CLIENT_PING_DATA)
                client.send(ping_data)
                status = data.ONLINE_STATUS
            except:
                status = data.OFFLINE_STATUS

            table.add_row([index, address, status])

        return table




    def sendcommand(self, client, data: str):

        encoded_data = self.encode_data(data)

        return client.send(encoded_data)

    def recvpath(self, client):

        self.sendcommand(client, data.PATHPING)
        path, res = self.response(client)
        return path

class filetrans:
    global serverside
    serverside = server_side()


    def create_filetrans_socket(self, host: str, port: int):

        return serverside.create_socket(host, int(port))



    def sendfile(self, client, filename):

        file = open(filename, "rb")
        bytes = file.read(data.BUFFER_SIZE)
        ls = [filename, bytes]
        data = pickle.dumps(ls)
        client.send(data)
        print("file sent.")
        return file.close()


    def recvfile(self, client):

        while True:
            try:

                res = client.recv(data.BUFFER_SIZE)
                filename, data = pickle.loads(res)

                with open(filename, "wb") as file:

                    file.write(data)
                    file.close()
            except:
                continue








