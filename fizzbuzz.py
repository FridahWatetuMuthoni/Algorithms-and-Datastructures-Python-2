# first you need a function that takes the range of the numbers
# in the function you need a loop that loops thru the numbers in that range
# first check if a number is both divisible by both 3 and 5 and if so print fizzbuzz
# check if the number is divible by 3 and if so print fizz
# check if the number is divible by 5 and if so print buzz
# else just print the number

def fizz_buzz(n):
    for i in range(0, n+1):
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        elif (i % 7 == 0):
            print("bazz")
        else:
            print(i)


def fizz_buzz_modified(n):
    for i in range(0, n+1):
        out = ""
        if (i % 7 == 0):
            out += "bazz"
        if (i % 3 == 0):
            out += "fizz"
        if (i % 5 == 0):
            out += "buzz"

        print(out or i)


fizz_buzz_modified(20)  # O(n)
