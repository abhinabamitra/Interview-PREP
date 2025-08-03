import hashlib
import random

class CuckooFilter:
    """Cuckoo Filter Implementation."""

    def __init__(self, size: int, bucket_size: int, fp_size: int, max_kicks: int = 500):
        """Initialize the Cuckoo Filter."""
        self.size = size
        self.bucket_size = bucket_size
        self.fp_size = fp_size
        self.max_kicks = max_kicks

        self.buckets = [[] for _ in range(self.size)]

    def _cuckoo_hash(self, item: str | int) -> int:
        """Cuckoo Hash Function."""
        return int(hashlib.md5(item.encode()).hexdigest(), 16)
    
    def _fingerprint(self, item: str | int) -> str:
        """Generate fingerprint for item."""
        h = self._cuckoo_hash(item)
        return format(h, 'x')[:self.fp_size]
    
    def _index1(self, item: str | int) -> int:
        """Generate index for item."""
        h = self._cuckoo_hash(item)
        return h % self.size
    
    def _index2(self, index1: int, fp: str) -> int:
        """Generate index for item."""
        h = self._cuckoo_hash(fp)
        return (index1 ^ h) % self.size
    
    def insert(self, item: str | int) -> bool:
        """Insert item into Cuckoo Filter."""
        fp = self._fingerprint(item)
        index1 = self._index1(item)
        index2 = self._index2(index1, fp)

        for i in [index1, index2]:
            if len(self.buckets[i]) < self.bucket_size:
                self.buckets[i].append(fp)
                return True
            
        # Kick out logic
        i = random.choice([index1, index2])
        for _ in range(self.max_kicks):
            if len(self.buckets[i]) == 0:
                self.buckets[i].append(fp)
                return True
                
            j = random.randint(0, len(self.buckets[i]) - 1)
            kicked_fp = self.buckets[i][j]
            self.buckets[i][j] = fp
            
            kicked_index1 = self._index1(kicked_fp)
            kicked_index2 = self._index2(kicked_index1, kicked_fp)
            
            if i == kicked_index1:
                i = kicked_index2
            else:
                i = kicked_index1
                
            fp = kicked_fp
            
            if len(self.buckets[i]) < self.bucket_size:
                self.buckets[i].append(fp)
                return True
            
        return False # Insertion failed
    
    def lookup(self, item: str | int) -> bool:
        """Lookup item in Cuckoo Filter."""
        fp = self._fingerprint(item)
        index1 = self._index1(item)
        index2 = self._index2(index1, fp)

        return fp in self.buckets[index1] or fp in self.buckets[index2]
    
    def delete(self, item: str | int) -> bool:
        """Delete item from Cuckoo Filter."""
        fp = self._fingerprint(item)
        index1 = self._index1(item)
        index2 = self._index2(index1, fp)

        for i in [index1, index2]:
            if fp in self.buckets[i]:
                self.buckets[i].remove(fp)
                return True
            
        return False
    

if __name__ == "__main__":
    cf = CuckooFilter(size=11, bucket_size=2, fp_size=4)

    for word in ['dog', 'cat', 'fish', 'horse']:
        print(f"Inserting {word}: {cf.insert(word)}")

    print(cf.buckets)

    print("\nChecking membership:")
    for word in ['dog', 'cat', 'bird']:
        print(f"{word} in filter? {cf.lookup(word)}")

    print("\nDeleting dog...")
    cf.delete('dog')
    print("dog in filter?", cf.lookup('dog'))  