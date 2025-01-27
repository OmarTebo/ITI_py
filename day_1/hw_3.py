def reverse_arr(arr):
    size = len(arr)
    temp = [0] * size
    for i in range(size):
        temp[i] = arr[size - i - 1]

    for i in range(size):
        arr[i] = temp[i]

arr = [1, 2, 3, 4, 5, 6]
reverse_arr(arr)
print(arr)
