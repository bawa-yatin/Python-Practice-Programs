def divide_five_by_zero(val1, val2):
    try:
        result = val1 // val2
        return result
    except ZeroDivisionError:
        print("Number cannot be divided by 0!")
    finally:
        print("I'm always executed")


res = divide_five_by_zero(5, 0)
if res is not None:
    print(res)
