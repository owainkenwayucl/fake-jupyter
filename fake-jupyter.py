#!/usr/bin/env python3

"""
    Main command line tool with emulates the Jupyter runner.
"""

if __name__ == "__main__":
    import argparse
    import configparser
    import sys

    raw_args = sys.argv
    my_name = raw_args[0]
    if not (my_name == "jupyter"):
        print(f"Warning: \"{my_name}\" will not override \"jupyter\"")
    if len(raw_args) > 1:
        if raw_args[1] == "lab":
            del raw_args[1]

    parser = argparse.ArgumentParser(description="Notebook shim.")
    parser.add_argument("--ServerApp.base_url", metavar="url", type=str, default="/")
    parser.add_argument("--ServerApp.allow_origin", metavar="origin", type=str, default="*")
    parser.add_argument("--ServerApp.allow_root", metavar="allow", type=bool, default=False)
    parser.add_argument("--ServerApp.port", metavar="port", type=int, default=8888)
    parser.add_argument("--ServerApp.ip", metavar="ip", type=str, default="127.0.0.1")

    args, unknown = parser.parse_known_args(raw_args)

    if unknown[0] == my_name:
        del unknown[0]


    port = getattr(args, "ServerApp.port")
    ip = getattr(args, "ServerApp.ip")
    base_url = getattr(args, "ServerApp.base_url")
    allow_origin = getattr(args, "ServerApp.allow_origin")
    allow_root = getattr(args, "ServerApp.allow_root")  

    config = configparser.ConfigParser()
    config.read("fake-jupyter.ini")
    provider = config["Configuration"]["provider"]

    print(f"Selected provider: {provider}")
    print(f"Selected url: {ip}:{port}{base_url}")
    print(f"Allow origin: {allow_origin} Allow root: {allow_root}")
    if len(unknown) > 0:
        print(f"Unknown arguments: {unknown}")