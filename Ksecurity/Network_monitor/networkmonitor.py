#!/usr/bin/python3
from colorama import Fore
import re,os
import socket
import subprocess
import os, time

time.sleep(10)

def get_new_connections(existing_connections):
  
    output = subprocess.check_output(['netstat', '-ntu','-nlpt']).decode()

    connection_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b"
    connections = re.findall(connection_pattern, output)

    new_connections = [conn for conn in set(connections) if conn not in existing_connections]

    existing_connections.extend(new_connections)

    return new_connections

def is_internal_ip(ip_address):
   
    octets = ip_address.split('.')
    if octets[0] == '10':
        return True
    elif octets[0] == '192' and octets[1] == '168':
        return True
    elif octets[0] == '172' and 16 <= int(octets[1]) <= 31:
        return True
    elif ip_address == '127.0.0.1':
        return True
    else:
        return False
def start_monitoring():
    existing_connections = []
    try:

        while True:

              new_connections = get_new_connections(existing_connections)
              for connection in new_connections:
                  ip_address, port = connection.split(':')
                  if is_internal_ip(ip_address):
                      print(Fore.YELLOW+"")
                      print(f"\t\t\tNew connection internal: {ip_address}:{port}")
                  else:
                      
                      print(f"\t\t\tNew connection external: {ip_address}:{port}")
        time.sleep(1000)                      	
    except KeyboardInterrupt:
        print("Bye bye.")

