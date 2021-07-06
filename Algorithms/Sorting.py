def selectionSort(arr):

    for j in range(0,len(arr)):
        maxElement = arr[j]
        position = j
        for i in range(j,len(arr)):
            if arr[i] > maxElement:
                maxElement = arr[i]
                position = i
        del arr[position]
        arr.insert(0, maxElement)
        print(arr)

def quickSort(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[-1:]
        else:
            return arr
    elif len(arr) == 1:
        return arr
    else:
        pivot = arr[0]
        arr_left = [element for element in arr if element < pivot ]
        arr_right = [element for element in arr if element > pivot ]
        arr_left_sorted = quickSort(arr_left)
        arr_right_sorted = quickSort(arr_right)
        return arr_left_sorted + [pivot] + arr_right_sorted


def merge(arr, low, high, mid):
    newArray = []
    i = 0
    j = 1

    while i <= mid - low and j < high - mid + 1:
        if arr[low + i] <= arr[mid + j]:
            newArray.append(arr[low + i])
            i = i + 1
        else:
            newArray.append(arr[mid+j])
            j = j + 1

    while i <= mid - low:
        newArray.append(arr[low + i])
        i = i + 1
    while j < high - mid + 1:
        newArray.append(arr[mid + j])
        j = j + 1

    arr[low:high+1] = newArray
    return arr


def mergeSort(arr, low, high):
    if high - low == 0:
        return arr
    else:
        mid = (low + high) // 2
        arr = mergeSort(arr, low, mid)

        arr = mergeSort(arr, mid+1, high)
        arr = merge(arr, low, high, mid)
        return arr









