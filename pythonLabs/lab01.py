import math

# 1
def count_vowels(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'e' or s[i] == 'a' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            cnt += 1
    return cnt

# 2

arr = []
def generate_array_of_specific_length(start, length):
    for i in range(length):
        arr.append(i+1)

# 3

temp = []
def arr_with_five_elements():
    i = 0
    while i < 5:
        print(f"ENTER ELEMENT NUMBER({ i+1})")
        inpt = input()
        temp.append(inpt)
        i += 1
    temp.sort(reverse=True)
    print(f"Arr after sortted Descending ")
    for i in range(5):
        print(temp[i], end=' ')
    print('\n')
    temp.sort(reverse=False)
    print(f"Arr after sortted Ascending ")
    for i in range(5):
        print(temp[i], end=' ')


# 4

def check_number(n):
    if n % 3 == 0:
        print("FIZZ")
    elif n % 5 == 0:
        print("buzz")
    elif n % 3 == 0 or n % 5 == 0:
        print("FizzBuzz")
    else:
        print("Number not divisible by both 3 and 5")



# 5

def reverse_string():
    print(f"Enter the name you want to reverse")
    name = input()
    print(name[::-1])

# 6
import math
def area():
    ok = True
    while ok:
        print(f"Enter the radius")
        r = int(input())
        res = r * r * math.pi
        print(f"Area is = {res}")
        print(f"do you want to continue? [y,n]")
        ans = input()
        if ans == 'n' or ans == 'N':
            ok = False


# 7
import re
def ask_for_name():
    print("Enter you name")
    name = input()
    while name == '':
        name = input()

    print("Enter you email")
    email = input()
    print(name)
    print(email)

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(pattern, email)):
        print("Valid Email")
    else:
        print("Invalid Email")



# 8
def count_iti():
    print(f"ENTER the word")
    s = input()
    res = s.count("iti")
    print(res)

# 9

def longest_substring(s):
    maxLen = 0
    current = s[0]
    longest = s[0]

    for i in range(len(s) - 1):
        if s[i + 1] >= s[i]:
            current += s[i + 1]
            if len(current) > maxLen:
                maxLen = len(current)
                longest = current
        else:
            current = s[i + 1]
        i += 1

    print(longest)

if __name__ == '__main__':
    # res = count_vowels("aeiouaeiouabbbb")
    # print(res)

    # generate_array_of_specific_length(1, 3)
    # for i in range(3):
    #     print(arr[i])

    # arr_with_five_elements()

    # check_number(7)

    #reverse_string()

    # area()

    ask_for_name()

    # count_iti()

    # longest_substring('abdulrahman')
    # longest_substring('abcabcdef')











