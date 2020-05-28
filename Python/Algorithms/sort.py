def radix_sort(arr = None):
    
    div, m, flag = 1, 10, True
    while flag:
        flag = False
        bucket = [[], [], [], [], [], [], [], [], [], []]
        # bucket = [[None]] * 10
        for i in arr:
            index = (i % m) // div
            bucket[index].append(i)
            if index > 0:
                flag = True
        arr = []
        for i in bucket:
            for j in i:
                arr.append(j)
        m *= 10
        div *= 10
    return arr


def count_sort(arr = None):

    freq = [0 for i in range(256)]
    result = [None] * len(arr)
    for i in arr:
        freq[ord(i)] += 1
    for i in range(1, len(freq)):
        freq[i] += freq[i-1]
    
    for i in range(len(arr)):
        result[freq[ord(arr[i])] -1] = arr[i]
        freq[ord(arr[i])] -= 1
    return ''.join(result)


def merge_sort(arr = None):

    def merge(arr1, arr2):
        i,j=0,0
        result = []
        
        while(i<len(arr1) and j < len(arr2)):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        
        while i<len(arr1):
                result.append(arr1[i])
                i += 1
        
        while j<len(arr2):
                result.append(arr2[j])
                j += 1
        
        return result

    if len(arr) >1:
        mid = len(arr)//2
        merge_sort(arr[:mid])   
        merge_sort(arr[mid:])   
        return merge(arr[:mid], arr[mid:])
        

def heap_sort(arr):

    def heapify(index):
        parent = index
        left_child = (2*parent) + 1
        right_child = (2*parent) + 2

        if left_child < len(arr) and arr[parent] < arr[left_child]  :
            arr[left_child], arr[parent] =  arr[parent], arr[left_child]
            heapify(parent)

        if right_child < len(arr) and arr[parent] < arr[right_child] :
            arr[right_child], arr[parent] =  arr[parent], arr[right_child]
            heapify(parent)
    
    i = (len(arr) // 2) -1
    while i >= 0:
        heapify(i)
        i -= 1

    i = len(arr)-1
    while i>0:
        arr[i], arr[0] = arr[0], arr[i]
        i -= 1

    return arr

if __name__=="__main__":
    arr = [1,3,2,5,4]
    print(heap_sort(arr))