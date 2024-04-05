# cracked v0.2

##### basic, lightweight python3 password cracker

## current features
- hash cracking (with wordlist)
- feature for wordlist selection (comes with basic 1.6 million entry wordlist from breaches and common password listings (standard.dat), supports custom wordlist with customset.dat)

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

## notes
- windows version works, mac & linux should work but aren't tested (main factor is termcolor)

- program will be more efficient with a task-specific wordlist over the standard one or a generic one

- in future, i will attempt to add a function that automatically checks combinations of the contents of the wordlist

- i will also be adding more options/functions at some point, likely as i see fit for my own requirements
### important side note
- this is a project from october 2023 that i forgor to post so obviously i won't frequently update and idgaf about licence for this build

---
