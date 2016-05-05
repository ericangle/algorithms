'''A dictionary class implemented by hashing and chaining. The set is
represented internally by a list of lists. The outer list is initialized to
all None's.  When multiple values hash to the same location (a collision),
new values are appended to the list at that location. The list is rehashed
when ~75% full.  The size starts at 10 and doubles with each rehash. The
first value of a sublist is the key, the second the value.

The initial list is:
[None, None, None, None, None, None, None, None, None, None]

After 0,"zero" 1, "one", and 10,"ten" have been inserted, it will be:
[[[0, "zero"],[10, "ten"]], [[1, "one"]], None, None, None, ...]
'''

class my_hash_set:
    def __init__(self, init=None):
        self.__limit = 10
        self.__items = [None] * self.__limit
        self.__count = 0

        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        return(self.__count)

    def __flattened(self):
        flattened = filter(lambda x: x != None, self.__items)
        flattened = [item for inner in flattened for item in inner]
        return(flattened)

    def __iter__(self):
        return(iter(self.__flattened())) 

    def __str__(self):
        return(str(self.__flattened()))

    def __setitem__(self, key, value):
        h = hash(key) % self.__limit

        collision = False

        # if None, set it
        if not self.__items[h]:
            self.__items[h] = [[key, value]]

        # if collision, append to current list if key not already used 
        else:
            for item in self.__items[h]:
                if item[0] == key:
                    self.__items[h].remove(item)
                    collision = True
                    break
  
            self.__items[h].append([key, value])

        if not collision:
            self.__count += 1

        if (0.0 + self.__count) / self.__limit > 0.75:
            self.__rehash()

    def __rehash(self):
        self.__limit = 2 * self.__limit
        flat = self.__flattened()  
        self.__items = [None] * self.__limit
        self.__count = 0

        for item in flat:
            self.__setitem__(item[0],item[1]) 

    def __contains__(self, key):
        h = hash(key) % self.__limit

        if self.__items[h]:
            for item in self.__items[h]:
                if item[0] == key:
                    return True
            
        return False
            
    def __getitem__(self, key):
        h = hash(key) % self.__limit

        if self.__items[h]:
            for item in self.__items[h]:
                if item[0] == key:
                    return item[1]

        raise KeyError 

    def __delitem__(self, key):
        h = hash(key) % self.__limit

        found = False

        if self.__items[h]:
            for item in self.__items[h]:
                if item[0] == key:
                    self.__items[h].remove(item)
                    self.__count -= 1
                    found = True

        if not found:
            raise KeyError
