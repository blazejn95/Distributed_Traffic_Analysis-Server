import os
import subprocess
import time
outp = subprocess.check_output("ls")
if "data" in outp:
    subprocess.Popen("rm data*", shell=True)
subprocess.Popen("tcpdump -w data -i br0 -C 5 -W 2 -s 96", shell=True)
