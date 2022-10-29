#Caesar Cipher
#Example Plain Text: CRYPTOGRAPHY
#Key:10

def encrypt():
    plain=input("Enter the plain text to encrypt ")
    key=int(input("Enter the KEY "))
    lst=[]
    for i in plain:
        i=ord(i)-65
        i=(i+key)%26
        i=i+65
        lst.append(chr(i))
    str=''
    return(str.join(lst))

def decrypt():
    cipher=input("Enter the plain text to decrypt ")
    key=int(input("Enter the KEY "))
    lst=[]
    for i in cipher:
        i=ord(i)-65
        i=(i-key)%26
        i=i+65
        lst.append(chr(i))
    str=''
    return(str.join(lst))

print("Caesar Cipher")
op=int(input("Choose one of the options:\n1.Encrypt\n2.Decrypt\n"))
if op==1:
    print(encrypt())
else:
    print(decrypt())