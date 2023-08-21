#!/usr/bin/env python3

"""
    Main command line tool with emulates the Jupyter runner.
"""

import argparse
import configparser
import sys

def _run(command):
    import subprocess
    return subprocess.run(command, capture_output=False, encoding='UTF-8')

def _pluto(notebook, deploy):
    command = ["julia", "-e"]
    code = "using Pluto;Pluto.run(;"
    code += "host=\"" + notebook["ip"] + "\", "
    code += "port=" + str(notebook["port"]) + ", "
    code += "base_url=\"" + notebook["base_url"] + "\", "
    code += "require_secret_for_access = false, "
    code += ")"
    command.append(code)
    print(command)
    print(f"Deploying: {deploy}")
    if (deploy):
        print(f"Fake Jupyter Server Pluto.jl is running on {notebook['ip']}:{notebook['port']}{notebook['base_url']}")
        _run(command)


if __name__ == "__main__":
    raw_args = sys.argv
    my_name = raw_args[0]

    if len(raw_args) > 1:
        if raw_args[1] == "lab":
            del raw_args[1]

    parser = argparse.ArgumentParser(description="Notebook shim.")
    parser.add_argument("--ServerApp.base_url", metavar="url", type=str, default="/")
    parser.add_argument("--ServerApp.allow_origin", metavar="origin", type=str, default="*")
    parser.add_argument("--ServerApp.allow_root", metavar="allow", type=bool, default=False)
    parser.add_argument("--ServerApp.port", metavar="port", type=int, default=8888)
    parser.add_argument("--ServerApp.ip", metavar="ip", type=str, default="127.0.0.1")
    parser.add_argument("--ServerApp.token", metavar="token", type=str, default="")

    args, unknown = parser.parse_known_args(raw_args)

    if unknown[0] == my_name:
        del unknown[0]

    notebook = {}

    notebook["port"] = getattr(args, "ServerApp.port")
    notebook["ip"] = getattr(args, "ServerApp.ip")
    notebook["base_url"] = getattr(args, "ServerApp.base_url")
    notebook["allow_origin"] = getattr(args, "ServerApp.allow_origin")
    notebook["allow_root"] = getattr(args, "ServerApp.allow_root")
    notebook["token"] = getattr(args, "ServerApp.token")

    config = configparser.ConfigParser()
    try:
        config.read("fake-jupyter.ini")
        provider = config["Configuration"]["provider"]
    except:
        print(f"Failed to read provider from \"fake-jupyter.ini\"")
        print(f"Defaulting to Pluto")
    try:
        provider = "pluto"
        deploy = (config["Configuration"]["deploy"].lower() == "true")
    except:
        print(f"Failed to read deploy from \"fake-jupyter.ini\"")
        print(f"Defaulting to true")
        deploy = True

    print(f"Selected provider: {provider}")
    print(f"Selected url: {notebook['ip']}:{notebook['port']}{notebook['base_url']}")
    print(f"Allow origin: {notebook['allow_origin']} Allow root: {notebook['allow_root']}")
    print(f"Token: {notebook['token']}")
    if len(unknown) > 0:
        print(f"Unknown arguments: {unknown}")

    if (provider == "pluto"):
        _pluto(notebook, deploy)
    else:
        print(f"Unknown provider: {provider}")