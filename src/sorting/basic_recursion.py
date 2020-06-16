'''
Example: Countdown
'''


def countdown_to_one(n):
    # 2. base case
    if n == 0:
        return
    print(n)
    countdown_to_one(n-1)  # 1. calls itself


countdown_to_one(5)

'''
Example: Recursive Sum
'''


def sum_list(items):
    # 1. base case
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])  # 2. recursive call
        # move towards the base case


sum_list([1, 2, 3, 4, 5])

'''
Example: Factorial
'''


def factorial(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + factorial(items[1:])


factorial([1, 2, 3, 4, 5])

'''
Example: Naive Fibonacci
'''
# We need to first understand the problem
# Then, plan out our solution using pseudocode
# Finally, turn our pseudocode into actual python code

# we know the first two items are 0 and 1
# we know that every item in the sequence is determined by summing the previous two items


def naive_fibonacci(n):
    # what is the base case?
    # TODO: look at handling negatives
    if n == 0:
        return 0
    if n == 1:
        return 1
    # what is the recursive case?
    n_minus_1 = naive_fibonacci(n-1)
    n_minus_2 = naive_fibonacci(n-2)
    return n_minus_1 + n_minus_2
    # how does it move towards the base case?
