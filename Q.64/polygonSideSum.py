def polygon_side_sum():
    try:
        sides = int(input("Enter the number of sides: "))
        res = (sides - 2) * 180
        sides_sum = "Sum of interior angles of a polygon is : " + str(res)
        return sides_sum
    except ValueError:
        print("Provide a numeric value only!")


result = polygon_side_sum()
if result is not None:
    print(result)
