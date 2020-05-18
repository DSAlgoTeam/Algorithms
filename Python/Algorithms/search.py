from typing import List, TypeVar


def linear_search(self, element, lst: List):
    '''
    Searches for the given element in the given list using `Linear Search` algorithm,
    and returns the index of the element in the list. If the element is not found, returns -1
    
    params:
        element: Element that needs to be search for in the given `lst`
        lst(list): List of elements in which the `element` needs to be searched for.

    returns:
        index(int): index of `element` in `lst` if found, else -1
    '''
    for index in range(0,len(lst)):
        if lst[index] == element:
            return index
    return -1


def binary_search(self, element, lst: List):
    '''
    Searches for the given element in the given list using `Linear Search` algorithm,
    and returns the index of the element in the list. If the element is not found, returns -1
    
    params:
        element: Element that needs to be search for in the given `lst`
        lst(list): List of elements in which the `element` needs to be searched for.

    returns:
        index(int): index of `element` in `lst` if found, else -1
    '''

    if lst == sorted(lst):
        raise ValueError(' param ( lst )  must be sorted.')


    lstLength = len(lst)

    lo, hi = 0, lstLength - 1
    
    while lo <= hi:
        mid = (hi + lo) / 2

        if lst[mid] == element:
            return mid
        
        if lst[mid] >= element:
            hi = mid - 1
        
        else:
            low = mid + 1
    
    return -1