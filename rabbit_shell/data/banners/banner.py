import sys



import colorama
from rabbit_shell import fixed_path, clear
import rabbit_shell
from rabbit_shell.data import basic, about
import os
colorama.init()
def main_banner(host=basic.HOST, port = basic.PORT, version=about.__name__, name=about.__version__):
    file = open(fixed_path(f"{os.path.dirname(rabbit_shell.__file__)}\\data\\banners\\rabbit.txt"), "r")
    banner = colorama.Fore.LIGHTGREEN_EX + str(file.read())
    banner = banner.replace("NAME", str(name))
    banner = banner.replace("VERSION", str(version))
    banner = banner.replace("ADDRESS", str(host))
    banner = banner.replace("PORT", str(port))
    file.close()
    return banner
