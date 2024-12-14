"""

Built With Bob The Builder

"""

import requests, os, queue, threading
from colorama import Fore

# ----------------------------------------- #

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

# ----------------------------------------- #

api = "https://github.com/Not-ISellStuff/CAIO/blob/main/Modules/Checkers/bww.py"
hit = "test1"
bad = "test2"

def d(username, password):
    d = {}
    return d

class Checker:
    def __init__(self, threads: int, accounts: list):
        self.threads = threads
        self.accounts = accounts

    def cls(self):
        os.system('cls')

    def load_accounts(self):
        try:

            with open("combo.txt", 'r', encoding='utf-8') as f:
                accounts = f.readlines()
            for i in accounts:
                self.accounts.append(i)

            return len(accounts)
        
        except:
            with open("combo.txt", "w") as f:
                pass

            return 0
    
    # ------------------------------------------- #

    def main(self):
        q = queue.Queue()
        for i in self.accounts:
            p = i.strip()
            acc = p.split(":")
            q.put(acc)

        try:
            with open("hits.txt", "r") as f:
                pass
        except:
            with open("hits.txt", "w") as f:
                pass

        def login(q):
            while not q.empty():
                try:
                    combo = q.get()
                    username, password = combo
                    acc = f"{username}:{password}"
                    r = requests.post(api, data=d(username, password))

                    if hit in r.text:
                        print(green + f"[+] {acc}")
                        with open("hits.txt", "a", encoding="utf-8") as f:
                            f.write(acc + "\n")

                    elif bad in r.text:
                        print(red + f"[-] {acc}")
                    else:
                        print(yellow + f"[!] {acc}")
                except:
                    pass

        threads = []
        for i in range(self.threads):
            t = threading.Thread(target=login, args=(q,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

# ----------------------------------------- #

def main():
    checker = Checker(0, [])
    checker.cls()
    accs = checker.load_accounts()

    print(green + f"[+] Loaded {accs} accounts\n")

    while True:
        try:
            checker.cls()
            threads = int(input(cyan + "Threads: "))
            checker.threads = threads
            break
        except:
            pass

    checker.cls()
    input(cyan + f"Accounts: {checker.accounts} | Threads: {checker.threads} | Press Enter To Start > ")
    checker.main()

    input(cyan + "\nStopped Checking Press Enter To Close > ")

if __name__ == "__main__":
    main()