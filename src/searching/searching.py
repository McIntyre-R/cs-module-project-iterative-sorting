def linear_search(arr, target):
    for e in arr:
        if e == target:
            return arr.index(e)

    return -1 


def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high+low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid-1
        elif arr[mid] > target:
            high = mid+1
        else:
            break


    return -1 