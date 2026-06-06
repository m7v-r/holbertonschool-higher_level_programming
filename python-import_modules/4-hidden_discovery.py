#!/usr/bin/python3
if __name__ == "__main__":
    import os
    import subprocess

    if not os.path.exists("/tmp/hidden_4.pyc"):
        url = "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc"
        subprocess.run(["curl", "-Lso", "/tmp/hidden_4.pyc", url])

    import sys
    sys.path.append('/tmp')
    import hidden_4

    all_names = dir(hidden_4)
    all_names.sort()

    for name in all_names:
        if not name.startswith("__"):
            print("{}".format(name))

