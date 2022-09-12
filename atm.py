from glob import glob
from optparse import Option
from numpy import random
import sys

acct_details = dict()
loginUser = []
print('Welcome to LC Bank, how can we service you today?')
def menu():
    print('''
          1. Open Account
          2. Transaction
          3. Quit''')    
    option = input('>>> ')
    if option =='1':
        Open_acct()
    elif option =='2':
        transact()
    elif option=='3':
        sys.exit()

def Open_acct():
    Name = input('First Name and Last Name ')
    Age = int(input('How old are you? '))
    Email = input('Enter your Email ')
    account = random.randint(1000000000)
    pin = random.randint(1000, 9000)
    balance = 0.0
    print('Please wait while we generate your account information...')
    acct_info = [Name, Age, Email, account, pin, balance]
    acct_details[account] = acct_info
    print(acct_details)
    menu()
    
def transact():
    global loginUser
    account = int(input('Account Number '))
    if account in acct_details:
        loginUser = acct_details.get(account)
           
    else:
        print('Invalid login details, try again')
    pin = int(input('Input your Pin '))
    if pin == loginUser[4]:
        
        print(''' Enter your operation:
            1. Deposit
            2. Check Balance
            3. Withdraw
            4. Buy Airtime
            5. quit''')
   
    else:
        print('Invalid login details, try again')
    option = input('>>> ')
    if option == '1':
        depo()
    if option == '2':
        bal()
    if option == '3':
        wtd()
    if option == '4':
        airt()
    if option == '5':
        menu()

def depo():
    Amount = int(input('How much do you want to deposit? '))
    print('Your ' + str(Amount) + ' was deposited successfully')
    loginUser[5] += Amount 
    print('Do want to perform another transaction? ')
    print('''
          1. Yes
          2. No''')
    option = input('>>> ')
    if option == '1':
        transact()
    if option == '2':
        menu()
    

def bal():
    print('Your account balance is ', loginUser[5])
    print('Do want to perform another transaction? ')
    print('''
          1. Yes
          2. No''')
    option = input('>>> ')
    if option == '1':
        transact()
    if option == '2':
        menu()
    

def wtd():
    Amount = int(input('How much do want to withdraw? '))
    if Amount < loginUser[5]:
        print('Your ' + str(Amount) + ' was withdraw successfully')
    else:
        print('Insufficient fund')
    loginUser[5] -= Amount 
    print('Do you want to perform another transaction? ')
    print('''
          1. Yes
          2. No''')
    option = input('>>> ')
    if option == '1':
        transact()
    if option == '2':
        menu()
    
    
def airt():
    Amount = int(input('How much airtime do you want? '))
    if Amount < loginUser[5]:
        print('Your ' + str(Amount) + ' was withdraw successfully')
    else:
        print('Insufficient fund')
    loginUser[5] -= Amount 
    print('Do want to perform another transaction? ')
    print('''
          1. Yes
          2. No''')
    option = input('>>> ')
    if option == '1':
        transact()
    if option == '2':
        menu()
    
        
menu()