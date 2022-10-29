#! /usr/bin/env python

f=open('new_text.txt','r')
plaintext=f.read()
f.close()

ciphertext=''

alphabet='abcdefghijklmnopqrstuvwxyz'
key='sadnmevjufzckptihqbrlxogwy'

for i in range(len(plaintext)):
    if plaintext[i] not in alphabet:
        ciphertext+=plaintext[i]
    else:
        index_in_alphabet=alphabet.index(plaintext[i])
        ciphertext+=key[index_in_alphabet]
    
print(ciphertext)