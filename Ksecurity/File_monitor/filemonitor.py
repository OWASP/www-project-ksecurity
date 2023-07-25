#!/usr/bin/python3
# Plugin Pro Ksecurity e um novo plugin de monitoramento de ataques ciberneticos no servidor
# Apache, monitora os seguintes diretorios e alerta de acesso.

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import Fore
import socket
import multiprocessing
import os.path
import time

diretorio_monitorado = '/etc/apache2'

def monitor():
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
    observer.schedule(MonitorAlteracoes(), diretorio_monitorado, recursive=True)
    observer.start()
    try:
       while True:
           time.sleep(1)
    except KeyboardInterrupt:
           observer.stop()
           observer.join()

