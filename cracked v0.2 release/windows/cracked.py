import os
import sys
from termcolor import colored
from time import sleep
import hashlib

#windows specific
os.system("color")

def run():
    for word in passfile:
        encword = word.encode("utf-8")
        hashattempt = hashlib.sha256(encword.strip()).hexdigest()
        if hash == hashattempt:
            print(colored("success", "green"))
            print(colored("hash has been confirmed as " + word, "yellow"))
            sleep(10)
            exit()

        else:
            hashattempt = hashlib.md5(encword.strip()).hexdigest()
            if hash == hashattempt:
                print(colored("success", "green"))
                print(colored("hash has been confirmed as " + word, "yellow"))
                sleep(10)
                exit()

            else:
                hashattempt = hashlib.sha1(encword.strip()).hexdigest()
                if hash == hashattempt:
                    print(colored("success", "green"))
                    print(colored("hash has been confirmed as " + word, "yellow"))
                    sleep(10)
                    exit()

                else:
                    hashattempt = hashlib.sha224(encword.strip()).hexdigest()
                    if hash == hashattempt:
                        print(colored("success", "green"))
                        print(colored("hash has been confirmed as " + word, "yellow"))
                        sleep(10)
                        exit()

                    else:
                        print(colored("fail", "red"))
                        print(colored("hash could not be confirmed", "yellow"))

print(colored(r"""

 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗     ██╗   ██╗ ██████╗    ██████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██║   ██║██╔═████╗   ╚════██╗
██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║    ██║   ██║██║██╔██║    █████╔╝
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ╚██╗ ██╔╝████╔╝██║   ██╔═══╝
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝     ╚████╔╝ ╚██████╔╝██╗███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝       ╚═══╝   ╚═════╝ ╚═╝╚══════╝

                    """, "yellow"))

print(colored("input hash", "yellow"))
hash = input(">")
print(colored(r"""input prefered dataset, standard (1) or custom (2)
(standard dataset is comp of several existing wordlists, custom requires user configuration of customset.dat file)""", "yellow"))
dataset = input(">")
if dataset == "1":
    passfile = open("standard.dat", "r")
elif dataset == "2":
    passfile = open("customset.dat", "r")
run()
