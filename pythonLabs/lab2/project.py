import sys 
from termcolor import colored

# from main import bcolors




# Project Function 
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
                for i in range(n):
                    print(f'PROJECT NAME IS {atitle[i]}')
                    print(f'PROJECT DETAILS ARE {adetails[i+1]}')
                    print(f'PROJECT TOTAL_TARGET IS  {atotal_target[i+2]}')
                    break
                    i += 1
                    

        else:
            sys.exit()

    

