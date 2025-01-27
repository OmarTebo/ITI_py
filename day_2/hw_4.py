# sort a list of numbers in ascending order (without using the built-in function)

# FINALLY SOME CODE I USED IN C
def bubble_sort(numbers): # BUBBLE SORT BUBBLE SORT BUBBLE SORT
    size = len(numbers)
    for i in range(size): # iterate through "list"
        for j in range(size - i - 1): # inner iteration for comparison later
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

uns_list = [2, 5, 7, 1, 9, 60, 30]
print(bubble_sort(uns_list))
