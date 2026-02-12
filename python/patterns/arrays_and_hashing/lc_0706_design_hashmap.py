'''
706. Design HashMap
'''
class MyHashMap(object):

    def __init__(self):
        self.hashmap = dict()   #initialize a dictionary

    def put(self, key, value):    #void
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashmap[key] = value

    def get(self, key):    #return int
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            return self.hashmap[key]
        else:
            return -1
        

    def remove(self, key):  #void
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashmap:
            del self.hashmap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)