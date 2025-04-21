import pathlib, glob, os, re, subprocess
cwd = os.getcwd()
files = list(os.listdir(cwd))
files = [file for file in list(os.listdir(cwd)) if re.match("[0-9]{4,4}",file)]
for file in files:
    out = 0
    with open(os.devnull, 'wb') as devnull:
        try:
            out = subprocess.check_call(['python3', file], stdout=devnull, stderr=subprocess.STDOUT)
        except:
            out += 1
            print(f"{file} failed")
if out==0:
    print("Success! All tests pass.")