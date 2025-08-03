import hashlib
import math


class CountingBloomFilter:
    """Counting Bloom Filter Implementation."""

    def __init__(self, expected_items: int, false_positive_rate: float):
        """Initialize the Counting Bloom Filter."""
        self.n = expected_items
        self.p = false_positive_rate

        self.size = self._get_size(self.n, self.p)
        self.k = self._get_hash_count(self.size, self.n)

        self.counter_array = [0] * self.size

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
        item = item.encode("utf-8")
        return [
            int(hashlib.md5(item + str(i).encode()).hexdigest(), 16) % self.size
            for i in range(self.k)
        ]
    
    def add(self, item: str | int) -> None:
        """Add an item to the Counting Bloom Filter."""
        hashes = self._hashes(item)
        for hash_val in hashes:
            self.counter_array[hash_val] += 1

    def remove(self, item: str | int) -> None:
        """Remove an item from the Counting Bloom Filter."""
        if not self.check(item):
            raise ValueError("Item not found in the Counting Bloom Filter.")
        
        for idx in self._hashes(item):
            self.counter_array[idx] -= 1
            

    def check(self, item: str | int) -> bool:
        """Check if an item is in the Counting Bloom Filter."""
        return all(self.counter_array[hash_val] > 0 for hash_val in self._hashes(item))
    

if __name__ == "__main__":
    """Implemenation of Counting Bloom Filter."""
    cbf = CountingBloomFilter(expected_items=100, false_positive_rate=0.01)

    cbf.add("apple")
    cbf.add("banana")
    cbf.add("apple")

    print(cbf.check("apple"))
    print(cbf.check("grape"))

    cbf.remove("apple")
    print(cbf.check("apple"))

    cbf.remove("apple")
    print(cbf.check("apple"))

    try:
        cbf.remove("apple")
    except ValueError as e:
        print(e)
    