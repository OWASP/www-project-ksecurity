#!/usr/bin/python3

from colorama import Fore
import time
import psutil


def server_performace():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"Used of  CPU: {cpu_usage}%")

        memory_usage = psutil.virtual_memory()
        print(f"Used of Memory: {memory_usage.percent}%")
     
        disk_usage = psutil.disk_usage('/')
        print(f"Used of Disk: {disk_usage.percent}%")

        network_usage = psutil.net_io_counters()
        print(f"Bytes sent: {network_usage.bytes_sent}")
        print(f"Bytes Received: {network_usage.bytes_recv}")

        time.sleep(5)
server_performace()
