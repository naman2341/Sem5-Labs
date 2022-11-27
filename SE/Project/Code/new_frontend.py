from tkinter import *
import tkinter.messagebox
import tkinter.font as font         # imports font module and being imported as font. It helps to define a specific font style
import random
from tkinter import ttk
import Functions
from pandas import *

 # Themes: blue (default), dark-blue, green
win = tkinter.Tk()  # create CTk window like you do with the Tk window                         # creates the window
win.title('ATM')
win.geometry('500x500')             # sets the dimension of the window

tim40 = font.Font(family='IBM plex mono', size=40, weight='bold')      # Font is an instance which contains parameter as
                                                                                            # family(the font style), size, weight(bold,normal)
                                                                                            # slant(italic,roman(non-italic)), underline(1-yes,0-no),
                                                                                            # overstrike(1-yes,0-no) and many more
cour20 = font.Font(family='IBM plex mono', size=20, weight='bold')
cour15 = font.Font(family='IBM plex mono', size=15, weight='bold')

glob_count = 0                      # this is used to access balance_func() after press yes in question_func()

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
    print(card_nos)
    print(type(card_nos[0]))
    print(type(card_no))
    for i in range(len(card_nos)):
        if card_no == str(card_nos[i]):
            user_index = i
            return True
        else:
            print("Card Number not found")
            return False

def Card_no_verification(card_no):
    if (len(card_no)!=9): #Make it !=
        print("Card No should be 9 digits, Try again\n")
        return False
    elif Card_search(card_no):
        print("Card Number Verified\n")
        return True
    else:
        print("Limits Exceeded, Try Again Later")
        return False

# displays message after selecting no in question_func()
def display_func():

    question_func.question_win.withdraw()
    display_win = Toplevel(win)
    display_win.geometry('500x500')
    message = Message(display_win, text='\n\nYour transaction has been successful\n\nThank you for using our', font=cour20, fg='grey')
    message.pack()
    text = Label(display_win, text='ATM', font=tim40, fg='black')
    text.pack()

    exit_button = Button(display_win, text='EXIT', font=cour15,fg='white',bg='black', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)


# window asking whether to show balance or not
def question_func():

    global glob_count
    glob_count+=1

    withdrawal_func_current.withdrawal_win.withdraw()
    question_func.question_win = Toplevel(win)
    question_func.question_win.geometry('500x500')

    bf = Frame(question_func.question_win)
    bf.pack(side=BOTTOM)

    msg_box = Message(question_func.question_win, text='\nYour transaction has been successful\n\nPlease collect your money\n\nYou can remove your card\n\nDo you want to check your balance?', font=cour20, fg='grey')
    msg_box.pack()

    yes_btn = Button(bf, text='YES', font=cour15, fg='white',bg='black',command=balance_func_savings)
    yes_btn.pack(side=LEFT, pady=10)

    no_btn = Button(bf, text=' NO ', font=cour15,fg='white',bg='black',command=display_func)
    no_btn.pack(pady=10, padx=10)


