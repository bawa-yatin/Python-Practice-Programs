def left_rotate_str(value):
    str_left_rotations = []
    val_len = len(value)
    for i in range(val_len):
        value = value[1: val_len] + value[0]
        str_left_rotations.append(value)
    return str_left_rotations


left_rotate = left_rotate_str("abc")
print("Left Rotations:", left_rotate)


def right_rotate_str(value):
    str_right_rotations = []
    val_len = len(value)
    for i in range(val_len):
        value = value[-1] + value[0: val_len-1]
        str_right_rotations.append(value)
    return str_right_rotations


right_rotate = right_rotate_str("hello")
print("Right Rotations:", right_rotate)
