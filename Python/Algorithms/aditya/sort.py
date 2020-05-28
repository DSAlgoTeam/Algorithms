from heap import Heap

def bubble_sort(arr , order = 'desc') :
    length = len(arr)
    for  i in range(length - 1) :
        exchanges = False
        for j in range(length -i - 1) :
            if order == 'aesc' :
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] =  arr[j+1] , arr[j]
                    exchanges = True
            else :
                if arr[j] < arr[j+1] :
                    arr[j], arr[j+1] =  arr[j+1] , arr[j]
                    exchanges = True
        
        if exchanges == False :
            return arr
    return arr

def selection_sort(arr , fn = max) :
    length = len(arr) 
    for i in range(length - 1):
        element = fn(arr[:length - i ])
        index = arr[:length - i].index(element)
        arr[index], arr[length - i - 1] = arr[length - i - 1] , arr[index]

    return arr


def insertion_sort(arr ) :
    length = len(arr)
    for i in range(1, length ) :
        value  = arr[i]
        position = i
        while position > 0 and arr[position -1] > value :
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = value 
    return arr

def count_sort(arr ,place = 1) :
    value = max(arr) // place
    new_arr = [0]*len(arr)
    count_arr = [arr.count(i // place) for i in range(value + 1)]
    for index in range(1,len(count_arr)) :
        count_arr[index] += count_arr[index - 1]
    count_arr = [0] + count_arr[0:-1] 
    for each_item in arr :
        new_arr[count_arr[each_item // place]] = each_item
        count_arr[each_item // place] += 1
    return new_arr

def radix_sort(arr) :
    max = len(arr)
    place = 1
    while (max // place) > 0 :
        count_sort(arr,place)
        place *= 10

def heap_sort(arr) :
    new_arr = []
    heap = Heap(10,'max')
    for ele in arr :
        heap.insert(ele)
    for _ in range(len(arr)) :
        new_arr.append(heap.extract())
    return new_arr


def quick_sort(arr):
   quick_sort_helper(arr,0,len(arr)-1)
   return arr

def quick_sort_helper(arr,low,high):
   if low<high:
       splitpoint = partition(arr,low,high)
       quick_sort_helper(arr,low,splitpoint-1)
       quick_sort_helper(arr,splitpoint+1,high)

def partition(arr,low,high):
   pivotvalue = arr[low]
   left = low+1
   right = high
   done = False
   while not done:
       while left <= right and arr[left] <= pivotvalue:
           left = left + 1
       while arr[right] >= pivotvalue and right >= left:
           right = right -1
       if right < left:
           done = True
       else:
           temp = arr[left]
           arr[left] = arr[right]
           arr[right] = temp
   temp = arr[low]
   arr[low] = arr[right]
   arr[right] = temp
   return right

def merge_sort(arr) :
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i,j,k=0,0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr

