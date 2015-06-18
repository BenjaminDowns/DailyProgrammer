number = 197
original_number = number
steps = 0

def make_palindrome(number):
    global steps
    if str(number) == ((str(number))[::-1]):
        print "{0} gets palindromic after {1} steps: {2}".format(original_number, steps, number)
    else:
        steps += 1
        make_palindrome(number + (int(str(number)[::-1])))

make_palindrome(number)
