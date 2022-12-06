# Applied Cryptography

<table style="width:100%">
  <tr>
    <th align="left">Name</th>
    <td>Naman Choudhary</td>
  </tr>
  <tr>
    <th align="left">SRN</th>
    <td>PES2UG20CS209</td>
  </tr>
  <tr>
    <th align="left">Section</th>
    <td>D</td>
  </tr>
</table>

## Hash Length Extension Attack Lab

## Lab Setup

Setting up the hostname
![](./SS/Task1/img1.jpg)

The server program
![](./SS/Task1/img2.jpg)
![](./SS/Task1/img3.jpg)


## Task 1:Send Request to List Files

Calculating the MAC address

![](./SS/Task1/img4.jpg)

Result on the website

![](./SS/Task1/img5.jpg)

When an invalid MAC is given

![](./SS/Task1/img6.jpg)

Contents of secret.txt

![](./SS/Task1/img7.jpg)

Contents of key.txt

![](./SS/Task1/img8.jpg)

## Task 2:Create Padding

![](./SS/Task2/img1.jpg)

## Task 3:Compute MAC using Secret Key

```c
/* calculate_mac.c */
#include <stdio.h>
#include <openssl/sha.h>
int main(int argc, const char *argv[])
{
   SHA256_CTX c;
   unsigned char buffer[SHA256_DIGEST_LENGTH];
   int i;
   SHA256_Init(&c);
SHA256_Update(&c,
   "This is a test message"
   "\x80"
   "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
   "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
   "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00"
   "\x00\x00\x00\x00\x00\x00\x00\xB0"
   "Extra message",
   64+13);
SHA256_Final(buffer, &c);
for(i = 0; i < 32; i++) {
     printf("%02x", buffer[i]);
   }
   printf("\n");
   return 0;
}
```

Using Python to create padding

![](./SS/Task3/img1.jpg)

Website ouput

![](./SS/Task3/img2.jpg)

## Task 4:Length Extension Attack

![](./SS/Task4/img1.jpg)

Website output

![](./SS/Task4/img2.jpg)

## Task 5:Attack Mitigation using HMAC

Using Python to calculate HMAC

![](./SS/Task5/img1.jpg)
