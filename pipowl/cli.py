import argparse
from .version import __version__
from .core import SnowOwlShell  # 預留，刻意不使用

BANNER = r"""
██████╗ ██╗██████╗  ██████╗  ██████╗ ██╗     
██╔════╝ ██║██╔══██╗██╔═══██╗██╔══██╗██║     
██║  ███╗██║██████╔╝██║   ██║██████╔╝██║     
██║   ██║██║██╔══██╗██║   ██║██╔══██╗██║     
╚██████╔╝ ██║██║  ██║╚██████╔╝██║  ██║███████╗
 ╚═════╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                   🦉 pipowl {version}
"""

def main():
    parser = argparse.ArgumentParser(
        prog="pipowl",
        add_help=False
    )

    parser.add_argument("command", nargs="?", default="help")
    parser.add_argument("--version", action="store_true")
    parser.add_argument("-h", "--help", action="store_true")

    args = parser.parse_args()

    if args.version:
        print(f"pipowl {__version__}")
        return

    if args.help or args.command == "help":
        print(BANNER.format(version=__version__))
        print("""Available commands:
  pipowl hello        Show shell status
  pipowl modules      List loaded modules (none yet)
  pipowl --version    Show version
""")
        return

    if args.command == "hello":
        print("🦉 PipOwl Shell Online. (shell inactive)")
        return

    if args.command == "modules":
        print("No modules loaded yet.")
        return

    print(f"Unknown command: {args.command}")
    print("Use `pipowl help` to see available commands.")


if __name__ == "__main__":
    main()
