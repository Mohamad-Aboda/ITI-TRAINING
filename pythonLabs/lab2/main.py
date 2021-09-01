from registration import registration
from login import login
from project import project 


def welcome():
    print('register or login[R/L]')
    ans = input()
    if ans == 'r' or ans== 'R':
        registration()
        login()
        project()
        print('************************************************************************************************')


        
    elif ans == 'L' or ans == 'l':
        login()
        project()
        print('************************************************************************************************')

    else:
        print('Enter valid[Y/N]!')

if __name__ == '__main__':
    ok = True
    while ok:
        welcome()
