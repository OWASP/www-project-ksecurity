#!/usr/bin/python3
import multiprocessing
import os.path
import psutil
import time
from File_monitor import filemonitor
from Network_monitor import networkmonitor
from Available_site import on_site

from colorama import Fore, Back


banner = (Fore.GREEN+'''
_  ______  _____ ____ _   _ ____  ___ _______   __
| |/ / ___|| ____/ ___| | | |  _ \|_ _|_   _\ \ / /
| ' /\___ \|  _|| |   | | | | |_) || |  | |  \ V /
| . \ ___) | |__| |___| |_| |  _ < | |  | |   | |
|_|\_\____/|_____\____|\___/|_| \_\___| |_|   |

	           OWASP Ksecurity 1.0

Server Performance || Monitor Connections || Monitor Files || Website Availibility 

''')
print (banner)

def server_performace():
    while True:
        time.sleep(10)
        cpu_usage = psutil.cpu_percent(interval=1)
        print(Fore.GREEN+"-----------------------------------------------------------------------------")
        print("\t\t\tServer Performance")
        print(f"\n\t\t\tUsed of CPU: {cpu_usage}%")

        memory_usage = psutil.virtual_memory()
        print(f"\t\t\tUsed of  Memory: {memory_usage.percent}%")

        disk_usage = psutil.disk_usage('/')
        print(f"\t\t\tUsed of Disk: {disk_usage.percent}%")

        network_usage = psutil.net_io_counters()
        print(f"\t\t\tBytes Sent: {network_usage.bytes_sent}")
        print(f"\t\t\tBytes Received: {network_usage.bytes_recv}")
        print(Fore.GREEN+"-----------------------------------------------------------------------------")

        time.sleep(10000)


if __name__ == '__main__':
   
  code_main = multiprocessing.Process(target=server_performace)
  modulo1 = multiprocessing.Process(target=networkmonitor.start_monitoring)
  modulo2 = multiprocessing.Process(target=filemonitor.monitor)
  modulo3 = multiprocessing.Process(target=on_site.disponivel)

  code_main.start()
  modulo1.start()
  modulo2.start()
  modulo3.start()

  code_main.join()
  modulo1.join()
  modulo2.join()
  modulo3.join()
