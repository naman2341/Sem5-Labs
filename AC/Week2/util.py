#! /usr/bin/env python3

def check_key_validity(key,alphabet):
    if len(key) != len(alphabet):
        return False
    if len(list(key)) != len(set(key)):
        return  False
    return True

def generate_key(alphabet_string):
    import random as r
    l = list(alphabet_string)
    r.shuffle(l)
    return ''.join(l)