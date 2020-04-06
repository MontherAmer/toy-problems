import math

"""
jumb search function will recive array and element to search for
"""


def jumbSearch(arr, x):
    n = len(arr)
    # best step length is the square root of the array length
    step = int(math.sqrt(n))
    prev = 0
    # keep add steps until the element is less than the next step
    while arr[step - 1] < x:
        prev += step
        step += math.sqrt(n)
        if prev > n:
            return -1

    # loop from the prev step untill reach the element
    while arr[prev] < x:
        prev += 1
        if prev == step:
            return -1
    
    if arr[prev] == x:
        return prev

    return -1


# test the function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 6

print(jumbSearch(arr, x))
