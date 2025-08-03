import random

class SkipListNode:

    def __init__(self, value: int, level: int):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:

    MAX_LEVEL = 4
    P = 0.5 # Probability for level increase

    def __init__(self):
        self.head = SkipListNode(value=None, level=self.MAX_LEVEL)
        self.level = 0


    def _random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl
    
    def insert(self, value: int):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head

        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        # getting random level for this node
        level = self._random_level()

        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.head
            self.level = level

        # Update forward pointers
        new_node = SkipListNode(value=value, level=level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node


    def search(self, value: int):
        current = self.head
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        return current.forward[0] and current.forward[0].value == value
    
    @property
    def display(self):
        print("\nSkip List:")
        for i in range(self.level + 1):
            level_nodes = []
            node = self.head.forward[i]
            while node:
                level_nodes.append(str(node.value))
                node = node.forward[i]
            print(f"Level {i}: {' -> '.join(level_nodes)}")


if __name__ == "__main__":
    s = SkipList()
    for val in [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]:
        s.insert(val)

    s.display

    print("\nSearch 19:", s.search(19))  # True
    print("Search 15:", s.search(15))    # False