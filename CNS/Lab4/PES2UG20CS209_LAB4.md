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

## Lab 4 - TCP Attack Lab

### Task 1: SYN Flooding Attack

**Command:** sysctl net.ipv4.tcp_max_syn_backlog

**Screenshots:**
![](SS/Task1/Task1.1/cmd1.jpg)

**Command:** 

sysctl net.ipv4.tcp_syncookies=0

netstat -tna

**Screenshots:**
![](SS/Task1/Task1.1/cmd2.jpg)

### Task 1.1: Launching the Attack Using Python


**Command:** python3 synflood.py

**Screenshots:**
![](SS/Task1/Task1.1/synflood1.jpg)
![](SS/Task1/Task1.1/synflood2.jpg)

**Command:** telnet 10.9.0.5

**Screenshots:**

Faliure
![](SS/Task1/Task1.1/failure.jpg)


Success
![](SS/Task1/Task1.1/attack_lanched.jpg)

### Task 1.2: Launching the Attack Using C


**Command:** 
 gcc -o synflood synflood.c
 
synflood 10.9.0.5 23

**Screenshots:**
![](SS/Task1/Task1.2/Task1.2.jpg)

### Task 1.3: Enable the SYN Cookie Countermeasure


**Command:** 
sysctl -w net.ipv4.tcp_syncookies=1

python3 synflood.py

**Screenshots:**
![](SS/Task1/Task1.3/cookie1.jpg)

**Command:** 
sysctl -w net.ipv4.tcp_syncookies=1

synflood 10.9.0.5 23

**Screenshots:**
![](SS/Task1/Task1.3/cookie2.jpg)

### Task 2: TCP RST Attacks on Telnet Connections

**Command:** 
telnet 10.9.0.5

**Wireshark Screenshots:**
![](SS/Task2/Toinputdata.jpg)

**Command:** 
python3 reset.py

**Screenshots:**
![](SS/Task2/attackprg.jpg)

**Wireshark Screenshots**
![](SS/Task2/rstsent.jpg)

reset flag sent

![](SS/Task2/rstaction.jpg)

Observation: The connection between host and victim is broken

#### Launching the attack automatically
**Wireshark Screenshots:**
![](SS/Task2/2wireshark.jpg)

**Command:** 
python3 reset_auto.py

**Screenshots:**
![](SS/Task2/2prg.jpg)

**Wireshark Screenshots:**
![](SS/Task2/2resetsuce.jpg)
Observation: A spam of reset flags is being sent to break the connection between host and victim

### Task 3: TCP Session Hijacking
**Command:**
On User 1 (remotely logged onto the Victim) $ cat > secret
(enter your desired text)

**Screenshots:**
![](SS/Task3/stp123.jpg)

**Command:** 
telnet 10.9.0.5

**Wireshark Screenshots:**
![](SS/Task3/hijacking.jpg)

**Command:** 
 nc -l 9090 & python3 hijack.py

**Screenshots:**
![](SS/Task3/secretreveal.jpg)
Observation: The secret stored in `secret` file has been revealed

```
Oh no, you have found the secret
```

**Wireshark Screenshots:**
![](SS/Task3/wiresharkreveal.jpg)

### Task 4:Creating Reverse Shell using TCP Session Hijacking

**Command:**
telnet 10.9.0.5

nc -l 9090 & python3 reverse.py

**Screenshots:**
![](SS/Task4/4_1redo.jpg)

**Wireshark Screenshots:**
![](SS/Task4/4_2redo.jpg)

Attack successful