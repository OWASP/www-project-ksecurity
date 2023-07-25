#!/usr/bin/python3
# Monitorar disponibilidade do site

import time
import requests
from colorama import Fore

time.sleep(10)

def disponivel():
    while True:
        try:
           target = "http://localhost"
           response = requests.get(target)
           print(Fore.BLUE+"-----------------------------------------------------------------------------")
           print("\t\t\tSITE AVAILABILITY")
    
           if requests.status_codes == 500:
               print(f"\t\t\t\n {target} is unavailable")
           else:
               print(f"\t\t\t{target} is available")
        except requests.exceptions.RequestException as e:
           print(Fore.BLUE+"") 
           print(f"\t\tKsecurity don't get access {target}: {e}")
        print(Fore.BLUE+"-----------------------------------------------------------------------------")

        time.sleep(10000)


