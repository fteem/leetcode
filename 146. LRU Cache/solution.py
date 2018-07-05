from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self._cache = OrderedDict()        

    def get(self, key):
        if key not in self._cache:
            return -1
        value = self._cache.pop(key)
        # append key-value pair internal queue
        self._cache[key] = value
        return value

    def put(self, key, value):
        if key in self._cache:
            self._cache.pop(key)
        else:
            # we always set a key, so >=
            if len(self._cache) >= self.capacity:
                # item in front is the least recently used
                self._cache.popitem(last=False)
        self._cache[key] = value


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert(cache.get(1) == 1)
    cache.put(3, 3)
    assert(cache.get(2) == -1)
    cache.put(4, 4)
    assert(cache.get(1) == -1)
    assert(cache.get(3) == 3)
    assert(cache.get(4) == 4)