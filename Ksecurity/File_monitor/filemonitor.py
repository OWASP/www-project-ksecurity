#!/usr/bin/python3
# Plugin Pro Ksecurity is a new cyber attack monitoring plugin for Apache and Nginx servers.
# It monitors the following directories and alerts on access: /etc/nginx and /etc/apache.

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import Fore
import socket
import multiprocessing
import os.path
import time


def monitor(server_name):
    class MonitorAlteracoes(FileSystemEventHandler):
        def on_any_event(self, event):
            if event.is_directory:
                return 
            elif event.event_type == 'modified':
                 print(Fore.RED+"")
                 print(f"\t\t\tmodified file: {event.src_path} - Time: {time.ctime()}")
        
            elif event.event_type == 'created':
                 print(Fore.YELLOW+"")
                 print (f"\t\t\tCreated file: {event.src_path} - Time: {time.ctime()}")

            elif event.event_type == 'deleted':
                 print(Fore.BLUE+"") 
                 print (f"\t\t\tDeleted file: {event.src_path} - Time:{time.ctime()}")

    observer = Observer()
    monitored_path = os.path.join('/etc/', server_name)
    observer.schedule(MonitorAlteracoes(), monitored_path, recursive=True)
    observer.start()
    try:
       while True:
           time.sleep(1)
    except KeyboardInterrupt:
           observer.stop()
           observer.join()

