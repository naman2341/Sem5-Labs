#ATM simulator Project
import Functions
import random
import time
import os
import sys

def Main():
    print("Welcome to ATM Simulator")
    Functions.read_csv1()
    Functions.Card_no_verification()
    Functions.Pin_verification()
    Functions.Account_type()
    # Functions.User_verification(card_no,pin)
    print("Login Successful")
    while True:
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change Pin")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Functions.Check_Balance()
        elif choice == 2:
            Functions.Withdraw()
        elif choice == 3:
            Functions.Deposit()
        elif choice == 4:
            Functions.Pin_change()
        elif choice == 5:
            Functions.Exit()
        else:
            print("Invalid Choice")



if __name__ == "__main__":
    Main()