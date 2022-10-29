#!/usr/bin/env python3

from util import check_key_validity
f=open('new_encrypt.txt','r')
ciphertext=f.read()
f.close()

plaintext=''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key= input("Enter the key:")

if not check_key_validity(key,alphabet):
    print('Invalid key')
    exit(1)
else:
    for i in range(len(ciphertext)):
        if ciphertext[i] not in key:
            plaintext+=ciphertext[i]
        else:
            index_in_key=key.index(ciphertext[i])
            plaintext+=alphabet[index_in_key]
    print(plaintext)