from collections.abc import Iterable

class Trie:
    def __init__(self, iterable = None):
        '''
        Constructor for a trie, takes optional iterable
        '''

        if not isinstance(iterable, (Iterable, type(None))):
            raise ValueError("Can't make a trie without an iterable.")

        self.trie = {}
        if iterable:
            for i in iterable:
                self.insert(i)

    def insert(self, word):
        '''
        insert value into trie
        '''
        if not isinstance(word, (Iterable, str)):
            raise ValueError('The word parameter should be str or an iterable')
        node = self.trie
        for i in word:
            if i not in node:
                node[i] = {}
            node = node[i]
        node['$'] = True  # End of word
    
    def search(self, word):
        '''
        search for the word in the trie
        returns True if the word is found, else returns False
        '''
        if not isinstance(word, (Iterable, str)):
            raise ValueError('The word parameter should be str or an iterable')
        node = self.trie
        for i in word:
            if i not in node:
                return False
            node = node[i]
        return '$' in node # checks if the word ends at the last element or not
    
    def startsWith(self, prefix):
        '''
        Checks if the prefix exists in the trie
        '''
        if not isinstance(prefix, (Iterable, str)):
            raise ValueError('The word parameter should be str or an iterable')

        node = self.trie
        for i in prefix:
            if i not in node:
                return False
            node = node[i]
        return True