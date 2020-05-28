from collections.abc import Iterable
from ..data_structures.heap import Heap

def _is_iterable(iterable):
    '''
    helper function to raise Exceptions if the given iterable isn't of iterable type.
    '''

    if not isinstance(iterable, Iterable):
        raise ValueError('Given value isn\'t of Iterable type')
def _is_bool(val):
    '''
    helper function to raise an Exception if the given value isn't of bool type
    '''
    if not isinstance(val, bool):
        raise ValueError('The incremental attribute must be a of `bool` type only')

def _is_homogenous(iterable):
    '''
    Helper function to raise Exception if the elements in the given 
    iterable are not all of same type
    '''
    if not all([(type(iterable[0]) == type(_)) for _ in iterable]):
        raise TypeError('All elements in the given iterable should be of the same type')
def _is_int(num,var_name):
    if not isinstance(num,int):
        raise ValueError(str(var_name)+' should be of type `int`')

def bubble_sort(arr, incremental = True):
    '''
    Sorts the `arr` using bubble sort
    '''
    _is_bool(incremental)
    _is_iterable(arr)
    arr = list(arr)
    if incremental:    
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j+1],arr[j] = arr[j],arr[j+1]
    else:
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] < arr[j+1]:
                    arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr


def insertion_sort(arr, incremental = True):
    '''
    Sorts the fiven `arr` using insertion sort.
    '''
    _is_bool(incremental)
    _is_iterable(arr)
    arr = list(arr)
    if incremental:
        for i in range(1, len(arr)):
            temp = arr[i]

            j = i -1 
            while temp < arr[j] and j >=0:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
    else:
        for i in range(1, len(arr)):
            temp = arr[i]

            j = i -1 
            while temp > arr[j] and j >=0:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
    return arr

def selection_sort(arr, incremental = True):
    '''
    Sorts an iterable using selection sort
    '''
    _is_bool(incremental)
    _is_iterable(arr)
    if incremental:
        for i in range(len(arr)):
            smallest = i

            for j in range(i,len(arr)):
                if arr[j] < arr[smallest]:
                    smallest = j
            arr[i],arr[smallest] = arr[smallest],arr[i]
    else:
        for i in range(len(arr)):
            largest = i

            for j in range(i,len(arr)):
                if arr[j] > arr[largest]:
                    largest = j
            arr[i],arr[largest] = arr[largest],arr[i]
    return arr


def heap_sort(arr, incremental = True):
    '''
    Sort `arr` using heap sort
    '''
    _is_iterable(arr)
    _is_bool(incremental)
    arr = list(arr)
    l = len(arr)
    heap = None
    if incremental:
        heap = Heap(arr, True)
    else:
        heap = Heap(arr, False)
    arr = []
    while l > 0:
        arr.append(heap.remove())
        l -= 1
    print(heap.heap)
    return arr


def _partition(arr, start, end, incremental = True):
    '''
    Helper function for quick sort. Partitions `arr` between the `start` and `end` indexes.
    Returns a pivot index after partitioning.
    '''
    i = start + 1
    piv = arr[start] # taking the first element as the pivot
    if incremental:
        for j in range(start + 1, end + 1): 
            if arr[j] < piv: # shift elements smaller than pivot to left
                arr[j],arr[i] = arr[i],arr[j]
                i += 1
    else:
        for j in range(start + 1, end + 1):
            if arr[j] > piv:  # shift elements greater than pivot to left
                arr[j],arr[i] = arr[i],arr[j]
                i += 1
    arr[start],arr[i-1] = arr[i-1],arr[start] # placing the pivot element.
    return i - 1 # returning the pivot index


def quick_sort(arr, start = 0, end = None, incremental = True):
    '''
    sort elements in arr using quicksort algorithm
    ''' 
    _is_iterable(arr)
    if end is None:
        end = len(arr) - 1
    _is_bool(incremental)
    _is_int(start,'start'),
    _is_int(end, 'end')
    if start < end:
        pivot = _partition(arr, start, end, incremental)
        quick_sort(arr, start, pivot-1, incremental) # quick sort left part of partition
        quick_sort(arr, pivot + 1, end, incremental) # quick sort right part of partition


def _merge(arr, start, mid, end, incremental):
    '''
    Helper function for merge sort
    '''
    p,q = start, mid+1
    ar = [0] * (end - start+1)
    k = 0
    print(start, mid , end)
    if incremental:
        for i in range(start, end+1):
            if p > mid:
                ar[k] = arr[q]
                p += 1
            elif q > end:
                ar[k] = arr[p]
                q += 1
            elif arr[p] < arr[q]:
                ar[k] = arr[p]
                p += 1
            else:
                ar[k] = arr[q]
                q += 1
            k += 1
    else:
        for i in range(start, end+1):
            if p > mid:
                ar[k] = arr[q]
                p += 1
            elif q > end:
                ar[k] = arr[p]
                q += 1
            elif arr[p] > arr[q]:
                ar[k] = arr[p]
                p += 1
            else:
                ar[k] = arr[q]
                q += 1
            k += 1
    for i in range(k):
        arr[start] = ar[i]
        start += 1
    
    print(ar, arr)

def merge_sort(arr,start = 0, end = None, incremental = True):
    
    _is_iterable(arr)
    if end is None:
        end = len(arr) - 1
    _is_bool(incremental)
    _is_int(start, 'start')
    _is_int(end, 'end')

    if start < end:
        mid = (start +end ) // 2
        merge_sort(arr, start, mid, incremental)
        merge_sort(arr, mid + 1, end, incremental)
        _merge(arr, start, mid, end, incremental)


def count_sort(arr, incremental = True):
    '''
    sort elements using count sort.
    '''
#TODO: finish this 
    _is_iterable(arr)
    _is_bool(incremental)
    _is_homogenous(arr)
        