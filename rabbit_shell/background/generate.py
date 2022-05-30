import subprocess
import os
import random
import rabbit_shell
from rabbit_shell.background import editor

class generator:

    def __init__(self):


        self.module = "PyInstaller"
        self.python = self.getpy()



    def to_exe(self, path, name, ico):
        cmd = self.python + " -m " + self.module + f" --onefile --noconsole " + str(path)
        command = subprocess.run(cmd,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE
                                 )
        return command.returncode

    def getpy(self):
        if os.name == "nt":
            return "python"
        else:
            return "python3"


    def genlogkey(self, length=16):

        chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        key = ""
        for _ in range(int(length)):

            key += random.choice(chars)
        return key





