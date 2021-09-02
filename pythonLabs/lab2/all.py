from termcolor import colored
import re 
import sys


# User Registration Function 
fname = lname = aemail = apassword = aphone = []
def registration():
    print(f'Enter your first name!')
    first_name = input()
    fname.append(first_name)
    print(f'Enter your last name!')
    last_name = input()
    lname.append(last_name)

    print(f'Enter your email!')
    ok = True
    while ok:
        email = input()
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(pattern, email)):
            aemail.append(email)
            ok = False
        else:
            print('Enter valid email!')



    print('Enter your password!')
    password = input()
    print('Enter your password again!')
    confirm_password = input()
    if(password == confirm_password):
        apassword.append(password)
        
    print('Enter your phone number!')
    phone_pattern = r'^01[0125][0-9]{8}$'
    ok = True
    while ok:
        phone = input()
        if re.fullmatch(phone_pattern, phone):
            aphone.append(phone)
            ok = False
        else:
            print('Enter valid phone number!')

    print(colored('Congratulations your registration completed successfully!', 'green'))
    print(colored("*************************************************************************************", "red"))



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
            print(colored('You Loged successfully!', 'green'))
            print(colored("*************************************************************************************", "red"))

            ok = False
        else:
            print('Enter valid email or password!')
    


atitle = adetails = atotal_target = [] 

def project():
    print("Welcome To The Crowd-Funding")
    print('create project or view previous prjects Y for create , N for viwe [Y/N]?')
    ok = True
    while ok:
        ans = input()
        if ans == 'Y' or ans == 'y':
            print('Enter the campaign title!')
            title = input()
            atitle.append(title)
            print('Enter the campaign details!')
            details = input()
            adetails.append(details)
            print('Enter the total target required for the campaign!')
            total_target = input()
            atotal_target.append(total_target)
            # start_date = input()
            # end_date = input()
            ok = False
        elif ans == 'n' or ans == 'N':
            if len(atitle) == 0:
                print('NO previous project available now!')
            else:
                n = len(atitle)
                j = 0
                cnt = 1
                for i in range(n//3):
                    print(colored('PROJECT INFO', 'red'), colored(cnt, 'red'))
                    print(f'PROJECT NAME IS {atitle[j]}')
                    print(f'PROJECT DETAILS ARE {adetails[j+1]}')
                    print(f'PROJECT TOTAL_TARGET IS  {atotal_target[j+2]}')
                    i += 1
                    j += 3
                    cnt += 1
                    print(colored("*************************************************************************************", "yellow"))

                    

        else:
            sys.exit()

    






def welcome():
    print(colored("*****************************************WELCOME********************************************", "green"))
    ok = True
    while ok:
        print('register or login[R/L]')
        ans = input()
        if ans == 'r' or ans== 'R':
            registration()
            login()
            project()
            print(colored("*************************************************************************************", "red"))

            
        elif ans == 'L' or ans == 'l':
            login()
            project()
            print(colored("*************************************************************************************", "red"))

        else:
            print('Enter valid[Y/N]!')

        print('Do you want to create more or exit[Y/N]?')
        ans = input()
        if ans == 'y' or ans == 'Y':
            ok = True
        elif ans == 'n' or ans == 'N':
            ok = False
        else:
            print(colored('Enter valid answer!', 'red'))

if __name__ == '__main__':
    ok = True
    while ok:
        welcome()
