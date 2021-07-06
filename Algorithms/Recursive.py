def sumRecursive(arr):
    if arr == [] :
         return 0
    else:
        return arr[0] + sumRecursive(arr[1:])

def maxRecursive(arr):
    if len(arr) == 1 :
        return arr[0]
    else:
        nextNumber = arr.pop(0)
        return max(nextNumber, maxRecursive(arr))

def binarySearchRecursive(arr, low, high, num):
    mid = (low + high) // 2
    if high >= low:
        if arr[mid] == num:
            return mid
        else:
            if arr[mid] < num:
                return binarySearchRecursive(arr, mid + 1, high, num)
            else:
                return binarySearchRecursive(arr, low, mid-1, num)
    else:
        return -1