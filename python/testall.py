import pathlib, glob, os, re, subprocess
cwd = os.getcwd()
files = [file for file in os.listdir(cwd) if re.match(r"[0-9]{4,4}.*\\.py$", file)]
any_failed = False
for file in files:
    try:
        subprocess.check_output(['python3', file], stderr=subprocess.STDOUT)
        print(f"{file} ✓")
    except subprocess.CalledProcessError as e:
        any_failed = True
        print(f"{file} ✗")
        print(e.output.decode(errors='ignore'))
if not any_failed:
    print("All tests passed!")
else:
    print("Some tests failed.")