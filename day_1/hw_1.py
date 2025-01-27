# Find all unique characters in a string

def find_uniques(input_txt):
    char_count = {} # dictionary to remove duplicate keys (unique chars)

    for char in input_txt:
        if (char in char_count):
            char_count[char] += 1 # Counter, hope it works right
        else:
            char_count[char] = 1 # Just in case


    non_repeated = [] # List to store final result
    for char in input_txt:
        if (char_count[char] == 1):
            non_repeated.append(char) # adds the unique char to to list
   
    return non_repeated

uni_txt = find_uniques(input("Entre a string> "))
print(f"the unique characters set are: {uni_txt}")
