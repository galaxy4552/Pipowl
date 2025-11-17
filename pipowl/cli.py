import argparse
from .version import __version__
from .core import SnowOwlShell

def main():
    parser = argparse.ArgumentParser(prog="pipowl")
    parser.add_argument("command", nargs="?", default="help")
    args = parser.parse_args()

    if args.command == "hello":
        print("🦉 PipOwl Shell Online.")
    elif args.command == "version":
        print(f"pipowl version {__version__}")
    elif args.command == "modules":
        print("No modules loaded yet.")  # 後面 plugin system 會塞進來
    else:
        print("""Available commands:
  pipowl hello
  pipowl version
  pipowl modules
        """)
