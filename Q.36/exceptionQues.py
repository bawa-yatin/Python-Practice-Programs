def divideFiveByZero(val1, val2):
    try:
        result = val1 // val2
        return result
    except ZeroDivisionError:
        print("Number cannot be divided by 0!")
    finally:
        print("I'm always executed")


res = divideFiveByZero(5, 0)
if res is not None:
    print(res)
