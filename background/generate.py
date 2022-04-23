'import subprocess'
import os



class generator:

    def __init__(self):


        self.module = "PyInstaller"
        self.python = self.getpy()



    def to_exe(self, path):
        print(99)
        cmd = self.python + " -m " + self.module + f" --onefile --noconsole " + str(path)
        '''        command = subprocess.Popen(cmd,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE
                                 )
                print(77)
                command.wait()'''

        return os.system(cmd)

    def getpy(self):
        if os.name == "nt":
            return "python"
        else:
            return "python3"