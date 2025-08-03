import hashlib

class CountMinSketch:

    def __init__(self, width: int, depth: int, seed: int = 0):
        self.width = width
        self.depth = depth
        self.seed = seed

        self.table = [[0] * width for _ in range(depth)]

    def _hash(self, item: str, i: int) -> int:
        """Hash function for item."""
        h = hashlib.md5(f"{self.seed + i}_{item}".encode()).hexdigest()
        return int(h, 16) % self.width
    
    def add(self, item: str, count: int = 1):
        """Update the count for an item."""
        for i in range(self.depth):
            idx = self._hash(item, i)
            self.table[i][idx] += count

    def estimate(self, item: str) -> int:
        """Estimate the count for an item."""
        estimates = []
        for i in range(self.depth):
            idx = self._hash(item, i)
            estimates.append(self.table[i][idx])
        return min(estimates)
    
    def __str__(self):
        return "\n".join(f"Row {i+1}: {row}" for i, row in enumerate(self.table))
    
if __name__ == "__main__":
    cms = CountMinSketch(width=20, depth=5)
    # print(cms)

    data_stream = ["apple", "banana", "apple", "orange", "banana", "apple", "apple", "grape"]

    for item in data_stream:
        cms.add(item)

    print(cms)

    print("\nEstimated counts:")
    for item in ["apple", "banana", "orange", "grape"]:
        print(f"{item}: {cms.estimate(item)}")