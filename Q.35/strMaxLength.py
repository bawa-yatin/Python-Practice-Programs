def getStrMaxLength(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    elif len(str1) == len(str2):
        print(str1, end='\n')
        print(str2)


str_val_1 = input('Enter first string: ')
str_val_2 = input('Enter second string: ')
getStrMaxLength(str_val_1, str_val_2)
