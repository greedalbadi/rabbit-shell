'''import sys
sys.path.insert(0, '..')'''
import os
import colorama
colorama.init()
def main_banner(host, port, version, name):
    file = open("data\\banners\\rabbit.txt", "r")
    banner = colorama.Fore.LIGHTGREEN_EX + str(file.read())
    banner = banner.replace("NAME", str(name))
    banner = banner.replace("VERSION", str(version))
    banner = banner.replace("ADDRESS", str(host))
    banner = banner.replace("PORT", str(port))
    file.close()
    return banner
