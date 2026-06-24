# Firewall Demo

import os
import time
import socket

# List of ANSI colors
def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

# Blocked sites appended to this list upon script execution
blockedList = []

def firewall():
    if os.path.exists("blocked_list.txt"):
        with open("blocked_list.txt", "r") as bl:
            values = [line.strip() for line in bl if line.strip()]
            if values:
                blockedList.extend(values)
firewall()

def resolve(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror as e:
        return f"Couldn't resolve {hostname}: {e}"

def Uques():
    user_prompt = input(green("Would you like to make another query? (y/n): "))
    if user_prompt == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        user_search()
    elif user_prompt == "n":
        os._exit(0)
    else:
        print(red("Invalid Input"))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        Uques();

def dns_search(query):
    for item in blockedList:
        if item in query:
            print(bold(red("Website Blocked")))
            time.sleep(3)
            return user_search()
    print(resolve(query))
    time.sleep(3)
    Uques()

def user_search():
    query = input(green("Enter your search here: ")).strip().lower()
    if not query:
        print(green("No query entered. Exiting..."))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        os._exit(0)
    dns_search(query);
user_search()