import requests
import threading
import argparse
from colorama import Fore, Style, init

init(autoreset=True)


def make_request(url, proxy):
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
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

    parser = argparse.ArgumentParser(description=Fore.CYAN + "Example: passurls -p <proxy_address> -l <urls_file_path> -t <threads>", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-l', type=str, required=True, help=Fore.CYAN + "Path to the list of URLs (e.g. /path/to/list/urls.txt)")
    parser.add_argument('-p', type=str, required=True, help=Fore.CYAN + "Proxy address (e.g. 127.0.0.1:8080)")
    parser.add_argument('-t', type=int, default=10, help=Fore.CYAN + "Number of threads to use (default 10)")

    args = parser.parse_args()


    with open(args.l, 'r') as file:
        urls = file.readlines()


    run_threads(urls, args.p, args.t)

if __name__ == "__main__":
    print(Fore.BLUE + "  _____  _______ _______ _______ _     _  ______        _______")
    print(Fore.BLUE + " |_____] |_____| |______ |______ |     | |_____/ |      |______ ")
    print(Fore.BLUE + " |       |     | ______| ______| |_____| |    \\_ |_____ ______|")
    print(Fore.RED + "                                                                ")
    print(Fore.RED + "        Coded by __> @ahmedhamdy0x (Gentil Security)")
    print(Fore.RESET + "")
    
    main()
