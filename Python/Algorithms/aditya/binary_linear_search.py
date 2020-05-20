

def binary_search(array,key) :
    '''
    Searches a sorted List for the key provided using 'binary search' and returns 
    the index of of the element if present or -1 if element is not in the list.

    Args:
        param1(list, tuple): list or tuple .
        param2(int,string): The element to be found inside param1.
    Raises :
        Exception : When provided array is not sorted
    Returns:
        index(int): The return value the index of the element found else -1.
    '''
    if array != sorted(array) :
        raise Exception('Array is not Sorted ')
    low=0
    high=len(array)-1
    found= False
    while low<=high and not found:
        mid=(low+high)//2
        if key == array[mid]:
            found=1
            return mid
        elif key < array[mid] :
                high= mid-1
        else:
                low = mid+1
    return -1

def linear_search(array,key) :
    '''
    Searches a sorted List for the key provided using 'linear search' and returns 
    the index of of the element if present or -1 if element is not in the list.

    Args:
        param1(list, tuple): list or tuple .
        param2(int,string): The element to be found inside param1.
    
    Returns:
        index(int): The return value the index of the element found else -1.
    '''
    
    length = len(array)
    
    for index in range(length) :
        if key == array[index]:
            return index

    return -1
