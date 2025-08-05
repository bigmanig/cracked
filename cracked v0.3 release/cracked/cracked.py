import os
import sys
from termcolor import colored
from time import sleep
import hashlib
from multiprocessing import Process, Event, Queue, freeze_support

if sys.platform.startswith("win"):
    os.system("color")

def detect_hash_type(hash_input):
    length = len(hash_input)
    if length == 32:
        return "md5"
    elif length == 40:
        return "sha1"
    elif length == 56:
        return "sha224"
    elif length == 64:
        return "sha256"
    else:
        return None

def check_hashes(hash_type, wordlist, hash_to_crack, variations, found_event, result_queue, status_queue):
    for word in wordlist:
        if found_event.is_set():
            return

        base = word.strip()
        combos = [base] + [base + v.strip() for v in variations]

        for combo in combos:
            if found_event.is_set():
                return

            encoded = combo.encode("utf-8")
            if hash_type == "sha256":
                attempt = hashlib.sha256(encoded).hexdigest()
            elif hash_type == "md5":
                attempt = hashlib.md5(encoded).hexdigest()
            elif hash_type == "sha1":
                attempt = hashlib.sha1(encoded).hexdigest()
            elif hash_type == "sha224":
                attempt = hashlib.sha224(encoded).hexdigest()
            else:
                continue

            if attempt == hash_to_crack:
                found_event.set()
                result_queue.put(combo)
                return
            else:
                status_queue.put(colored("fail", "red") + " - tried: " + combo)

def run(passfile, variations, hash_to_crack):
    wordlist = [line.strip() for line in passfile]
    found_event = Event()
    result_queue = Queue()
    status_queue = Queue()

    hash_type = detect_hash_type(hash_to_crack)
    if not hash_type:
        print(colored("could not detect hash type", "red"))
        sleep(5)
        return

    processes = []
    p = Process(target=check_hashes, args=(hash_type, wordlist, hash_to_crack, variations, found_event, result_queue, status_queue))
    processes.append(p)
    p.start()

    try:
        while True:
            while not status_queue.empty():
                msg = status_queue.get()
                print(msg)

            if not result_queue.empty():
                confirmed = result_queue.get()
                print(colored("success", "green"))
                print(colored("hash has been confirmed as " + confirmed, "yellow"))
                input()
                os._exit(0)

            if all(not p.is_alive() for p in processes):
                while not status_queue.empty():
                    msg = status_queue.get()
                    print(msg)
                break

            sleep(0.05)

    except KeyboardInterrupt:
        print(colored("terminated by user", "red"))
        for p in processes:
            p.terminate()

    print(colored("fail", "red"))
    print(colored("hash could not be confirmed", "yellow"))
    sleep(10)

# UI

if __name__ == "__main__":
    freeze_support()  # Windows compatibility for multiprocessing

    print(colored(r"""
 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗     ██╗   ██╗ ██████╗    ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██║   ██║██╔═████╗   ╚════██╗
██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║    ██║   ██║██║██╔██║    █████╔╝
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ╚██╗ ██╔╝████╔╝██║    ╚═══██╗
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝     ╚████╔╝ ╚██████╔╝██╗██████╔╝
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝       ╚═══╝   ╚═════╝ ╚═╝╚═════╝ 
""", "yellow"))

    print(colored("input hash", "yellow"))
    hash_input = input(">")

    detected_type = detect_hash_type(hash_input)
    if not detected_type:
        print(colored("could not detect hash type", "red"))
        sleep(5)
        sys.exit(1)
    else:
        print(colored(f"detected hash type: {detected_type}", "green"))

    print(colored(r"""input preferred dataset, standard (1) or custom (2)
(standard dataset is comp of several existing wordlists, custom requires user configuration of customset.dat file)""", "yellow"))

    try:
        with open("vari.dat", "r") as vfile:
            variations = [line.strip() for line in vfile]
    except FileNotFoundError:
        print(colored("vari.dat not found", "red"))
        sleep(5)
        sys.exit(1)

    dataset = input(">")
    if dataset == "1":
        try:
            with open("standard.dat", "r", encoding="utf-8", errors="ignore") as passfile:
                run(passfile, variations, hash_input)
        except FileNotFoundError:
            print(colored("standard.dat not found.", "red"))
            sleep(5)
            sys.exit(1)
    elif dataset == "2":
        try:
            with open("customset.dat", "r", encoding="utf-8", errors="ignore") as passfile:
                run(passfile, variations, hash_input)
        except FileNotFoundError:
            print(colored("customset.dat not found.", "red"))
            sleep(5)
            sys.exit(1)
    else:
        print(colored("invalid option", "red"))
        sleep(5)
        sys.exit(1)
