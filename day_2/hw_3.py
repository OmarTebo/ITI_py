# invert a dictionary, where keys become values and values become keys.

def inv_dict(in_dict):
    inverted_dict = {}
    for key, value in in_dict.items(): # WHY TOO MANY BUILT-INS FFS
        if value not in inverted_dict:
            inverted_dict[value] = []

        inverted_dict[value].append(key)
    return inverted_dict

input_dict = {"l":5, "m":4, "n":3, "o":2}
print(inv_dict(input_dict))
