#import sympy 
PRIME = 7


def hash(Hash_table,key) :
    if type(key) == int :
        return  int(key) % len(Hash_table)
    else :
        sum = 0
        for i in key :
            sum += ord(i)
        return sum % len(Hash_table)
    


def set_hashtable_size(N = 11):
    if not isinstance(N,int) :
        raise Exception('int type parameter expected')
    #if not sympy.isprime(N) :
    #    raise Exception('A prime number was expected')
    return [None]*N

def rehash_linear(pos,length) :
    return (pos + 1)%length

def rehash_quadratic(pos,i,length) :
    return (pos + (i**2))%length

def rehash(pos) :
    return  PRIME - (pos//PRIME)

def insert(Hash_table,key) :
    length = len(Hash_table)
    hash_key = hash(Hash_table,key)
    if Hash_table[hash_key] is None or Hash_table[hash_key] == 'deleted' :
        Hash_table[hash_key] = key
    else :
        flag = False
        
        i = rehash_linear(hash_key,length)
        while i != hash_key and not flag :
            if Hash_table[i] is None  or  Hash_table[i] == 'deleted':
                Hash_table[i] = key
                flag = True
            i = rehash_linear(i,length)
        
        if flag == False :
            raise Exception("Hash Table is Full")

def search(Hash_table,key) :
    length = len(Hash_table)
    hash_key = hash(Hash_table,key)
    if Hash_table[hash_key] == key :
        return True
    elif Hash_table[hash_key] is None :
        return False 
    else :    
        i = rehash_linear(hash_key,length)
        while i != hash_key  :
            if Hash_table[i] == key :
                return True
            if Hash_table[i] is None  :
                return False    
            i = rehash_linear(i,length)
    return False 

def delete(Hash_table,key) :
    length = len(Hash_table)
    hash_key = hash(Hash_table,key)
    
    if Hash_table[hash_key] == key :
        Hash_table[hash_key] ='deleted'
        return True
    elif Hash_table[hash_key] is None :
        raise Exception('Can\'t delete an Non-existent Key')
    
    else :
        i = rehash_linear(hash_key,length)
        while i != hash_key  :
            if Hash_table[i] == key :
                Hash_table[hash_key] ='deleted'
                return True
            if Hash_table[i] is None  :
                return False    
            i = rehash_linear(i,length)
    return False 


