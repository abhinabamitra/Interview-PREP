"""Bloom Filter Implementation."""
import hashlib
import math
import bitarray

class BloomFilter:
    """Bloom Filter Implementation."""

    def __init__(self, expected_items: int, false_positive_rate: float):
        """Initialize the Bloom Filter."""
        self.n = expected_items
        self.p = false_positive_rate

        self.size = self._get_size(self.n, self.p)
        self.k = self._get_hash_count(self.size, self.n)

        # self.bit_array = [0] * self.size
        # self.hash_functions = [self.hash_function1, self.hash_function2]
        self.bit_array = bitarray.bitarray(self.size)
        self.bit_array.setall(0)

    # We are using this formula to calculate the size of optimal size of the bit array.
    # Comes from the Bloom Filter theory.
    # - minimizing the memory usage,
    # - minimizing the false positive rate below a certain target p.
    def _get_size(self, expected_items: int, false_positive_rate: float) -> int:
        """Calculate the size of the bit array m."""
        m = - (expected_items * math.log(false_positive_rate)) / (math.log(2) ** 2)
        return int(m)
    
    def _get_hash_count(self, size: int, expected_items: int) -> int:
        """Calculate the optimal number of hash functions k."""
        k = (size / expected_items) * math.log(2)
        return int(k)
    
    def _hashes(self, item: str | int) -> list[int]:
        """Generate hash functions."""
        hashes = []
        item = item.encode("utf-8")
        for i in range(self.k):
            digest = hashlib.md5(item + str(i).encode()).hexdigest()
            hash_val = int(digest, 16) % self.size
            hashes.append(hash_val)
        return hashes
    
    def add(self, item: str | int):
        """Add an item to the Bloom Filter."""
        hashes = self._hashes(item)
        for hash_val in hashes:
            self.bit_array[hash_val] = 1

    def check(self, item: str | int) -> bool:
        """Check if an item is in the Bloom Filter."""
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))
    

if __name__ == "__main__":
    """Implemenation of Bloom Filter."""
    bloom = BloomFilter(expected_items=100, false_positive_rate=0.01)

    # print(bloom.size)
    # print(bloom.k)

    bloom.add("apple")
    bloom.add("banana")

    print(bloom.check("apple"))
    print(bloom.check("banana"))

    print(bloom.bit_array)

    print(bloom.check("cherry"))
    print(bloom.check("grape")) # Possibly False ( Maybe True )
