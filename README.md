# SPN_encryption_and_decryption

## This is my first coding challange using Python3 on a Ubuntu 17 machine.

### I have solved a task in cryptography where I have implemented a SPN algorithm.

### I took the design from [Wiki](https://en.wikipedia.org/wiki/Substitution%E2%80%93permutation_network).

### Git clone my repo and start using PyCharm CE or type those commands in terminal:

cd ~

cd Desktop

mkdir SPN

cd SPN 

git clone https://github.com/RobertSimion/SPN_encryption_and_decryption/

python3 main.py

### This code encrypt and decrypt a cleartext which consists in 4 bytes of data using 10 Rounds of sBox block,permutation and XOR operations, generating independent key for each Round.

####### The main part of algth. stands in main.py and the behavior of methos were built in SPN.py header(python3 file).

I've used list_to_string.py script for identifying the maps between sBox and invers sBox as well as generating the inverse permutation.