# withdrawing money window
def withdrawal_func_savings():

    option_func_savings.option_win.withdraw()
    withdrawal_func_savings.withdrawal_win = Toplevel(win)
    withdrawal_func_savings.withdrawal_win.geometry('500x500')

    def withdraw():
        withdraw_amt = money_entry.get()
        print(user_index)
        balance = Functions.Check_Balance(user_index, Balances) 
        check = Functions.Withdraw_savings(withdraw_amt, balance, user_index)
        if check==2:
            error_msg = Label(withdrawal_func_savings.withdrawal_win,text="Savings acccount limit crossed = 150000", font=cour15, fg='red')
            error_msg.pack()
        elif check==3:
            error_msg = Label(withdrawal_func_savings.withdrawal_win,text="Balance insufficient", font=cour15, fg='red')
            error_msg.pack()
        else:
            error_msg = Label(withdrawal_func_savings.withdrawal_win,text="Money Withdrawn Successfully!", font=cour15, fg='red')
            error_msg.pack()
            balance = check
            question_func()
   
    enter_lbl = Label(withdrawal_func_savings.withdrawal_win, text='\nPlease enter amount\n', font=cour20, fg='black')
    enter_lbl.pack()
    global money_entry
    money_entry = Entry(withdrawal_func_savings.withdrawal_win, font=cour15, justify='center')
    money_entry.pack()

    bf = Frame(withdrawal_func_savings.withdrawal_win)
    bf.pack(side=BOTTOM)

    bf4 = Frame(withdrawal_func_savings.withdrawal_win)
    bf4.pack(side=BOTTOM)

    bf3 = Frame(withdrawal_func_savings.withdrawal_win)
    bf3.pack(side=BOTTOM)

    bf3 = Frame(withdrawal_func_savings.withdrawal_win)
    bf3.pack(side=BOTTOM)

    bf2 = Frame(withdrawal_func_savings.withdrawal_win)
    bf2.pack(side=BOTTOM)

    bf1 = Frame(withdrawal_func_savings.withdrawal_win)
    bf1.pack(side=BOTTOM)
    
    b1 = Button(bf1, text='1', font=cour15, bg='black',fg='white',command=lambda: money_entry.insert('end', '1'))
    b1.pack(side=LEFT, pady=10)

    b2 = Button(bf1, text='2', font=cour15,bg='black',fg='white',command=lambda: money_entry.insert('end', '2'))
    b2.pack(side=LEFT, padx=10)

    b3 = Button(bf1, text='3', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '3'))
    b3.pack(side=LEFT)

    b4 = Button(bf2, text='4', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '4'))
    b4.pack(side=LEFT)

    b5 = Button(bf2, text='5', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '5'))
    b5.pack(side=LEFT, padx=10)

    b6 = Button(bf2, text='6', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '6'))
    b6.pack(side=LEFT)

    b7 = Button(bf3, text='7', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '7'))
    b7.pack(side=LEFT, pady=10)

    b8 = Button(bf3, text='8', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '8'))
    b8.pack(side=LEFT, padx=10)

    b9 = Button(bf3, text='9', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '9'))
    b9.pack(side=LEFT)

    #btn = Button(bf4, text=' ', font=cour15)
    #btn.pack(side=LEFT)

    b0 = Button(bf4, text='0', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '0'))
    b0.pack(side=LEFT, padx=10)

    #btn_ = Button(bf4, text=' ', font=cour15)
    #btn_.pack(side=LEFT)

    enter_btn = Button(bf, text='ENTER', font=cour15,fg='white',bg='black', command=withdraw)
    enter_btn.pack(side=LEFT, pady=10)

    clear_btn = Button(bf, text='CLEAR', font=cour15,fg='white',bg='black', command=lambda: money_entry.delete(1))
    clear_btn.pack(side=LEFT, padx=10)

