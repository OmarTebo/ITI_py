# make function that take n as argument
# and print that pyramid based on number of n

def foo(n):
    for i in range(0, n):
        print(" " * (n-i), "*" * (i+1) + "*" * i)

foo(4)

