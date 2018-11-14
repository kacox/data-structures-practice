"""
Naive implementation for a Hash Table w/ linear probing. Duplicates
allowed.
"""

import hashlib


class HashTable:

    def __init__(self, size):
        self._size = size
        self.table = ["_" for _ in range(size)]

    def add(self, key):
        """Adds a key to the hash table."""
        addition_idx = self._reduce(self._hash(key))

        if self.table[addition_idx] != "_":
            # collision
            new_idx = self._resolve_collision(addition_idx)
            if new_idx == addition_idx:
                # table is full; do not insert
                print("Did not add key: hash table is full!")
            else:
                # found a new
                self.table[new_idx] = key
        else:
            # no collision; place value at index
            self.table[addition_idx] = key

    def _resolve_collision(self, original_indx):
        """Returns an unoccupied index."""
        new_idx = original_indx
        empty = False

        while not empty:
            # get new index w/ linear probing
            new_idx = (new_idx + 1) % self._size

            # make sure we are not where we started (full)
            if new_idx == original_indx:
                break

            # update empty
            empty = (self.table[new_idx] == "_")

        # now you either have an empty index or the original index
        return new_idx


    def _hash(self, key):
        """Hashes the key."""
        hash_fxn = hashlib.sha1(bytes(str(key), encoding="ascii"))
        return hash_fxn.hexdigest()

    def _reduce(self, hash):
        """Returns an index based on the hash."""
        summation = 0
        for char in hash:
            summation += ord(char)
        return summation % self._size

    def remove(self, key):
        """Removes a key from the hash table."""
        pass

    def membership(self, key):
        """Returns a boolean indicating presence of key."""
        pass

    def __repr__(self):
        """Display contents of the hash table."""
        return "[" + ", ".join([str(member) for member in self.table]).rstrip(",") + "]"


if __name__ == '__main__':
    h = HashTable(11)