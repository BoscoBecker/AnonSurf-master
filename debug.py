import subprocess
import chardet

process = subprocess.Popen(["./anonsurf/bin/win32/tor.exe"], stdout=subprocess.PIPE)

while True:
    print(chardet.detect(process.stdout.readline()))