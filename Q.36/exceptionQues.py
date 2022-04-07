
# Write a function to compute 5/0 and use try/except to catch the exceptions.

def divide_five_by_zero(val1, val2):
    try:
        result = val1 // val2
        return result
    except ZeroDivisionError:
        print("Number cannot be divided by 0!")
    finally:
        print("I'm always executed")


res = divide_five_by_zero(5, 0)  # Variable holding the response returned from
# the function "divide_five_by_zero()"
if res is not None:
    print(res)
