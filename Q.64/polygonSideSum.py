
# Python program to print the sum of the polygon angle side in degree.
# Take side of angle input from console

# User-defined function to return the sum of the polygon side
def polygon_side_sum():
    # Using try-except block to verify whether the value provided for number of sides
    # are in correct form or not
    try:
        sides = int(input("Enter the number of sides: "))
        res = (sides - 2) * 180  # Variable holding the sum of polygon side
        sides_sum = "Sum of interior angles of a polygon is : " + str(res)
        return sides_sum
    except ValueError:
        print("Provide a numeric value only!")


result = polygon_side_sum()  # Variable holding the response returned from the function
if result is not None:
    print(result)
