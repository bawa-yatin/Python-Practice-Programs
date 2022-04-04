def polygon_side_sum():
    sides = int(input("Enter the number of sides: "))
    res = (sides - 2) * 180
    sides_sum = "Sum of interior angles of a polygon is : " + str(res)
    return sides_sum


result = polygon_side_sum()
print(result)
