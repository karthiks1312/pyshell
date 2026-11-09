import shlex
import subprocess
from os import chdir, getcwd
from pathlib import Path

PROMPT = "shell> "


def run_cd(args):
    if len(args) > 1:
        print("cd: too many arguments")
        return
    path = Path(args[0]).expanduser() if args else Path.home()
    try:
        chdir(path)
    except OSError as e:
        print(f"cd: {path}: {e.strerror}")


def run_pwd(args):
    if args:
        print("pwd: too many arguments")
    else:
        print(getcwd())


def run_external(cmd, args):
    try:
        subprocess.run([cmd, *args])
    except FileNotFoundError:
        print(f"{cmd}: command not found")
    except PermissionError:
        print(f"{cmd}: permission denied")
    except OSError as e:
        print(f"{cmd}: {e.strerror}")


def execute(cmd_line):
    """Run one command line. Returns False when the shell should exit."""
    try:
        tokens = shlex.split(cmd_line)
    except ValueError as e:
        print(f"parse error: {e}")
        return True
    if not tokens or not tokens[0]:
        return True
    cmd, *args = tokens

    match cmd:
        case "exit":
            return False
        case "cd":
            run_cd(args)
        case "pwd":
            run_pwd(args)
        case _:
            run_external(cmd, args)
    return True


def pyshell():
    while True:
        try:
            cmd_line = input(PROMPT).strip()
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            continue

        if not cmd_line:
            continue
        if not execute(cmd_line):
            break


main = pyshell

if __name__ == "__main__":
    pyshell()
