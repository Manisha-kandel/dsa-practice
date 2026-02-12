'''
705. Design HashSet
'''
class MyHashSet(object):

    def __init__(self):
        self.hashset =  set()   #initialization

    def add(self, key):   #void
        """
        :type key: int
        :rtype: None
        """
        self.hashset.add(key)

    def remove(self, key):  #void
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key):   #return 
        """
        :type key: int
        :rtype: bool
        """
        return key in self.hashset
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)