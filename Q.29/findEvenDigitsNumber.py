# Python Program which will find all such numbers between 0 and n (both included) such
# that each digit of the number is an even number.

# Approach 1: Using For Loop

try:
    limit = int(input("Enter the number limit: "))
    if limit > 0:
        even_ele = []
        for i in range(limit + 1):
            str_form = str(i)
            if i < 10:
                if i % 2 == 0:
                    even_ele.append(i)
            elif 10 <= i < 100:
                if int(str_form[0]) % 2 == 0 and int(str_form) % 2 == 0:
                    even_ele.append(i)
            elif 100 <= i < 1000:
                if int(str_form[0]) % 2 == 0 and int(str_form) % 2 == 0:
                    even_ele.append(i)

        print(even_ele)
    else:
        print("Limit less than 0!")

except ValueError:
    print("Provide numeric value only!")


# Approach 2: Using Function
def even_elements():
    try:
        no_limit = int(input("Enter the number limit: "))
        if no_limit > 0:
            list_items = []
            for j in range(no_limit + 1):
                s1 = str(j)
                if j < 10:
                    if j % 2 == 0:
                        list_items.append(j)
                elif 10 <= j < 100:
                    if int(s1[0]) % 2 == 0 and int(s1) % 2 == 0:
                        list_items.append(j)
                elif 100 <= j < 1000:
                    if int(s1[0]) % 2 == 0 and int(s1) % 2 == 0:
                        list_items.append(j)

            return list_items
        else:
            print("Limit less than 0!")
    except ValueError:
        print("Provide numeric value only!")


res = even_elements()
if res is not None:
    print("Using Function")
    print(res)


# Approach 3: Using Class
class evenNos:
    def get_even_digit_nos(self):
        try:
            no_limit = int(input("Enter the number limit: "))
            if no_limit > 0:
                list_items = []
                for j in range(no_limit + 1):
                    s1 = str(j)
                    if j < 10:
                        if j % 2 == 0:
                            list_items.append(j)
                    elif 10 <= j < 100:
                        if int(s1[0]) % 2 == 0 and int(s1) % 2 == 0:
                            list_items.append(j)
                    elif 100 <= j < 1000:
                        if int(s1[0]) % 2 == 0 and int(s1) % 2 == 0:
                            list_items.append(j)

                return list_items
            else:
                print("Limit less than 0!")
        except ValueError:
            print("Provide numeric value only!")


en = evenNos()
result = en.get_even_digit_nos()
if result is not None:
    print("Using Class")
    print(result)
