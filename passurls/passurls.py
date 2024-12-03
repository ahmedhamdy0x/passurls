import requests
import threading
import argparse
from colorama import Fore, Style, init
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

init(autoreset=True)

def print_logo():
    print(Fore.BLUE + "")
    print(Fore.BLUE + "  _____  _______ _______ _______ _     _  ______        _______")
    print(Fore.BLUE + " |_____] |_____| |______ |______ |     | |_____/ |      |______ ")
    print(Fore.BLUE + " |       |     | ______| ______| |_____| |    \\_ |_____ ______|")
    print(Fore.RED + "                                                                ")
    print(Fore.RED + "        Coded by __> @ahmedhamdy0x (Gentil Security)\n")
    print(Fore.RESET + "")

def make_request(url, proxy):
    try:
        proxies = {
            "http": proxy,
            "https": proxy  # تأكد من أن البروكسي يدعم HTTPS
        }
        response = requests.get(url, proxies=proxies, verify=False)
        if response.status_code == 200:
            print(Fore.GREEN + f"Success: {url} - Status Code: {response.status_code}")
        else:
            print(Fore.YELLOW + f"Error: {url} - Status Code: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"Failed: {url} - Error: {str(e)}")

def run_threads(urls, proxy, threads):
    thread_list = []
    for url in urls:
        thread = threading.Thread(target=make_request, args=(url.strip(), proxy))
        thread_list.append(thread)
        thread.start()
        if len(thread_list) >= threads:
            for t in thread_list:
                t.join()
            thread_list = []
    for t in thread_list:
        t.join()

def main():
    print_logo()

    parser = argparse.ArgumentParser(
        usage=argparse.SUPPRESS,
        description=Fore.WHITE + "Example: passurls -p [PROXY] -l [LIST] -t [THREADS]" + Fore.CYAN,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument('-l', '--list', type=str, required=True, metavar='', help=Fore.CYAN + "Path to the list of URLs (e.g. /path/to/list.txt)")
    parser.add_argument('-p', '--proxy', type=str, required=True, metavar='', help=Fore.CYAN + "Proxy address (e.g. 127.0.0.1:8080)")
    parser.add_argument('-t', '--threads', type=int, default=10, metavar='', help=Fore.CYAN + "Number of threads to use (default 10)")

    args = parser.parse_args()

    with open(args.list, 'r') as file:
        urls = file.readlines()

    run_threads(urls, args.proxy, args.threads)

if __name__ == "__main__":
    main()
