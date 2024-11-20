import subprocess 
import sys

def ccsh():
    while True:
        cmd = input("shell> ").strip()
        if cmd == "exit":
            sys.exit(0)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
    
if __name__ == "__main__":
    ccsh()
