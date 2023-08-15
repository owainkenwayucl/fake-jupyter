#!/usr/bin/env python3

"""
    Main command line tool with emulates the Jupyter runner.
"""

if __name__ == "__main__":
    import argparse
    import configparser

    config = configparser.ConfigParser()

    config.read("fake-jupyter.ini")
    provider = config["Configuration"]["provider"]

    print(f"Selected provider: {provider}")