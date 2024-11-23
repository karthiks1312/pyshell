from os import chdir, getcwd
from pathlib import Path
from subprocess import run
import sys

def ccsh():
    while True:
        cmd_line = input("shell> ").strip()
        cmd, *args = cmd_line.split(' ')

        match cmd:
            case "": continue

            case 'cd':
                if len(args) > 1:
                    print("Too many args")
                else:
                    path = args[0] if len(args) == 1 else Path.home()
                    chdir(path)
            case 'pwd':
                if args:
                    print('Too many args')
                else:
                    print(getcwd())
            case other:
                try:    
                    cmd_args = [cmd]
                    cmd_args.extend(args)
                    run(cmd_args, shell=True, stdout=sys.stdout, stderr=sys.stderr)
                except Exception as e:
                    print(e)
        
if __name__ == "__main__":
    ccsh()
