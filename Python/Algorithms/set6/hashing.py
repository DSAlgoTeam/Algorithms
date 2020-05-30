def hash_func(num = None, mod = 10):
    if num is not None: return num % mod    #linear_probing
    # return num + num**2    #quadratic probing
    # return [num % 13] + [8 - num % 8]     #double hasing 



def getIndex(num = None, hash_table = None) -> int:
    '''
    function: return index of num if its in the hash table (closed hashing)'''
    n = len(hash_table)
    h = hash_func((hash_func(num) + 0), n)
    if hash_table[h] == num: return h
    j, flag = 1, True
    while j < len(hash_table):
            h = hash_func((hash_func(num) + hash_func(j)), n)
            if hash_table[h] == num: break
            j += 1
    if j < n: return h
    return -1
    



def closed_hashing(arr = None):
    '''
    use hash function to store elements in hash table
    '''
    n = len(arr)
    hash_table = [None] * n
    for i in arr:
        j = 0
        h = hash_func((hash_func(i) + j), n)
        # while hash_table(h) and j < len(hash_table):
        while hash_table[h]:
            j += 1
            h = hash_func((hash_func(i) + hash_func(j)), n) 
            # print(h)  
        if j < len(hash_table): hash_table[h] = i
        else: print("list overflow")
    return hash_table






if __name__ == "__main__":
    arr = [10,29,31,48,55]
    hash_table = closed_hashing(arr)
    print(hash_table)
    print(getIndex(4, hash_table))