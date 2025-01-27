# make function rotate array based on variable k
# for example x = [1, 2, 3, 4, 5, 6] k = 3
# output = [4, 5, 6, 1, 2, 3]

def rotate_arr(ar, k):
    k = k % len(x)
    return x[-k:] + x[:-k]

x = [1, 2, 3, 4, 5, 6]
print("x after rotation by 3")
print(rotate_arr(x, 3))
