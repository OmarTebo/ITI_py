def count_chars(input_txt):
    char_count = {}

    for char in input_txt:
        if (char in char_count):
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

txt = count_chars(input("Enter a string> "))
print(txt)
