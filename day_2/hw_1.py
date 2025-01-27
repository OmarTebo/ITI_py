# make a function that takes a list as input and returns a new list with all duplicates removed

def list_filter(listy):
    return list(set(listy))

test_list = ["hello", 2, 2, 5, 5, 5, 3, "hello", "armor"]

print(list_filter(test_list))
