"""
MIT License

Copyright (c) 2022 greed albadi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os

from background import editor
from background import generate
from background import backstuff
import argparse
from data import about, basic
from data.banners import banner
class main:

    def __init__(self):


        parser = argparse.ArgumentParser()
        parser.add_argument("--server", action="store_true", help="server")
        parser.add_argument("--client", action="store_true", help="client")
        parser.add_argument("-host", "--host", help="Host")
        parser.add_argument("-port", "--port", help="Port")

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
            self.edit(host, port)

            print("Generating client exe please wait...")

            if self.generate_client() == 0:
                print("Done generating client exe, check dist folder.")
            else:
                print("Failed to generate.")

    def run_server(self, host: str, port: int):

        from server import server

        mbanner = banner.main_banner(host, port, about.__version__, about.__name__)
        backstuff.clear()
        print(mbanner)
        server = server.server(host, port)
        server.main()

    def generate_client(self):
        generator = generate.generator()
        path = "client\\client.py"
        return generator.to_exe(backstuff.fixed_path(path))




    def edit(self, host: str, port: str):
        editor.edit_basicvar("data/basic.py", "HOST", host)
        editor.edit_basicvar("data/basic.py", "PORT", int(port))
        return

if __name__ == "__main__":

    main()


