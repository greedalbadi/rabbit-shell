import json
import os


BUFFER_SIZE = 6969696
CODE_FORMATE = "UTF-8"


INPUT_MODE = ">: "
FILETRANS_PORT = 1
CAM_FRAME_PORT = 2

ONLINE_STATUS = "ONLINE"
OFFLINE_STATUS = "OFFLINE"


CLIENT_PING_DATA = ""
PATHPING = " "

# TABLE FIELDS

USENUM = "use"
IP_ADDRESS = "ADDRESS"
STATUS = "status"

# SERVER

FILE_REQUEST = "reqfile:"
QUIT = "quit"
CLEAR = ["clear", "cls"]
SERVERINFO = "server"
SEND_FILE = "file"
BANNER_CLEAR = "bclear"
LIST_CLIENTS = "list"
SET_CLIENT = "set"
TIMEOUT = 12

# paths
CLIENT_NAME = "client"
WIN_STARTUP_PATH = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
DEFAULT_ICON = "data\\images\\logoicon.ico"



'''def json_change_value(key, value):
    file = open("data.json", "r")
    data = json.load(file)
    file.close()
    data[0][str(key)] = value
    file = open("data.json", "w")
    json.dump(data, file)
    file.close()
    return True


def json_get_value(key):
    file = open("data\data.json", "r")
    data = json.load(file)
    file.close()
    return data[0][str(key)]'''

'''print(json_change_value("version", True))
'''











