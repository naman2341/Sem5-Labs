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

## Firewall Exploration Lab

### Task 1: Implementing a Simple Firewall

#### Task 1.A: Implement a Simple Kernel Module
```c
#include <linux/module.h>
#include <linux/kernel.h>

int initialization(void)
{
    printk(KERN_INFO "Hello World!\n");
    return 0;
}

void cleanup(void)
{
    printk(KERN_INFO "Bye-bye World!.\n");
}

module_init(initialization);
module_exit(cleanup);

MODULE_LICENSE("GPL");

```


```bash
$ make
$ sudo insmod hello.ko (inserting a module) $ lsmod | grep hello (list modules)
$ sudo rmmod hello
```
![](./SS/Task1/img1.jpg)


```bash
sudo dmesg -k -w
```
![](./SS/Task1/img2.jpg)



#### Task 1.B: Implement a Simple Firewall Using Netfilter
```bash
 dig @8.8.8.8 www.example.com
```
![](./SS/Task1.1/img1.jpg)

```bash
sudo dmesg -k -w
```

![](./SS/Task1.1/img2.jpg)

For seedFilter:

```bash
$ make
$ sudo insmod seedFilter.ko
$ lsmod | grep seedFilter
```
![](./SS/Task1.1/img3.jpg)

![](./SS/Task1.1/img4.jpg)

For seedPrint:

```bash
$ make
$ sudo insmod seedPrint.ko
$ lsmod | grep seedPrint
```
![](./SS/Task1.2/img1.jpg)

![](./SS/Task1.2/img2.jpg)


For seedBlock:

```bash
$ make
$ sudo insmod seedBlock.ko
$ lsmod | grep seedBlock
```
![](./SS/Task1.3/img1.jpg)

![](./SS/Task1.3/img2.jpg)


### Task 2: Experimenting with Stateless Firewall Rules
#### Task 2.A: Protecting the Router

```bash
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
iptables -A OUTPUT -p icmp --icmp-type echo-reply -j ACCEPT
iptables -P OUTPUT DROP
iptables -P INPUT DROP
iptables -t filter -L -n
```

```bash
ping seed-router
```

![](./SS/Task2A/img1.jpg)


```bash
telnet seed-router
```

![](./SS/Task2A/img2.jpg)


Questions:

1 .Can you ping the router

-> Yes, Pinging the router is possible


2 .Can you telnet into the router

-> No, Cannot telnet into the server, as it's stuck at 'Trying'


#### Task 2.B: Protecting the Internal Network

```bash
iptables -A FORWARD -i eth0 -p icmp --icmp-type echo-request -j DROP
iptables -A FORWARD -i eth1 -p icmp --icmp-type echo-request -j ACCEPT # iptables -A FORWARD -i eth0 -p icmp --icmp-type echo-reply -j ACCEPT
iptables -P FORWARD DROP
iptables -L -n -v
```

```bash
ping 192.168.60.5
ping seed-router
```

![](./SS/Task2B/img1.jpg)

```bash
ping 10.9.0.5
telnet 10.9.0.5
```
![](./SS/Task2B/img2.jpg)


#### Task 2.C: Protecting Internal Servers

```bash
iptables -A FORWARD -i eth0 -d 192.168.60.5 -p tcp --dport 23 -j ACCEPT # iptables -A FORWARD -i eth1 -s 192.168.60.5 -p tcp --sport 23 -j ACCEPT # iptables -P FORWARD DROP
iptables -L -n -v
```


In host1:

```bash
telnet 192.168.60.5
telnet 192.168.60.6
telnet 192.168.60.7
```

![](./SS/Task2C/img1.jpg)
![](./SS/Task2C/img2.jpg)
![](./SS/Task2C/img3.jpg)

In host2:

```bash
telnet 192.168.60.5
telnet 192.168.60.7
telnet 10.9.0.5
```

![](./SS/Task2C/img4.jpg)
![](./SS/Task2C/img5.jpg)
![](./SS/Task2C/img6.jpg)


Observation: 

```iptables -A FORWARD -i eth0 -d 192.168.60.5 -p tcp --dport 23 -j ACCEPT```
It accepts any tcp connection on the interface eth0 where the destination port is 23 and ip is 192.168.60.5

```iptables -A FORWARD -i eth1 -s 192.168.60.5 -p tcp --sport 23 -j ACCEPT```
It accepts any tcp connection on the interface eth1 where the source port is 23 and ip is 192.168.60.5


