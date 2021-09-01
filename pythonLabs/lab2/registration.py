import re 


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

    print('Congratulations your registration completed successfully!')
    print('************************************************************************************************')


