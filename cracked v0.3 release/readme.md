# cracked v0.3

##### basic, lightweight python3 password cracker

## current features
- hash cracking (with wordlist), updated algo now checks variations of wordlist entries via vari.dat
- feature for wordlist selection (comes with basic 1.6 million entry wordlist from breaches and common password listings (standard.dat), supports custom wordlist with customset.dat)
- automatic hash algo detection and allocation

## usage
usage is straightforward and self-explanatory; just do what the program asks

to use the custom wordlist/dataset, you just need to paste your wordlist into the customset.dat file with the same formatting as the existing standard one, as you would for a .txt document

## requirements
- termcolor ("pip install termcolor" in terminal)

## currently supported hash algorithms
- sha-256
- sha-224
- sha1
- md5

(most commonly used algorithms)

note that program will be more efficient with a task-specific wordlist over the standard one or a generic one

## improvements (v0.2-v0.3)
- implemented afformentioned variation check mechanism
- implemented multiprocessing to accelerate execution rates (clears 165k hashes in <12s on Intel I5-10400F, which is 70% faster than v0.2)
- this build is also cross-platform

## future improvements (v0.4)
- will attempt to add a secondary bruteforce hash cracking function (not reliant on wordlist, but will be slower)
- will attempt to add GPU support to compensate for additional complexity
---