def withdrawal_func_current():

    option_func_current.option_win.withdraw()
    withdrawal_func_current.withdrawal_win = Toplevel(win)
    withdrawal_func_current.withdrawal_win.geometry('500x500')

    def withdraw():
        withdraw_amt = money_entry.get()
        print(user_index)
        balance = Functions.Check_Balance(user_index, Balances) 
        check = Functions.Withdraw_savings(withdraw_amt, balance, user_index)
        if check==2:
            error_msg = Label(withdrawal_func_current.withdrawal_win,text="Savings acccount limit crossed = 150000", font=cour15, fg='red')
            error_msg.pack()
        elif check==3:
            error_msg = Label(withdrawal_func_current.withdrawal_win,text="Balance insufficient", font=cour15, fg='red')
            error_msg.pack()
        else:
            error_msg = Label(withdrawal_func_current.withdrawal_win,text="Money Withdrawn Successfully!", font=cour15, fg='red')
            error_msg.pack()
            balance = check
            question_func()
   
    enter_lbl = Label(withdrawal_func_current.withdrawal_win, text='\nPlease enter amount\n', font=cour20, fg='black')
    enter_lbl.pack()
    global money_entry
    money_entry = Entry(withdrawal_func_current.withdrawal_win, font=cour15, justify='center')
    money_entry.pack()

    bf = Frame(withdrawal_func_current.withdrawal_win)
    bf.pack(side=BOTTOM)

    bf4 = Frame(withdrawal_func_current.withdrawal_win)
    bf4.pack(side=BOTTOM)

    bf3 = Frame(withdrawal_func_current.withdrawal_win)
    bf3.pack(side=BOTTOM)

    bf3 = Frame(withdrawal_func_current.withdrawal_win)
    bf3.pack(side=BOTTOM)

    bf2 = Frame(withdrawal_func_current.withdrawal_win)
    bf2.pack(side=BOTTOM)

    bf1 = Frame(withdrawal_func_current.withdrawal_win)
    bf1.pack(side=BOTTOM)
    
    b1 = Button(bf1, text='1', font=cour15, bg='black',fg='white',command=lambda: money_entry.insert('end', '1'))
    b1.pack(side=LEFT, pady=10)

    b2 = Button(bf1, text='2', font=cour15,bg='black',fg='white',command=lambda: money_entry.insert('end', '2'))
    b2.pack(side=LEFT, padx=10)

    b3 = Button(bf1, text='3', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '3'))
    b3.pack(side=LEFT)

    b4 = Button(bf2, text='4', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '4'))
    b4.pack(side=LEFT)

    b5 = Button(bf2, text='5', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '5'))
    b5.pack(side=LEFT, padx=10)

    b6 = Button(bf2, text='6', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '6'))
    b6.pack(side=LEFT)

    b7 = Button(bf3, text='7', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '7'))
    b7.pack(side=LEFT, pady=10)

    b8 = Button(bf3, text='8', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '8'))
    b8.pack(side=LEFT, padx=10)

    b9 = Button(bf3, text='9', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '9'))
    b9.pack(side=LEFT)

    #btn = Button(bf4, text=' ', font=cour15)
    #btn.pack(side=LEFT)

    b0 = Button(bf4, text='0', font=cour15,bg='black',fg='white', command=lambda: money_entry.insert('end', '0'))
    b0.pack(side=LEFT, padx=10)

    #btn_ = Button(bf4, text=' ', font=cour15)
    #btn_.pack(side=LEFT)

    enter_btn = Button(bf, text='ENTER', font=cour15,fg='white',bg='black', command=withdraw)
    enter_btn.pack(side=LEFT, pady=10)

    clear_btn = Button(bf, text='CLEAR', font=cour15,fg='white',bg='black', command=lambda: money_entry.delete(1))
    clear_btn.pack(side=LEFT, padx=10)



# balance displaying window
def balance_func_savings():
    read_csv1()
    global glob_count

    if glob_count == 1:
        question_func.question_win.withdraw()

    option_func_savings.option_win_.withdraw()
    balance_win = Toplevel(win)
    balance_win.geometry('500x500')
    #balance_win.grab_set()
    print(user_index)
    global balance
    balance = Functions.Check_Balance(user_index, Balances)
    message = Message(balance_win,text='\nYour transaction is successful\n\nAvailable Balance: '+str(balance)+'\n\nThank you for using our', font=cour20, fg='grey')
    message.pack()
    text = Label(balance_win, text='ATM', font=tim40, fg='black')
    text.pack()

    exit_button = Button(balance_win, text='EXIT', font=cour15, fg='white',bg='black', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)

