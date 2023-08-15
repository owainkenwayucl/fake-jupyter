#!/usr/bin/env python3

"""
    Main command line tool with emulates the Jupyter runner.
"""

if __name__ == "__main__":
    import argparse
    import configparser
    import sys

    raw_args = sys.argv
    if len(raw_args) > 0:
        if raw_args[1] == "lab":
            del raw_args[1]
    del raw_args[0]

    parser = argparse.ArgumentParser(description="Notebook shim.")
    parser.add_argument("--ServerApp.port", metavar="port", type=int, default=8888)
    parser.add_argument("--ServerApp.ip", metavar="port", type=str, default="127.0.0.1")

    args, unknown = parser.parse_known_args(raw_args)

    port = getattr(args, "ServerApp.port")
    ip = getattr(args, "ServerApp.ip")
    

    config = configparser.ConfigParser()
    config.read("fake-jupyter.ini")
    provider = config["Configuration"]["provider"]

    print(f"Selected provider: {provider}")
    print(f"Selected ip/port: {ip}:{port}")
    print(f"Unknown arguments: {unknown}")