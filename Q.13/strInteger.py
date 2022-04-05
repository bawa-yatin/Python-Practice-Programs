# Python program to change string to integer and vice versa

# Approach 1:
str_user_age = input("Enter user age: ")
print(str_user_age)
print(type(str_user_age))

# Converting str to int
if str_user_age.isdigit():
    int_user_age = int(str_user_age)
    print(type(int_user_age))
else:
    print("String cannot be converted to int!")

var_1 = 109
print(type(var_1))
str_var_1 = str(var_1)
print(type(str_var_1))


# Approach 2: Using Functions

def str_int_convert():
    print("\nUsing Functions")
    user_age = input("Enter user age: ")
    print(user_age)
    print(type(user_age))

    # Converting str to int
    if user_age.isdigit():
        new_type_age = int(user_age)
        print(type(new_type_age))
    else:
        print("String cannot be converted to int!")

    var_2 = 87
    print(type(var_2))
    str_var_2 = str(var_2)
    print(type(str_var_2))


str_int_convert()


# Approach 3: Using Class
class convertStrInt:
    def convert_type(self):
        print("\nUsing Class")
        class_user_age = input("Enter user age: ")
        print(class_user_age)
        print(type(class_user_age))

        # Converting str to int
        if class_user_age.isdigit():
            type_age = int(class_user_age)
            print(type(type_age))
        else:
            print("String cannot be converted to int!")

        var_3 = 121
        print(type(var_3))
        str_var_3 = str(var_3)
        print(type(str_var_3))


cs = convertStrInt()
cs.convert_type()
