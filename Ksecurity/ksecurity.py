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

def server(server_name):
    print(f"Chosen server: {Fore.GREEN}{server_name}{Fore.RESET}")

    monitored_path = os.path.join('/etc/', server_name)
    
    if not os.path.exists(monitored_path) or not os.path.isdir(monitored_path):
        print(f"{Fore.RED}The chosen server path is not valid..")
        return

    code_main = multiprocessing.Process(target=server_performace)
    modulo1 = multiprocessing.Process(target=networkmonitor.start_monitoring)
    modulo2 = multiprocessing.Process(target=filemonitor.monitor, args=(server_name,))
    modulo3 = multiprocessing.Process(target=on_site.available)

    code_main.start()
    modulo1.start()
    modulo2.start()
    modulo3.start()

    code_main.join()
    modulo1.join()
    modulo2.join()
    modulo3.join()



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

        time.sleep(100)


if __name__ == '__main__':

    print("Switch an server to network monitor:")
    print(f"{Fore.CYAN}1 - Nginx")
    print(f"{Fore.CYAN}2 - Apache")

    server_number = input(f"{Fore.YELLOW}Enter the desired server number: ")

    if serverNumber == "1":
        server("nginx")

    elif serverNumber == "2":
        server("apache")

    else:
        print(f"{Fore.RED}Invalid option. Choose 1 for Nginx or 2 for Apache.")