### Task 3: Connection Tracking and Stateful Firewall
#### Task 3.A: Experiment with the Connection Tracking

```bash
ping 192.168.60.5
conntrack -L
```

![](./SS/Task3/img1.jpg)

```bash
nc -l 9090
```

![](./SS/Task3/img2.jpg)


#### Task 3.B: Setting Up a Stateful Firewall

```bash
iptables -A FORWARD -p tcp -i eth0 -d 192.168.60.5 --dport 23 --syn -m conntrack --ctstate NEW -j ACCEPT
iptables -A FORWARD -i eth1 -p tcp --syn -m conntrack --ctstate NEW -j ACCEPT
iptables -A FORWARD -p tcp -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -p tcp -j DROP # iptables -P FORWARD ACCEPT
iptables -L -n -v
```

On host A:

```bash
telnet 192.168.60.5
telnet 192.168.60.6
telnet 192.168.60.7
```

![](./SS/Task3/img4.jpg)
![](./SS/Task3/img5.jpg)
![](./SS/Task3/img6.jpg)

On host 2:

```bash
telnet 192.168.60.5
telnet 192.168.60.7
telnet 10.9.0.5
```

![](./SS/Task3/img8.jpg)
![](./SS/Task3/img9.jpg)
![](./SS/Task3/img10.jpg)

Observation:

```iptables -A FORWARD -p tcp -i eth0 -d 192.168.60.5 --dport 23 --syn -m conntrack --ctstate NEW -j ACCEPT```


It accepts any tcp connection on the interface eth0 where the destination port is 23 and ip is 192.168.60.5 using the conntrack module


```iptables -A FORWARD -i eth1 -p tcp --syn -m conntrack --ctstate NEW -j ACCEPT```
It accepts connections on eth1 interface using the conntrack module


### Task 4: Limiting Network Traffic

```bash
iptables -A FORWARD -s 10.9.0.5 -m limit --limit 10/minute --limit-burst 5 -j ACCEPT
iptables -A FORWARD -s 10.9.0.5 -j DROP
iptables -L -n -v
```

```bash
ping 192.168.60.5
```

![](./SS/Task4/part1/img1.jpg)


```bash
iptables -A FORWARD -s 10.9.0.5 -m limit --limit 10/minute --limit-burst 5 -j ACCEPT
iptables -L -n -v
```

```bash
ping 192.168.60.5
```

![](./SS/Task4/part1/img2.jpg)

### Task 5: Load Balancing


```bash

iptables -t nat -A PREROUTING -p udp --dport 8080 -m statistic --mode nth --every 3 --packet 0 -j DNAT --to-destination 192.168.60.5:8080
iptables -t nat -A PREROUTING -p udp --dport 8080 -m statistic --mode nth --every 2 --packet 0 -j DNAT --to-destination 192.168.60.6:8080
iptables -t nat -A PREROUTING -p udp --dport 8080 -m statistic --mode nth --every 1 --packet 0 -j DNAT --to-destination 192.168.60.7:8080
iptables -L -n -v
```
On Host 1,2,3

```bash
nc -luk 8080
nc -luk 8080
nc -luk 8080
```

On Host A

```bash
nc -u 10.9.0.11 8080
< enter 3 words, wait 30 seconds before entering the next word>
```

![](./SS/Task5/img1.jpg)
![](./SS/Task5/img2.jpg)
![](./SS/Task5/img3.jpg)


**random mode**

```bash
iptables -t nat -A PREROUTING -p udp --dport 8080 -m statistic --mode random --probability 0.3333 -j DNAT --to-destination 192.168.60.5:8080
iptables -t nat -A PREROUTING -p udp --dport 8080 -m statistic --mode random --probability 0.5 -j DNAT --to-destination 192.168.60.6:8080
iptables -t nat -A PREROUTING -p udp --dport 8080 -m statistic --mode random --probability 1 -j DNAT --to-destination 192.168.60.6:8080
iptables -L -n -v

```

On Host 1,2,3

```bash
nc -luk 8080
nc -luk 8080
nc -luk 8080
```

On Host A

```bash
 nc -u 10.9.0.11 8080
< enter 3 words, wait 30 seconds before entering the next word>
```

![](./SS/Task5/img4.jpg)
![](./SS/Task5/img5.jpg)






