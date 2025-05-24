from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re
from termcolor import colored

print(colored("-----------------------------------------------------------------------------------------------------------------------------------------\n", "green"))
print(colored('''  █████████                                   ███████████                       ██████████                            ███  ████         
 ███░░░░░███                                 ░░███░░░░░░█                      ░░███░░░░░█                           ░░░  ░░███         
░███    ░░░   ██████   ██████   ████████      ░███   █ ░   ██████  ████████     ░███  █ ░  █████████████    ██████   ████  ░███   █████ 
░░█████████  ███░░███ ░░░░░███ ░░███░░███     ░███████    ███░░███░░███░░███    ░██████   ░░███░░███░░███  ░░░░░███ ░░███  ░███  ███░░  
 ░░░░░░░░███░███ ░░░   ███████  ░███ ░███     ░███░░░█   ░███ ░███ ░███ ░░░     ░███░░█    ░███ ░███ ░███   ███████  ░███  ░███ ░░█████ 
 ███    ░███░███  ███ ███░░███  ░███ ░███     ░███  ░    ░███ ░███ ░███         ░███ ░   █ ░███ ░███ ░███  ███░░███  ░███  ░███  ░░░░███
░░█████████ ░░██████ ░░████████ ████ █████    █████      ░░██████  █████        ██████████ █████░███ █████░░████████ █████ █████ ██████ 
 ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░    ░░░░░        ░░░░░░  ░░░░░        ░░░░░░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░░░ ░░░░░░  
  
                                                                                                                        - By Spidy57''', "blue"))
print(colored("-----------------------------------------------------------------------------------------------------------------------------------------\n", "green"))

user_url = str(input(colored('[?] Enter Target URL To Scan: ', "light_yellow")))           # Use https:// or http:// before the website URL.
print()
urls = deque([user_url])

scraped_urls = set()
emails = set()

count = 0
try:
    while len(urls):
        count += 1
        if count == 100:
            break
        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)

        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        print(colored('[%d] Processing %s' % (count, url), "cyan"))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print(colored('\n[!] Closing!\n', "red"))
except Exception as e:
    print(colored('\n[!] Something went wrong...:(\n', "red"))
    print(colored(f"[-] Error: {e}","yellow"))

print(colored(f"\n[$] The Emails Caught in {user_url} :-", "magenta"))

for mail in emails:
    print(colored(mail, "white"))
