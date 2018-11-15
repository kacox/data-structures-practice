"""
Naive implementation of a dictionary using a hash table.

Keys must number data types (might expand later).
"""


class Dictionary:
    """A dictionary abstract data structure."""

    def __init__(self):
        """Create an empty dictionary object."""
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
        Add a new key-value pair to the dictionary. If the key is already
        in the dictionary then replace the old value with the new value.

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
                next_slot = self.rehash(next_slot)

            return "{} not in dictionary.".format(key)


    def delete(self, key):
        """Delete an item by key."""
        hashvalue = self.hash_function(key)

        if self.slots[hashvalue] == key:
            self.slots[hashvalue] = None
            self.data[hashvalue] = None
        else:
            # start looking elsewhere; rehashgit 
            next_slot = self.rehash(hashvalue)

            while next_slot != hashvalue:
                if self.slots[next_slot] == key:
                    self.slots[next_slot] = None
                    self.data[next_slot] = None
                    return
                else:
                    next_slot = self.rehash(next_slot)

            return "{} not in dictionary.".format(key)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, key):
        """Returns whether or not key is in the dictionary."""
        for element in self.slots:
            if element == key:
                return True
        return False

    def __repr__(self):
        """Human-readable version of dictionary."""
        ans = "< "
        for key, val in zip(self.slots, self.data):
            ans += "{}:{}, ".format(key, val)
        ans = ans.strip().rstrip(",")
        ans += " >"
        return ans


if __name__ == '__main__':
    d = Dictionary()
    d.put(11, "green")
    d.put(13, "blue")
    d.put(17, "purple")
    # test collision resolution
    d.put(22, "red")
