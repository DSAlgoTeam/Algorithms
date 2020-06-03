

class HashTable:
    def __init__(self):
        self.__table = [None] * 10 # default size of array is 10, increases as more elements are included
        self.__hashNo = len(self.__table)
        self.__prime = 7

    
    def __incr_table_size(self):
        self.__table.extend([None] * self.__hashNo)
        self.__hashNo *= 2
        self.__prime = self.__get_prime(self.__hashNo)
    
    def _is_table_full(self):
        return all()

    def __hash(self,key):
        '''
        returns hashed key
        '''
        if key is int:
            return key % self.__hashNo
        elif key is str:
            s = 0
            for i in key:
                s += ord(i)
            return s % self.__hashNo

    def get(self, key):
        '''
        Get the value of key saved in the hash table
        '''
        
        
    def __assign(self, hashkey, key, value):
        '''
        assign key value to the given hashkey
        '''
        if self.__table[hashkey] is not None:
            raise ValueError('Cannot assign at hashkey, slot not empty')

        self.__table[hashkey] = (key,value)


    def __linear_probe(self, key):
        '''
        
        '''
        return self.__hash(key) + 1

    def put(self, key, value):
        '''
        
        insert key value pair
        '''
        if not isinstance(key, (str, int)):
            raise TypeError("Current implementation only supports `str` and `int` as keys")
        if value is None:
            raise ValueError("Can't insert NoneType as value")

        self.__findKey(key)

        hashkey = self.__hash(key)
        if self.__table[hashkey] is None:
            self.__table[hashkey] = (key, value)
        if self.__hashNo < 20:
            while self.__table[hashkey] is not None:
                hashkey = self.__linear_probe(key)
        else:
            while self.__table[hashkey] is not None:
                hashkey = self.__quadratic_probe(key)
        self.__assign(hashkey, key, value)

    def __findKey(self, key):
        hashkey = self.__hash(key)

        if self.__table[hashkey][0] == key:
            return True
