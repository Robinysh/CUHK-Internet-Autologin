#!/usr/bin/env python3
import os
import psutil
from time import sleep
from datetime import datetime
import socket
import urllib.request
import urllib.error

import subprocess

PROCNAME = 'chromedriver'
SLEEP_TIME = 10
 
def kill_chromedriver():
    for proc in psutil.process_iter():
        if proc.name == PROCNAME:
            proc.kill()

def is_connected_git_method():
  # Note that you need to have a valid github key on your computer
  # Even read-only deploy keys of one particular repo works
  try:
    result = subprocess.run(["ssh", "-T", "git@github.com", "-o ConnectTimeout=2"])
    print(result.returncode)
    return (result.returncode == 1)
  except Exception as _:
    return False

def is_connected(host="8.8.8.8", port=53, timeout=3):
  """
  Host: 8.8.8.8 (google-public-dns-a.google.com)
  OpenPort: 53/tcp
  Service: domain (DNS/TCP)
  """
  try:
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    return True
  except Exception as ex:
    return False

def start_wifi():
    print(('# restarting internet connection ({now})'.format(now=datetime.now())))
    os.system('python ./login.py')
    print('# restarted internet connection')
 
def main():
    while True:
        if not is_connected_git_method():
            print('# network is down')
            start_wifi()
            kill_chromedriver()
        else:
            print('# network is up')
            pass
        sleep(SLEEP_TIME)
 
if __name__ == "__main__":
    main()

