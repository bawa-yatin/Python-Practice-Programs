def str_repeat(str1, num):
    if num < 0:
        return ""
    elif num == 1:
        return str1

    return str1 + str_repeat(str1, num-1)


result = str_repeat("Hello", 6)
print(result)
