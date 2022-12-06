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

## Heartbleed Attack Lab

### Step 1: Configure the DNS server for the Attacker machine

Adding the IP of victim in `/etc/hosts`

![](./SS/img1.png)


### Step 2: Lab Tasks


```bash
$ sudo chmod 777 attack.py
$ python attack.py www.heartbleedlabelgg.com
```

![](./SS/img2.png)

### Step 2: Explore the damage of the Heartbleed attack
Step 2(a): On the Victim Server: Login to `www.heartbleedlabelgg.com`
Step 2(b): On Attacker machine:

1) Find out the Username & Password

![](./SS/img3.png)

2) Find the exact content of the private message

![](./SS/img4.png)

### Step 3: Investigate the fundamental cause of the Heartbleed attack

```bash
$ python /home/seed/attack.py www.heartbleedlabelgg.com --length 40
```

![](./SS/img5.png)


### Step 4: Find out the boundary value of the payload length variable.

![](./SS/img6.png)