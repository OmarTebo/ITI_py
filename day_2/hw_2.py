# check if a given string is a palindrome (reads the same forwards and backwards).

def pali_check(txt):
    return txt == ''.join(reversed(txt))

word = input("Enter one word> ")
print(f"is {word} a palindrome: {pali_check(word)}")
