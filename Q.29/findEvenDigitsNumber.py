# Python Program which will find all such numbers between 0 and n (both included) such
# that each digit of the number is an even number.

# Approach 1: Using For Loop
limit = int(input("Enter the number limit: "))
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


# Approach 2: Using Function
def evenElements():
    no_limit = int(input("Enter the number limit: "))
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


res = evenElements()
print("Using Function")
print(res)


# Approach 3: Using Class
class evenNos:
    def getEvenDigitNos(self):
        no_limit = int(input("Enter the number limit: "))
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


en = evenNos()
result = en.getEvenDigitNos()
print("Using Class")
print(result)
