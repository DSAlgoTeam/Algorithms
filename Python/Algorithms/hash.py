        
def hash(num, key):
    '''
    returns hash key for key in the arr
    '''
    if key is int:
        return key % num
    else:
        s = 0
        for i in key:
            s += ord(i)
        return s % num

def double_hash(arr, key, prime):
    '''
    use double hash to avoid collision and clustering
    '''
    hashkey = hash(len(arr),key)
    primehash = _prime_hash(prime, key)
    i = 1
    while arr[hashkey] is not None:
        hashkey = (hashkey + i * primehash) % len(arr)
        i += 1
    return hashkey

def _prime_hash(prime, key):
    '''
    helper second hash function for double hash
    '''
    if key is int:
        return prime - (key % prime)
    if key is str:
        s = 0
        for i in key:
            s += ord(i)
        return prime - (s % prime)


def linear_probe(arr, key):
    '''
    linear probing to avoid collision
    '''
    hashkey = hash(len(arr),key)
    i = 1
    while arr[hashkey] is not None:
        hashkey = (hashkey + i) % len(arr)
        i += 1
    return hashkey

def quadratic_probe(arr, key):
    '''
    quadratic probing to aoid collision and clustering
    '''
    hashkey = hash(len(arr),key)
    i = 1
    while arr[hashkey] is not None:
        hashkey = (hashkey + i*i) % len(arr)
        i += 1
    return hashkey