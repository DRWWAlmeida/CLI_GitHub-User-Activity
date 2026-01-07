import argparse
from services.manager import Manager

manager = Manager()

def _cmd_check(args):
    manager.check(args.user_name)

def main():
    parser = argparse.ArgumentParser(prog='API', description="CLI Github activity")
    sub = parser.add_subparsers()

    check = sub.add_parser("check", help="Checar")
    check.add_argument("user_name", help="User name")
    check.set_defaults(func=_cmd_check)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()