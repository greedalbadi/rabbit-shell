import os
import subprocess
def startup_shortcut(path, dir):
    if isfile_path(dir + "\\" + path) != True:
        text = f'start {os.getcwd()}\\client.exe"'
        os.chdir(dir)
        to = open(path, "w+")
        to.write(text)
        to.flush()
        to.close()
    return

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



