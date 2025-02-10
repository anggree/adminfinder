import os
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.WHITE
CYAN = Fore.CYAN
def jembut():
  print (f"""
  {GREEN}

 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝

{RESET}
github: github.com/anggree
telegram: t.me/jrexril
tools adminfinder
version: 1.0
  """)
def cek_kontol(url, path):
    full_url = f"{url}/{path}"
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            print(f"{GREEN}[+]{RESET} {full_url} → {response.status_code}")
        elif response.status_code == 403:
            print(f"{RED}[FORBIDDEN]{RESET} {full_url} → {response.status_code}")
    except requests.exceptions.RequestException:
        pass

def kontol(wordlist_file):
    url = input("MASUKAN URL: ").strip()
    
    if not os.path.exists(wordlist_file):
        print(f"{RED}[ERROR]{RESET} File '{wordlist_file}' tidak ditemukan!")
        return
    with open(wordlist_file, "r") as f:
        paths = f.read().splitlines()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for path in paths:
            executor.submit(cek_kontol, url, path)
jembut()
kontol("wordlist.txt")