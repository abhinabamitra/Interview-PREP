"""Tries Data Structure."""
class TrieNode:

    def __init__(self) -> None:
        """Initialize the TrieNode."""
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self) -> None:
        """Initialize the Trie."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root # node is root node
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Search for a word in the trie."""
        node = self.root # node is root node
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix: str) -> bool:
        """Check if a prefix exists in the trie."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def _dfs(self, node: TrieNode, prefix: str, results: list[str], limit: int) -> None:
        if len(results) == limit:
            return  # Stop once limit is reached
        if node.is_end:
            results.append(prefix)
        for char in sorted(node.children):  # sort to return alphabetically
            self._dfs(node.children[char], prefix + char, results, limit)


    def autocomplete(self, prefix, limit=5):
        prefix = prefix.lower()
        current = self.root
        results = []

        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        self._dfs(current, prefix, results, limit)
        return results


if __name__ == "__main__":
    trie = Trie()

    words = ["apple", "app", "banana", "bat", "ball", "cat", "dog", "doge"]

    for word in words:
        trie.insert(word)

    print(trie.autocomplete(prefix="app", limit=5))

    # print(trie.search("apple"))
    # print(trie.starts_with("app"))
    # print(trie.search("app"))
    # print(trie.starts_with("bat"))
    # print(trie.search("call"))

