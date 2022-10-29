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

## Remote DNS Attack Lab

### Task 0:

```
dig ns.attacker32.com
```
![](./SS/img1.jpg)


```
dig www.example.com
dig @ns.attacker32.com www.example.com
```
![](./SS/img2.jpg)

### Task 1: Construct DNS request

```
python3 generate_dns_query.py
```

![](./SS/img3.jpg)


### Task 2: Spoof DNS Replies

```
dig NS example.com
dig +short a [example.com name server’s name]
```

![](./SS/img4.jpg)

```
python3 generate_dns_reply.py
```

![](./SS/img5.jpg)

Wireshark:
![](./SS/img6.jpg)

Observation: Spoofed DNS packets observed

### Task 3: Launch the Kaminsky Attack

```
gcc -o kaminsky attack.c
./kaminsky
```

![](./SS/img7.jpg)

```
rndc dumpdb -cache && grep attacker /var/cache/bind/dump.db
```

![](./SS/img8.jpg)

Observation: Spoofed nameserver appears in the dump

### Task 4: Result Verification 

```
dig www.example.com
```
![](./SS/img9.jpg)


```
dig @ns.attacker32.com www.example.com
```
![](./SS/img10.jpg)


Wireshark:

![](./SS/img11.jpg)
![](./SS/img12.jpg)

Observation: The attack was successful because we ran the Kaminsky attack, where the NameServer is spoofed from an external DNS source