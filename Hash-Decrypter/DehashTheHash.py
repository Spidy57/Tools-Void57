import hashlib
from termcolor import colored
import time

def animation(counter):
  while counter == 0:
    print(colored("[-] Finding the hash match password...", "light_magenta"))
    time.sleep(0.05)
    print('\033[F\033[K', end='')
    print(colored("[\] Finding the hash match password...", "light_magenta"))
    time.sleep(0.05)
    print('\033[F\033[K', end='')
    print(colored("[|] Finding the hash match password...", "light_magenta"))
    time.sleep(0.05)
    print('\033[F\033[K', end='')
    print(colored("[/] Finding the hash match password...", "light_magenta"))
    time.sleep(0.05)
    print('\033[F\033[K', end='')
    return 1

class DehashTheHash:
    def __init__(self):
        print(colored("\n--------------------------------------------------------------------------------------------------------------------\n", "cyan"))
        print(colored('''▓█████▄ ▓█████  ██░ ██  ▄▄▄        ██████  ██░ ██    ▄▄▄█████▓ ██░ ██ ▓█████     ██░ ██  ▄▄▄        ██████  ██░ ██    
▒██▀ ██▌▓█   ▀ ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒   ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒   
░██   █▌▒███   ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░   ▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░   
░▓█▄   ▌▒▓█  ▄ ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██    ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██    
░▒████▓ ░▒████▒░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓     ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓   
 ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒     ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░    ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒   
 ░ ▒  ▒  ░ ░  ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░       ░     ▒ ░▒░ ░ ░ ░  ░    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░   
 ░ ░  ░    ░    ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░     ░       ░  ░░ ░   ░       ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   
   ░       ░  ░ ░  ░  ░      ░  ░      ░   ░  ░  ░             ░  ░  ░   ░  ░    ░  ░  ░      ░  ░      ░   ░  ░  ░   \n
                                                                                                        - By Spidy57''', color="red"))
        print(colored("\n--------------------------------------------------------------------------------------------------------------------\n\n", "cyan"))
        print(colored("[~] Choose the type of hash from the following list of hashes:\n", "light_yellow"))
        print(colored("0. Unknown (try all 14 hashes)\n1. md5\n2. sha1\n3. sha224\n4. sha256\n5. sha384\n6. sha512\n7. sha3_224\n8. sha3_256\n9. sha3_384\n10. sha3_512\n11. blake2b\n12. blake2s\n13. shake_128\n14. shake_256\n", "light_blue"))
        self.hashtype = int(input(colored("[?] Enter the choice(1 - 14): ", "light_yellow")).strip())
        self.thehash = input(colored("\n[?] Enter the hash you want to dehash: ", "light_yellow")).strip()
        self.passfile = input(colored("\n[?] Enter the password file(path) on which you want to check the hash: ", "light_yellow")).strip()
        print('\n', end="")
        self.hashTypeDetermine()
        
    def hashTypeDetermine(self):
      match(self.hashtype):
        case 0:
          self.check_all_hashes()
        case 1:
          self.hash_md5()
        case 2:
          self.hash_sha1()
        case 3:
          self.hash_sha224()
        case 4:
          self.hash_sha256()
        case 5:
          self.hash_sha384()
        case 6:
          self.hash_sha512()
        case 7:
          self.hash_sha3_224()
        case 8:
          self.hash_sha3_256()
        case 9:
          self.hash_sha3_384()
        case 10:
          self.hash_sha3_512()
        case 11:
          self.hash_blake2b()
        case 12:
          self.hash_blake2s()
        case 13:
          self.hash_shake_128()
        case 14:
          self.hash_shake_256()
        case _:
          print(colored("\n[!] Something went wrong try again carefully...", "red"))
          exit(0)
          
    def check_all_hashes(self):
      hash_functions = [
          ('MD5', hashlib.md5),
          ('SHA1', hashlib.sha1),
          ('SHA224', hashlib.sha224),
          ('SHA256', hashlib.sha256),
          ('SHA384', hashlib.sha384),
          ('SHA512', hashlib.sha512),
          ('SHA3_224', hashlib.sha3_224),
          ('SHA3_256', hashlib.sha3_256),
          ('SHA3_384', hashlib.sha3_384),
          ('SHA3_512', hashlib.sha3_512),
          ('BLAKE2b', hashlib.blake2b),
          ('BLAKE2s', hashlib.blake2s),
      ]

      try:
        with open(self.passfile, 'r') as file:
          for line in file:
            password = line.strip()
            for name, func in hash_functions:
              result = func(password.encode()).hexdigest()
              if result == self.thehash:
                print(colored(f"[+] {name} Hash Password Found: {password}", "green"))
                exit(0)
              else:
                counter = 0
                counter = animation(counter)
            for length in range(16, 65):
              shake128 = hashlib.shake_128(password.encode()).hexdigest(length)
              if shake128 == self.thehash:
                print(colored(f"[+] SHAKE-128 Hash Password Found: {password}", "green"))
                print(colored(f"[@] Digest length matched: {length} bytes", "cyan"))
                exit(0)
              else:
                counter = 0
                counter = animation(counter)
              shake256 = hashlib.shake_256(password.encode()).hexdigest(length)
              if shake256 == self.thehash:
                print(colored(f"[+] SHAKE-256 Hash Password Found: {password}", "green"))
                print(colored(f"[@] Digest length matched: {length} bytes", "cyan"))
                exit(0)
              else:
                counter = 0
                counter = animation(counter)
          print(colored("[-] Password not found using any supported hash type.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
      
          
    def hash_md5(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.md5(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] MD5 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))

    def hash_sha1(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.sha1(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] SHA1 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
    
    def hash_sha224(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.sha224(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] SHA224 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))

    def hash_sha256(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.sha256(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] SHA256 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
          
    def hash_sha384(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.sha384(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] SHA384 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
          
    def hash_sha512(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.sha512(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] SHA512 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
          
    def hash_sha3_224(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.sha3_224(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] SHA3_224 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
          
    def hash_sha3_256(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.sha3_256(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] SHA3_256 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
      
    def hash_sha3_384(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.sha3_384(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] SHA3_384 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
        
    def hash_sha3_512(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.sha3_512(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] SHA3_512 Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
          
    def hash_blake2b(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.blake2b(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] BLAKE2b Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))

    def hash_blake2s(self):
      try:
          with open(self.passfile, 'r') as file:
              for line in file:
                  password = line.strip()
                  hash_object = hashlib.blake2s(password.encode())
                  if hash_object.hexdigest() == self.thehash:
                      print(colored("\n[+] BLAKE2s Hash Password Found:", "green"), password)
                      exit(0)
                  else:
                    counter = 0
                    counter = animation(counter)         
          print(colored("[!] Password not found in the file.", "red"))
      except FileNotFoundError:
          print(colored("[!] Password file not found.", "red"))
          
    def hash_shake_128(self):
      with open(self.passfile, 'r') as file:
        for line in file:
          line = line.strip()
          for length in range(16, 65):
            hash_object = hashlib.shake_128(line.encode())
            hash_string = hash_object.hexdigest(length)
            if hash_string == self.thehash:
              print(colored(f"[+] SHAKE-128 Hash Password Found: {line}", "green"))
              print(colored(f"[@] Digest length matched: {length} bytes", "cyan"))
              return
            else:
              counter = 0
              counter = animation(counter)
      print(colored("[-] Password not found for any SHAKE-128 digest length (16-64 bytes).", "red"))
      
      def hash_shake_256(self):
        with open(self.passfile, 'r') as file:
            for line in file:
              line = line.strip()
              for length in range(16, 65):
                hash_object = hashlib.shake_256(line.encode())
                hash_string = hash_object.hexdigest(length)
                if hash_string == self.thehash:
                  print(colored(f"[+] SHAKE-256 Hash Password Found: {line}", "green"))
                  print(colored(f"[@] Digest length matched: {length} bytes", "cyan"))
                  return
                else:
                  counter = 0
                  counter = animation(counter)
        print(colored("[-] Password not found for any SHAKE-256 digest length (16-64 bytes).", "red"))

obj = DehashTheHash()