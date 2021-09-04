from termcolor import colored
import re , sys, psycopg2, datetime


# Postgres connection 
conn = psycopg2.connect(database="test",user='postgres',password='postgres',host='127.0.0.1',port= '5432')   
cursor = conn.cursor()
cursor.execute("SELECT email, user_password FROM registration_info;")
# User Registration Function 
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def registration():
    while True:
        first_name = input(colored('Enter your first name!', 'blue'))
        first_name = first_name.strip()
        if first_name  and len(first_name) >= 3 and first_name.isdigit() == False:
            break
        else:
            print(colored("Please enter valid name?? (name should be string not less than 3 characters)", 'red'))
    
    while True:
        last_name = input(colored('Enter Your Last Name!', 'blue'))
        last_name = last_name.strip()
        if last_name  and len(last_name) >= 3 and last_name.isdigit() == False:
            break
        else:
            print(colored("Please Enter Valid Name? (name should be string not less than 3 characters)", 'red'))


    while True: 
        email = input(colored('Enter Your Email Address!', 'blue'))
        if (re.fullmatch(email_pattern, email)):
            break
        else:
            print(colored('Please Enter Valid Email?', 'red'))
    
    while True:
        while True:
            password =  input(colored('Enter Your Password!', 'blue'))
            password = password.strip()
            if password:break
            else:print(colored('Please Enter Your Password?', 'red'))


        while True:    
            confirm_password = input(colored('Confirm Your Password!', 'blue'))
            confirm_password = confirm_password.strip()
            if confirm_password:break
            else:print(colored('Please Confirm Your Password?', 'red'))


        if password == confirm_password:break
        else: print(colored("Password Don't Match!", 'red'))


    phone_pattern = r'^01[0125][0-9]{8}$'
    while True:
        phone = input(colored("Enter Your Phone Number!", 'blue'))
        if re.fullmatch(phone_pattern, phone):break
        else:print(colored("Please Enter Valid Phone Number?", 'red'))
    
    cursor.execute("INSERT INTO registration_info(fname, lname, email, user_password, phone) VALUES(%s, %s, %s, %s, %s)", 
        (first_name,last_name, email, password, phone))

    conn.commit()
    # cursor.close()
    # conn.close()
    print(colored('Congratulations Your Registration Completed Successfully!', 'green'))
    print(colored("*************************************************************************************", "green"))

def login():
    flag = False
    while True:
        cursor.execute("SELECT email, user_password FROM registration_info;")
        data = cursor.fetchall()
        print(colored("Enter Your Email & Password To Login?", 'blue'))
        while True:
            login_email = input(colored("Enter Your Email Address: ", 'blue'))
            if (re.fullmatch(email_pattern, login_email)):
                break
            else:
                print(colored('Please Enter Valid Email?', 'red'))
        while True:
            login_password = input(colored("Enter Your Password: ", 'blue'))
            login_password = login_password.strip()
            if login_password:break
            else:print(colored("Password can't be empty?", 'red'))

        ok = False
        for row in data:
            if login_email in row[0] and login_password in row[1]:ok=True
                
        if ok :print(colored("Congratulations You Logged Successfully", 'green'));flag = True;break
        else:print(colored("Invalid Credentials?", 'red'))
    # cursor.close()
    # conn.close()
    flag = True # if the user is valid to view project
    return flag

def logic():
    ok = True
    f = res = False
    while ok:
        print(colored("Welcome To Crowd-Funding console app", 'yellow'))
        print(colored("[1] Enter 1 To Register", 'blue'))
        print(colored("[2] Enter 2 To Login", 'blue'))
        while True:
            ans = input(colored("Enter Your Selection?", 'yellow'))
            if ans == "1":
                registration()
                break
            elif ans == "2":
                f = login()
                break
            else:print(colored("Enter Valid Input!", 'red'))
        if f:welcome()
        else:
            while True:
                print(colored("You should login first to access the app!", 'yellow'))
                inp = input(colored("Do You Want To Login?[Y/N]", 'blue'))
                inp = inp.strip()
                inp = inp.lower()
                if inp == 'y':
                    res = login()
                    if res:welcome();break
                    else:print(colored("Invalid Credentials", 'red'));
                elif inp == 'n':sys.exit();break;
                else:print(colored("Enter Valid Input!", 'red'));break;
        
        while True:
            finish = input(colored("Do you want to continue?[Y/N]", 'blue'))
            finish = finish.lower()
            finish = finish.strip()
            if finish == 'n':ok = False;break 
            elif finish == 'y':welcome()
            else:print(colored("Enter Valid Input!", 'red'))

def create_project():
    
    while True:
        title = input(colored('Enter The Campaign Title!', 'blue'))
        title = title.strip()
        if title and len(title) >= 5:break
        else:print(colored("Project title can't be empty!"), 'red')
    
    while True:
        details = input(colored('Enter The Campaign Details!', 'blue'))
        details = details.strip()
        if details and len(details) >= 5:break
        else:print(colored("Project details can't be empty!"), 'red')

    
    while True:
        total_target = input(colored('Enter The Total Target Required For The Campaign!', 'blue'))
        total_target = total_target.strip()
        if total_target:break
        else:print(colored("Project total target can't be empty!"), 'red')

        

    while True:
        start_date = input("Enter the start date in format 'dd-mm-yy' : ")
        day, month, year = start_date.split('-')
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if isValidDate:break
        else:print(colored("Enter Valid Date?", 'red'))

    while True:
        end_date = input("Enter the end date in format 'dd-mm-yy' : ")
        day, month, year = start_date.split('-')
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if isValidDate:break
        else:print(colored("Enter Valid Date?", 'red'))

    cursor.execute("INSERT INTO project_info(title, details, total_target, start_date, end_date) VALUES(%s, %s, %s, %s, %s)", 
        (title,details, total_target, start_date, end_date))

    conn.commit()
    # cursor.close()
    # conn.close()

