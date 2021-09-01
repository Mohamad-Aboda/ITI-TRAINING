import sys 
from registration import aemail, apassword

# User Login Function 
def login():
    ok = True
    while ok:
        print('Login To The System [Y/N]')
        ans = input()
        if ans == 'y' or ans == 'Y':
            ok = False
        elif ans == 'n' or ans == 'N':
            sys.exit()
        else:
            print('Please Enter [Y/N]?')

    one = False
    ok = True
    while ok:
        print(f'Enter your email address!')
        user_email = input()
        print(f'Enter your password!')
        user_password = input()

        if user_email in aemail and user_password in apassword:
            one = True
        
        if one:
            print('You Loged successfully!')
            print('************************************************************************************************')
            

            ok = False
        else:
            print('Enter valid email or password!')
    




