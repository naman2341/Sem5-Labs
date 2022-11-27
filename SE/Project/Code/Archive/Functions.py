import math
from pandas import *
# Create an Atm Simulator in python
# card_no = input("Enter your card number: ")
# pin = input("Enter your pin: ")
# global card_nos,pins,Balance

card_nos=list()
pins=list()
Balances=list()
user_index=-1
Account_Types=['Savings','Current']
acc_choice = 0
# #Read the file from csv
# def read_csv():
#     global card_nos,pins,Balance
#     with open("ATM.csv","r") as f:
#         csvFile = csv.reader(f)
#         for row in csvFile:

def read_csv1():
    global card_nos,pins,Balances,Account_Types
    data = read_csv("./ATM.csv",sep="\t") #,usecols = ['card_nos','pins','Balance','Account_Type'])
    #int of data to list
    card_nos = data["card_nos"].tolist()
    list(map(int, card_nos))
    # card_nos = [eval(i) for i in card_nos]
    pins = data["pins"].tolist()
    list(map(int, pins))
    # pins = [eval(i) for i in pins]
    Balances = data["Balance"].tolist()
    list(map(int, Balances))
    # Balance = [eval(i) for i in Balance]

 
def Card_search(card_no):
    global user_index
    for i in range(len(card_nos)):
        if card_no == card_nos[i]:
            user_index = i
            return True
    print("Card Number not found")
    return False

def Card_no_verification():
    n =0
    while(n<3):
        card_no=int("Enter your card number: ")
        if not (card_no>99999999 and card_no<=999999999): #Make it !=
            print("Card No should be 9 digits, Try again\n")
            n+=1
        elif Card_search(card_no):
            print("Card Number Verified\n")
            return card_no
    else:
        print("Limits Exceeded, Try Again Later")
        Exit()
        

def Pin_verification():
    print("Pin Verification")
    n = 0
    while(n<3):
        pin = input("Enter your pin: ")
        if len(pin) != 4:
            print("Pin should be 4 digits, Try again")
            n+=1
        elif int(pin) == pins[user_index]:
            print("Pin Verified\n")
            return True
    else:
        print("Limits Exceeded, Try Again Later")
        Exit()
   

def User_verification(card_no,pin):
    if Card_no_verification() and Pin_verification():
        print("User Verified\n")
        return True
    else:
        print("User Not Verified\n")
        return False
# def Account_balance():
#      print("Your Account Balance is: ",Balance[0])

def Account_type():
    global acc_choice
    print("Select your Account Type: ")
    for i in range(len(Account_Types)):
        print(i+1,Account_Types[i])
    acc_choice = int(input("Enter your choice: "))
    if acc_choice == 1:
        print("You have selected Savings Account")
    elif acc_choice == 2:
        print("You have selected Current Account")
    else:
        print("Invalid Choice")
        Account_type()

def Withdraw():
    global Balances
    global acc_choice
    global user_index
    Balance=Balances[user_index]
    amount = int(input("Enter the amount to be withdrawn: "))
    invalid=False
    if acc_choice == 1:
        if amount > 15000:
            invalid=True
            print("You can only withdraw 15000 at a time from Savings Account\n\n")
            Withdraw_exit()
            return
    elif acc_choice == 2:
        if amount > 100000:
            invalid=True
            print("You can only withdraw 100000 at a time from Current Account\n\n")
            Withdraw_exit()
            return
    if amount > Balance and invalid==False:
        print("Insufficient Balance")
    elif invalid == False:
        Balance = Balance - amount
        Balances[user_index]=Balance
        print("Withdrawal Successful")
        print("Your Account Balance is: ",Balance)
    Balances[user_index]=Balance

def Withdraw_exit():
    print("Do you want to withdraw a new amount?")
    print("1. Yes")
    print("2. No")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Withdraw()
    elif choice == 2:
        Exit()

def Deposit():
    global Balances
    global user_index
    Balance=Balances[user_index]
    amount = int(input("Enter the amount to be deposited: "))
    Balance = Balance + amount
    print("Deposit Successful")
    print("Your Account Balance is: ",Balance)
    Balances[user_index]=Balance

def Check_Balance():
    Balance=Balances[user_index]
    print("Your Account Balance is: ",Balance)

def Pin_change():
    global pins
    pin=pins[user_index]
    old_pin = int(input("Enter your old pin: "))
    if old_pin == pin:
        new_pin = int(input("Enter your new pin: "))
        if not(new_pin>999 and new_pin<=9999):
            print("Pin should be 4 digits")
        else:
            pin = new_pin
            print("Pin Changed Successfully")
    else:
        print("Incorrect Pin")
    pins[user_index]=pin

def write_csv():
    global card_nos,pins,Balances
    data = {"card_nos":card_nos,"pins":pins,"Balance":Balances}
    df = DataFrame(data,columns=["card_nos","pins","Balance"])
    df.to_csv("ATM.csv",sep="\t",index=False)

def Exit():
    write_csv()
    print("Thank You for using our ATM")
    exit()


# card_no = str(input("Enter your card number: "))
# Card_no_verification(card_no)
# pin = str(input("Enter your pin: "))
# Pin_verification(pin)
# User_verification(card_no,pin)



# def login(card_no,pin):
#     n = 0
    
     
            
            
            
#             print("Login Successful")
#             return True
#             n+=1
#         else:
#             print("Login Failed")
#             return False
#             n+=1

# class Atm:
#     def __init__(self,card_no,pin):
#         self.card_no = card_no
#         self.pin = pin
#         self.balance = Balance
#         self.card_nos = card_nos
#         self.pins = pins
#     def check_balance(self):
#         print("Your current balance is: ",self.balance)
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount
#             print("Withdrawal Successful, Your current balance is: ",self.balance)
#     def deposit(self,amount):
#         self.balance += amount
#         print("Deposit Successful, Your current balance is: ",self.balance)
#     def change_pin(self,new_pin):
#         self.pins = new_pin
#         print("Pin Changed Successfully")
#     def change_card_no(self,new_card_no):
#         self.card_nos = new_card_no
#         print("Card No Changed Successfully")
