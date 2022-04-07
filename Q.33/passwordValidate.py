
# Python program to check the validity of password input by users.

pwd_input = input("Enter password: ")
count = 0  # count variable initialized that gets incremented when an input password
# contains an uppercase letter, lowercase letter, digit or a special from the list
# given below
spe_chars = ['@', '$', '#']  # List of special characters allowed

# Condition to check if length of password is between 7 and 12 characters
if 7 <= len(pwd_input) <= 12:
    for i in pwd_input:
        if i.isalpha():
            count += 1
            break

    for j in pwd_input:
        if j.isupper():
            count += 1
            break

    for k in pwd_input:
        if k.isnumeric():
            count += 1
            break

    for l in pwd_input:
        if l in spe_chars:
            count += 1
            break

    if count == 4:
        print("Password Accepted", pwd_input)

    else:
        print("Password Rejected!")


else:
    print("Password too big or small!")
