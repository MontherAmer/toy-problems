# pinary search tree
# recursice solution


def solution(arr, left, right, elem):
    if right >= left:
        # if the element is the mid of the array return the mid
        mid = left + (right - left)
        if elem == arr[mid]:
            return mid
        elif arr[mid] > elem:
            return solution(arr, left, mid-1, elem)
        else:
            return solution(arr, mid+1, right, elem)
    else:
        return -1


arr = [2, 3, 4, 10, 14, 13, 16, 17, 34, 36, 40]
right = len(arr)-1
left = 0
elem = 40
print(solution(arr, left, right, elem))

# using loop


def solution2(arr, left, right, elem):
    mid = left + (right - left)
    while right >= left:
        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(solution2(arr, left, right, elem))