def view():
    cursor.execute("SELECT * from project_info;")
    data = cursor.fetchall()
    if data == []:
        print(colored("No Previous Projects Found!", 'red'))
    else:
        j = 0
        for idx in data:
            print(colored("PROJECT INFO", 'yellow'))
            print(f'Projcet Title Is {idx[j]}')
            print(f'Project Detais Is {idx[j+1]}')
            print(f'Project Total Target Is {idx[j+2]}')
            print(f'Project Start Date Is {idx[j+3]}')
            print(f'Project End Date Is {idx[j+4]}')
            print(colored('***********************************************', 'yellow'))
            
    
    conn.commit()

def delete_project():
    
    while True:
        ans = input(colored("Enter The Project Title You Want To Delete!", 'blue'))
        ans = ans.strip()
        if ans:
            cursor.execute("SELECT * from project_info")
            data = cursor.fetchall();
            Found = False
            for row in data:
                if ans  in row[0]:
                    Found = True
            if Found == False:print(colored("Project title not found!", 'red'))
            else:
                cursor.execute("DELETE FROM project_info WHERE title = %s ", (ans,))
                print(colored(f"Project {ans} deleted succefully!", 'green'))
                conn.commit()
                break
        else:
            print(colored("Enter Valid Input!", 'red'))
               
def update_project():
    cursor.execute("SELECT * from project_info;")
    data = cursor.fetchall()
    while True:
        ans = input(colored("Enter Project Title You Want to Modify?", 'blue'))
        ans = ans.strip()
        if ans:
            found = False
            for idx in data:
                if ans in idx[0]:found = True
            if found:
                while True:
                    title = input(colored('Enter The New Campaign Title!', 'blue'))
                    title = title.strip()
                    if title and len(title) >= 5:break
                    else:print(colored("Title can't be empty!", 'red'))
                
                while True:
                    details = input(colored('Enter The New Campaign Details!', 'blue'))
                    details = details.strip()
                    if details and len(details) >= 5:break
                    else:print(colored("Details can't be empty!", 'red'))
                
                while True:
                    total_target = input(colored('Enter The New Total Target Required For The Campaign!', 'blue'))
                    total_target = total_target.strip()
                    if total_target:break
                    else:print(colored("Total Target can't be empty!", 'red'))

                while True:
                    start_date = input(colored("Enter the New start date in format 'dd-mm-yy' : ", 'blue'))
                    day, month, year = start_date.split('-')
                    isValidDate = True
                    try:
                        datetime.datetime(int(year), int(month), int(day))
                    except ValueError:
                        isValidDate = False

                    if isValidDate:break
                    else:print(colored("Enter Valid Date?", 'red'))

                while True:
                    end_date = input(colored("Enter the New end date in format 'dd-mm-yy' : ", 'blue'))
                    day, month, year = start_date.split('-')
                    isValidDate = True
                    try:
                        datetime.datetime(int(year), int(month), int(day))
                    except ValueError:
                        isValidDate = False

                    if isValidDate:break
                    else:print(colored("Enter Valid Date?", 'red'))
                sql = """ UPDATE project_info 
                        SET title = %s , details = %s , total_target = %s , start_date = %s , end_date = %s
                        WHERE title = %s """
                cursor.execute(sql, (title, details, total_target, start_date, end_date, ans))
                print(colored('Data Updated Successfully!', 'green'))
                print(colored("******************************************************", "green"))

                conn.commit()
                break
                
            else:
                print(colored("Project Not Found?", 'red'))

        # cursor.close()
        # conn.close()
        else:print(colored("Input can't be empty",'red'))

def welcome():
    while True:
        print(colored("[1] Enter 1 To Create Project", 'blue'))
        print(colored("[2] Enter 2 To View All Projects", 'blue'))
        print(colored("[3] Enter 3 To Delete Project", 'blue'))
        print(colored("[4] Enter 4 To Update Project", 'blue'))
        print(colored("[5] Enter 5 To Exit Project", 'blue'))
        ans = input(colored("Enter Your Selection", 'yellow'))
        ans = ans.strip()
        if ans == "1":create_project();break
        elif ans == "2":view();break
        elif ans == "3":delete_project();break
        elif ans == "4":update_project();break
        elif ans == "5":sys.exit()
        else:print(colored("Enter valid input!", 'red'))

def search_by_date():
    while True:
        cursor.execute("SELECT * FROM project_info")
        data = cursor.fetchall()
        ans = input("Enter the Date in format 'dd-mm-yy' : ")
        day, month, year = ans.split('-')
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        print(type(ans))
        if isValidDate:
            if data == []:
                print(colored("No Previous Projects With That Date!", 'red'))
                break
            else:
                # cursor.execute("SELECT * FROM project_info WHERE start_date = %s", (ans))
                cursor.execute("""SELECT * FROM project_info 
               WHERE start_date BETWEEN 
                   date '2015-06-01' and 
                   date '2021-06-30';""")

                break

        else:print(colored("Enter Valid Date?", 'red'))


if __name__ == '__main__':
    logic()

