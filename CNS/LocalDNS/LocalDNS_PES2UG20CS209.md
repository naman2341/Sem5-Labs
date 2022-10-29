# Computer Network Security

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

## Local DNS Attack Lab

### Task 0:Verification of the DNS setup

```
 dig ns.attacker32.com 
```
![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img1.jpg)

```
dig www.example.com
dig @ns.attacker32.com www.example.com
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img2.jpg)
![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img3.jpg)

### Task 1: Directly Spoffing Response to User

```
dig www.example.com
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img4.jpg)

```
python3 task1.py
```
```
dig www.example.com
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img5.jpg)

Wireshark:

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img6.jpg)

```
rndc dumpdb -cache
cat /var/cache/bind/dump.db | grep example
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img7.jpg)

Observation: When we see the contents of the dump file, we notice that the response is being spoofed to a random ip address

### Task 2: DNS Cache Poisoning Attack – Spoofing Answers

```
python3 task2.py
```
```
dig www.example.com
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img8.jpg)

Wireshark:


![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img9.jpg)

```
rndc dumpdb -cache
cat /var/cache/bind/dump.db | grep example
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img10.jpg)

Observation: We observe that a new entry was created because of `task2.py`


### Task 3: Spoofing NS Records

```
python3 task3.py
```
```
dig www.example.com
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img11.jpg)

Wireshark:


![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img12.jpg)

```
dig www.example.com
dig ftp.example.com
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img13.jpg)

```
rndc dumpdb -cache
cat /var/cache/bind/dump.db | grep example
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img14.jpg)

Observation: The spoofing of the packed has been reflected in the dump file

### Task 4: Spoofing NS Records for Another Domain

```
python3 task3.py
```
```
dig www.example.com
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img15.jpg)

Wireshark:

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img16.jpg)

```
rndc dumpdb -cache
cat /var/cache/bind/dump.db | grep example
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img17.jpg)

Observation: ns attacker now becomes the default nameserver due to entries in authority section

### Task 5: Spoofing Records in the Additional Section 

```
python3 task3.py
```
```
dig www.example.com
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img18.jpg)

Wireshark:

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img19.jpg)

```
rndc dumpdb -cache
cat /var/cache/bind/dump.db | grep example
```

![](/Users/naman2341/Documents/Sem5/Labs/CNS/LocalDNS/img20.jpg)

Observation: attack successful on the default nameserver due to entries in additional section

