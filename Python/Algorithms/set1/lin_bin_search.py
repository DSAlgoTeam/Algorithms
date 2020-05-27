def lin_search(arr, value):
    if arr:
        if value in arr:
            return arr.index(value)
    return -1





def bin_search(arr, value):
    if arr != sorted(arr):
        raise ValueError(' list must be sorted for bin_search ')

    high = len(arr) -1
    low =0

    while low <= high:
        mid = (low + high) //2 

        if arr[mid] == value:
            return mid

        if arr[mid] > value:
            high =mid-1

        else: low = mid+1

    return -1