def balance_func_current():
    read_csv1()
    global glob_count

    if glob_count == 1:
        question_func.question_win.withdraw()

    option_func_current.option_win.withdraw()
    balance_win = Toplevel(win)
    balance_win.geometry('500x500')
    #balance_win.grab_set()
    print(user_index)
    global balance
    balance = Functions.Check_Balance(user_index, Balances)
    message = Message(balance_win,text='\nYour transaction is successful\n\nAvailable Balance: '+str(balance)+'\n\nThank you for using our', font=cour20, fg='grey')
    message.pack()
    text = Label(balance_win, text='ATM', font=tim40, fg='black')
    text.pack()

    exit_button = Button(balance_win, text='EXIT', font=cour15, fg='white',bg='black', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)


# displays message after change has been changed
def pin_message_func():
    change_pin_func.change_pin_win.withdraw()
    win2 = Toplevel(win)
    win2.geometry('500x500')
    message = Message(win2, text='\n\nYour PIN has been successfully changed\n\nThank you for using our', font=cour20, fg='grey')
    message.pack()
    text = Label(win2, text='ATM', font=tim40, fg='black')
    text.pack()

    exit_button = Button(win2, text='EXIT', font=cour15, fg='white',bg='black', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)


# changing pin function
def change_pin_func():
    option_func_savings.option_win.withdraw()
    change_pin_func.change_pin_win = Toplevel(win)
    change_pin_func.change_pin_win.geometry('500x500')

    def check_new_pin():
        pin = entry_box.get()
        print(user_index)
        check = Functions.Pin_change(pin, user_index)
        if check:
            error_msg = Label(change_pin_func.change_pin_win,text="Pin Changed Successfully!", font=cour15, fg='red')
            error_msg.pack()
            pin_message_func
        else:
            error_msg = Label(change_pin_func.change_pin_win,text="Error! Re-enter pin", font=cour15, fg='red')
            error_msg.pack()

    pin_lbl = Label(change_pin_func.change_pin_win, text='\nEnter new-PIN', font=cour15, fg='black')
    pin_lbl.pack()
    global pin_entry
    pin_entry = Entry(change_pin_func.change_pin_win, font=cour15,justify='center', show='*')
    pin_entry.pack()
    re_entry_lbl = Label(change_pin_func.change_pin_win, text='\nRe-enter new-PIN\n', font=cour15, fg='black')
    re_entry_lbl.pack()
    
    re_entry = Entry(change_pin_func.change_pin_win, font=cour15, justify='center', show='*')
    re_entry.pack()
    bf = Frame(change_pin_func.change_pin_win)
    bf.pack(side=BOTTOM)

    bf4 = Frame(change_pin_func.change_pin_win)
    bf4.pack(side=BOTTOM)

    bf3 = Frame(change_pin_func.change_pin_win)
    bf3.pack(side=BOTTOM)

    bf3 = Frame(change_pin_func.change_pin_win)
    bf3.pack(side=BOTTOM)

    bf2 = Frame(change_pin_func.change_pin_win)
    bf2.pack(side=BOTTOM)

    bf1 = Frame(change_pin_func.change_pin_win)
    bf1.pack(side=BOTTOM)
    b1 = Button(bf1, text='1', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','1'), re_entry.insert('end','1')])
    b1.pack(side=LEFT,pady=10)

    b2 = Button(bf1, text='2', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','2'), re_entry.insert('end','2')])
    b2.pack(side=LEFT, padx=10)

    b3 = Button(bf1, text='3', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','3'), re_entry.insert('end','3')])
    b3.pack(side=LEFT)

    b4 = Button(bf2, text='4', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','4'), re_entry.insert('end','4')])
    b4.pack(side=LEFT)

    b5 = Button(bf2, text='5', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','5'), re_entry.insert('end','5')])
    b5.pack(side=LEFT, padx=10)

    b6 = Button(bf2, text='6', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','6'), re_entry.insert('end','6')])
    b6.pack(side=LEFT)

    b7 = Button(bf3, text='7', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','7'), re_entry.insert('end','7')])
    b7.pack(side=LEFT,pady=10)

    b8 = Button(bf3, text='8', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','8'), re_entry.insert('end','8')])
    b8.pack(side=LEFT, padx=10)

    b9 = Button(bf3, text='9', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','9'), re_entry.insert('end','9')])
    b9.pack(side=LEFT)

    #btn = Button(bf4, text=' ', font=cour15)
    #btn.pack(side=LEFT)

    b0 = Button(bf4, text='0', font=cour15,bg='black',fg='white', command=lambda: [pin_entry.insert('end','0'), re_entry.insert('end','0')])
    b0.pack(side=LEFT, padx=10)                         # with help of list we can assign multiple functions for buttons

    #btn_ = Button(bf4, text=' ',font=cour15)
    #btn_.pack(side=LEFT)

    enter_btn = Button(bf, text='ENTER', font=cour15,fg='white',bg='black', command=check_new_pin )
    enter_btn.pack(side=LEFT, pady=10)

    clear_btn = Button(bf, text='CLEAR', font=cour15,fg='white',bg='black', command=lambda: [pin_entry.delete(0), re_entry.delete(0)])
    clear_btn.pack(side=LEFT, padx=10)


# options window
def option_func_savings():
    acctype.acctype_win.withdraw()                # check enter_pin() function for the functionality of .withdraw()
    option_func_savings.option_win = Toplevel(win)
    option_func_savings.option_win.geometry('460x390')
   # option_win.grab_set()                       ## check enter_pin() function for the functionality of .grab_set()

    text_title = Label(option_func_savings.option_win, text='\nATM', font=tim40)
    text_title.pack()

    rf = Frame(option_func_savings.option_win)          #right frame
    rf.pack(side=RIGHT)

    lf = Frame(option_func_savings.option_win)          #left frame
    lf.pack(side=LEFT)

    withdrawal_btn = Button(rf, text=' WITHDRAWAL ', font=cour15, fg='white',bg='black', command=withdrawal_func_current)
    withdrawal_btn.pack(padx=40, pady=10)

    balance_btn = Button(rf, text='BALANCE INQ', font=cour15,fg='white',bg='black', command=balance_func_savings)
    balance_btn.pack(padx=40, pady=10)

    change_pin_btn = Button(lf, text='CHANGE PIN', font=cour15,fg='white',bg='black', command=change_pin_func)
    change_pin_btn.pack(padx=40, pady=10)

    exit_btn = Button(lf, text='   EXIT   ', font=cour15, fg='white',bg='black', command=lambda: [option_func_savings.option_win.destroy(), enter_pin.new_win.deiconify()])
    exit_btn.pack(padx=40, pady=10)                                                                         # check enter_pin() function for the functionality of .deiconify()

# options window
def option_func_current():
    acctype.acctype_win.withdraw()                # check enter_pin() function for the functionality of .withdraw()
    option_func_current.option_win = Toplevel(win)
    option_func_current.option_win.geometry('460x390')
   # option_win.grab_set()                       ## check enter_pin() function for the functionality of .grab_set()

    text_title = Label(option_func_current.option_win, text='\nATM', font=tim40)
    text_title.pack()

    rf = Frame(option_func_current.option_win)          #right frame
    rf.pack(side=RIGHT)

    lf = Frame(option_func_current.option_win)          #left frame
    lf.pack(side=LEFT)

    withdrawal_btn = Button(rf, text=' WITHDRAWAL ', font=cour15, fg='white',bg='black', command=withdrawal_func_current)
    withdrawal_btn.pack(padx=40, pady=10)

    balance_btn = Button(rf, text='BALANCE INQ', font=cour15,fg='white',bg='black', command=balance_func_current)
    balance_btn.pack(padx=40, pady=10)

    change_pin_btn = Button(lf, text='CHANGE PIN', font=cour15,fg='white',bg='black', command=change_pin_func)
    change_pin_btn.pack(padx=40, pady=10)

    exit_btn = Button(lf, text='   EXIT   ', font=cour15, fg='white',bg='black', command=lambda: [option_func_current.option_win.destroy(), enter_pin.new_win.deiconify()])
    exit_btn.pack(padx=40, pady=10)    

# enter_pin window
def enter_pin(card_no):

    win.withdraw()                              # .withdraw() hides or make the associated window invisible until (.deiconify()) appears

    enter_pin.new_win = Toplevel(win)           # enter_pin.new_win makes the variable new_win as the member of the function object
    enter_pin.new_win.geometry('460x390')       # this helps us to use the variable even outside the function

    #enter_pin.new_win.grab_set()               ## .grab.set() makes the associated window inactive temporarily until the active window is working


    def setInputText(text):
        entry_box.insert('end',text)            # insert allows to enter(display on entry box) the text at the end(if we replace end with 0 the text is placed at front)

    def text_delete():
        entry_box.delete(0)                     # we have another function called delete which deletes text for the given range(.delete(0,'end') deletes the entire text

    def check_pin():
        pin = entry_box.get()
        print(user_index)
        check = Functions.Pin_verification(pin, user_index)
        if check:
            error_msg = Label(enter_pin.new_win,text="Correct Pin!", font=cour15, fg='red')
            error_msg.pack()
            acctype()
        else:
            error_msg = Label(enter_pin.new_win,text="Error! Pin does not match", font=cour15, fg='red')
            error_msg.pack()

    lbl = Label(enter_pin.new_win, text='Enter your PIN',font=cour20,fg='black')
    lbl.pack(pady=10)
    option = Label(win, text='\n', font=cour15, fg='white')
    option.pack()
    global entry_box
    entry_box = Entry(enter_pin.new_win, font=cour15, show='*', justify='center')  # show parameter display the input text as *(we can use any other element also)
    entry_box.pack()
    pin=entry_box.get()
    
    option = Label(win, text='\n', font=cour15, fg='white')
    option.pack()
    bf = Frame(enter_pin.new_win)
    bf.pack(side=BOTTOM)

    bf0 = Frame(enter_pin.new_win)
    bf0.pack(side=BOTTOM)

    bf1 = Frame(enter_pin.new_win)
    bf1.pack(side=BOTTOM)

    bf2 = Frame(enter_pin.new_win)
    bf2.pack(side=BOTTOM)

    bf3 = Frame(enter_pin.new_win)
    bf3.pack(side=BOTTOM)

    bf4 = Frame(enter_pin.new_win)
    bf4.pack(side=BOTTOM)

    rf = Frame(enter_pin.new_win)
    rf.pack(side=RIGHT)
    optio = Label(win, text='\n', font=cour15, fg='white')
    optio.pack()
    btn1 = Button(bf4,text='1',font=cour15,bg='black',fg='white', command=lambda:setInputText('1'))
    btn1.pack(side=LEFT, pady=10)

    btn2 = Button(bf4, text='2',bg='black',fg='white', font=cour15, command=lambda:setInputText('2'))
    btn2.pack(side=LEFT,padx=10)

    btn3 = Button(bf4, text='3',bg='black',fg='white', font=cour15, command=lambda:setInputText('3'))
    btn3.pack(side=LEFT)

    btn4 = Button(bf3, text='4',bg='black',fg='white', font=cour15, command=lambda:setInputText('4'))
    btn4.pack(side=LEFT)

    btn5 = Button(bf3, text='5',bg='black',fg='white', font=cour15, command=lambda:setInputText('5'))
    btn5.pack(side=LEFT,padx=10)

    btn6 = Button(bf3, text='6',bg='black',fg='white', font=cour15, command=lambda:setInputText('6'))
    btn6.pack(side=LEFT)

    btn7 = Button(bf2, text='7',bg='black',fg='white', font=cour15, command=lambda:setInputText('7'))
    btn7.pack(side=LEFT,pady=10)

    btn8 = Button(bf2, text='8', bg='black',fg='white',font=cour15, command=lambda:setInputText('8'))
    btn8.pack(side=LEFT, padx=10)

    btn9 = Button(bf2, text='9',bg='black',fg='white', font=cour15, command=lambda:setInputText('9'))
    btn9.pack(side=LEFT)

    #btn = Button(bf1, text=' ', font=cour15)
    #btn.pack(side=LEFT)

    btn0 = Button(bf1, text='0',bg='black',fg='white', font=cour15, command=lambda:setInputText('0'))
    btn0.pack(side=BOTTOM, padx=70)

    #btn_ = Button(bf1, text=' ', font=cour15)
    #btn_.pack(side=LEFT)

    enter_btn = Button(bf0, text='ENTER', font=cour15,fg='white',bg='black',command=check_pin)
    enter_btn.pack(side= LEFT, pady=10,padx=10)

    exit_btn = Button(bf0, text='EXIT', font=cour15,fg='white',bg='black', command=lambda:[enter_pin.new_win.destroy(), win.deiconify()])   # .deiconify() makes the associated window visible
    exit_btn.pack(side=RIGHT, padx=10)

    clear_btn = Button(bf0,text='CLEAR', font=cour15,fg='white',bg='black', command=text_delete)
    clear_btn.pack(side=LEFT)


def acctype():
                   # check enter_pin() function for the functionality of .withdraw()
    enter_pin.new_win.withdraw()
    acctype.acctype_win = Toplevel(win)
    acctype.acctype_win.geometry('460x390')
    lb2 = Label(acctype.acctype_win,text='\nSelect Account Type\n ',font=cour20,fg='black')
    lb2.pack(pady=10)
    bf0 = Frame(acctype.acctype_win)
    bf0.pack()
    saving = Button(bf0,text='Savings', font=cour15,bg='black',fg='white',command=option_func_savings,anchor='center')
    saving.pack(padx=30, pady=10,side=LEFT)
    current = Button(bf0,text="Current", font=cour15, bg='black',fg='white', command=option_func_current,anchor='center')
    current.pack(padx=50, pady=10,side=LEFT)

read_csv1()    
# main opening window
title_label = Label(win, text='ATM', font=tim40, fg='black')              # Lackbel is something similar to a label which displays text on the window
title_label.pack(pady=1)                                               # pad y gives vertical distance both above and below where as pad x gives

#displaying some introduction
intro = Label(win, text='\nWelcome User ', font=cour20, fg='grey')
intro.pack()
def takinginp():
   global entry_
   card_no= entry_.get()
   print(card_no)
   
   check = Card_no_verification(card_no)
   print(check)
   if check:
    error_msg = Label(win,text="Card available!", font=cour15, fg='red')
    error_msg.pack()
    enter_pin(card_no)
    #enter_btn = Button(text='ENTER', font=cour15,fg='white',bg='black',command=takinginp,anchor=CENTER)
    #enter_btn.pack(pady=10,padx=10) 
   else:
    error_msg = Label(win,text="Error! Card number unavailable", font=cour15, fg='red')
    error_msg.pack() 

label = Label(win,text='\nEnter your Card number ',font=cour20,fg='black')
label.pack(pady=10)
option = Label(win, text='\n', font=cour15, fg='white')
option.pack()
entry_ = Entry(win,font=cour15, justify='center') 
entry_.focus_set() 
entry_.pack() 
enter_btn = Button(text='ENTER', font=cour15,fg='white',bg='black',command=takinginp,anchor=CENTER)
enter_btn.pack(pady=10,padx=10)

#option_label = Label(win, text='\nSelect your account type', font=cour15, fg='grey')
#option_label.pack()
option_l = Label(win, text='\n', font=cour15, fg='white')
option_l.pack()
bottom_frame = Frame(win)
bottom_frame.pack(side=BOTTOM)
right_frame = Frame(win)
right_frame.pack(side=RIGHT)

note = Label(bottom_frame, text='NOTE:Use only EXIT button to exit', font=cour15, fg='red',background='white')
note.pack(pady=10)
top = Frame(win)
top.pack(side=TOP)


win.mainloop()