def strRepeat(str1, num):
    if num < 0:
        return ""
    elif num == 1:
        return str1

    return str1 + strRepeat(str1, num-1)


result = strRepeat("Hello", 6)
print(result)
