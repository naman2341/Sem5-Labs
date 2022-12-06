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

## VPN Tunneling Lab

### Task 1: Network Setup


On Client-10.9.0.5

```bash
ping server-router
```

![](./SS/Task1/img1.jpg)

In router

```bash
ping 192.168.60.5
```

![](./SS/Task1/img2.jpg)

On Client-10.9.0.5

```bash
ping 192.168.60.5
```

![](./SS/Task1/img3.jpg)


```bash
tcpdump -i eth0 -n
```


```bash
ping server-router
```

![](./SS/Task1/img4.jpg)



### Task 2: Create and Configure TUN Interface

### Task 2.a: Name of the Interface

```bash
chmod a+x tun.py
./tun.py &
ip addr
```

![](./SS/T2a/img1.jpg)

Change tun to SRN

![](./SS/T2a/img2.jpg)

```bash
chmod a+x tun.py
./tun.py &
ip addr
```

![](./SS/T2a/img3.jpg)


### Task 2.b: Set up the TUN Interface

```bash
ip addr add 192.168.53.99/24 dev <SRN>0
ip link set dev <SRN>0 up
```

![](./SS/T2b/img1.jpg)


### Task 2.c: Read from the TUN Interface

Replace code :

```py
while True:
# Get a packet from the tun interface
	packet = os.read(tun, 2048)
	if packet:
		ip = IP(packet)
		print(ip.summary())

```

![](./SS/T2c/img1.jpg)

```bash
ip addr add 192.168.53.99/24 dev <SRN>0
ip link set dev <SRN>0 up
```

![](./SS/T2c/img2.jpg)

**Observation:** Yes, `ping 192.168.53.5` prints out `IP / ICMP 192.168.53.99 > 192.168.53.5 echo-request 0 / Raw`

No, `ping 192.168.60.5` loses all packets

### Task 2.d: Write to the TUN Interface

Change tun to SRN

![](./SS/T2d/img1.jpg)

```bash
chmod a+x tun.py
./tun1.py &
ip addr
```

![](./SS/T2d/img2.jpg)

```bash
ping 192.168.53.5
```

![](./SS/T2d/img3.jpg)


### Task 3: Send the IP Packet to VPN Server Through a Tunnel


Change tun to SRN

![](./SS/T3/img1.jpg)

```bash
chmod a+x tun_server.py
./tun_server.py
```

```bash
chmod a+x tun_client.py
./tun_client.py &
ip addr
```

![](./SS/T3/img2.jpg)

```bash
ping 192.168.53.5
ping 192.168.60.5
```

![](./SS/T3/img3.jpg)

```bash
 ip route
```

![](./SS/T3/img4.jpg)


### Task 4: Set Up the VPN Server

```bash
chmod a+x tun_server1.py
./tun_server1.py
```

```bash
ping 192.168.60.5
```

![](./SS/T4/img1.jpg)

```bash
tcpdump -i eth0 -n
```

![](./SS/T4/img2.jpg)


### Task 5: Handling Traffic in Both Directions

Change tun to SRN

![](./SS/T5/img1.jpg)

```bash
 chmod a+x tun_client_select.py
 ./tun_client_select.py
```

```bash
ping 192.168.60.5
```

![](./SS/T5/img2.jpg)

```bash
chmod a+x tun_server_select.py
./tun_server_select.py
```

![](./SS/T5/img4.jpg)

Wireshark:

![](./SS/T5/img3.jpg)

```bash
telnet 192.168.60.5
```

![](./SS/T5/img4.jpg)

Wireshark:

![](./SS/T5/img5.jpg)

### Task 6: Tunnel-Breaking Experiment

```bash
telnet 192.168.60.5
```

and then breaking the connection off [last 7 lines]

![](./SS/T5/img1.jpg)

Bringing connection back

```bash
./tun_server_select.py
```

![](./SS/T5/img2.jpg)
![](./SS/T5/img3.jpg)