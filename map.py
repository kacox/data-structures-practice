"""
Implementation of a Map Abstract Data Type using a hash table.

The map abstract data type is defined as follows. The structure is an
unordered collection of associations between a key and a data value. The
keys in a map are all unique so that there is a one-to-one relationship
between a key and a value. The operations are given below.

    Map() Create a new, empty map. It returns an empty map collection.

    put(key,val) Add a new key-value pair to the map. If the key is already
        in the map then replace the old value with the new value.

    get(key) Given a key, return the value stored in the map or None
        otherwise.

    del Delete the key-value pair from the map using a statement of the
        form del map[key].
    
    len() Return the number of key-value pairs stored in the map.

    in Return True for a statement of the form key in map, if the given key
        is in the map, False otherwise.

"""


class Map:
    """A Map abstract data type."""

    def __init__(self):
        """Create an empty Map object."""
        self.size = 11

        # will hold the keys
        # treat the key list as a hash table
        self.slots = [None for slot in range(self.size)]

        # will hold the values
        self.data = [None for slot in range(self.size)]

    def hash_function(self, key):
        """
        Implementation of the simple remainder method.

        Returns a hash value.
        """
        return key % self.size

    def rehash(self, oldhash):
        """
        The collision resolution technique is linear probing with a 'plus 1'
        rehash function.
        """
        return (oldhash + 1) % self.size

    def put(self, key, val):
        """
        Add a new key-value pair to the map. If the key is already
        in the map then replace the old value with the new value.

        If a slot is already occupied, rehash the hash value. Rehashing
        iterates until an empty slot occurs. 
        """
        hashvalue = self.hash_function(key)

        if self.slots[hashvalue] is None:
            # slot is unoccupied
            self.slots[hashvalue] = key
            self.data[hashvalue] = val
        else:
            # slot is occupied
            if self.slots[hashvalue] == key:
                # same key; replace value (update)
                self.data[hashvalue] = val
            else:
                # collision resolution
                next_slot = self.rehash(hashvalue)
                while self.slots[next_slot] is not None and \
                                    self.slots[next_slot] != key:
                    # look for next empty slot
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = val
                else:
                    # replace
                    self.data[next_slot] = val

    def get(self, key):
        """Look up a value in the hash table using the key."""
        hashvalue = self.hash_function(key)

        if self.slots[hashvalue] == key:
            return self.data[hashvalue]
        else:
            # start looking elsewhere; rehash
            next_slot = self.rehash(hashvalue)
            while next_slot != hashvalue:
                if self.slots[next_slot] == key:
                    return self.data[next_slot]


    def delete(self):
        pass

    def len():
        pass

    def __repr__(self):
        """Human-readable version of map."""
        ans = "< "
        for key, val in zip(self.slots, self.data):
            ans += "{}:{}, ".format(key, val)
        ans = ans.strip().rstrip(",")
        ans += " >"
        return ans


if __name__ == '__main__':
    a_map = Map()
    a_map.put(11, "green")
    a_map.put(13, "blue")
    a_map.put(17, "purple")
    # test collision resolution
    a_map.put(22, "red")
