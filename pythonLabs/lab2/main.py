from registration import registration
from login import login
from project import project 
from termcolor import colored



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
