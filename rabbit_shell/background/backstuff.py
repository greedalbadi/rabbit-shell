import os
import subprocess
from rabbit_shell.data import about, basic
def startup_shortcut(path, dir, shortcut):
    if isfile_path(dir + "\\" + path) != True:
        text = f'start {os.getcwd()}\\{shortcut}.exe"'
        os.chdir(dir)
        to = open(path, "w+")
        to.write(text)
        to.flush()
        to.close()
    return

def server_info():
    dic = {
        "name": about.__name__,
        "version": about.__version__,
        "host": basic.HOST,
        "port": basic.PORT
    }
    return dic

def runcommand(command: str):

    cmd = subprocess.Popen(command,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE
                            )
    cmd.wait()

    return cmd.stdout.read() + cmd.stderr.read()

def clear():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def isfile_path(path):

    return os.path.isfile(path)

def fixed_path(path):

    if os.name == "nt":
        if "/" in path:
            return path.replace("/", "\\")
    else:
        if "\\" in path:
            return path.replace("\\", "/")

    return path

