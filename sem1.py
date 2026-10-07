def move_zeros(arr):
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
            non_zero_index += 1

    return arr

print(move_zeros([0, 0, 1, 0, 3, 12]), move_zeros([0, 33, 57, 88, 60, 0, 0, 80, 99]), move_zeros([0, 0, 0, 18, 16, 0, 0, 77, 99]))