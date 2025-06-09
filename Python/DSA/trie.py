class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def get_all_words(self):
        words = []
        self._dfs(self.root, "", words)
        return words

    def _dfs(self, node, path, words):
        if node.is_end:
            words.append(path)
        for ch, child in node.children.items():
            self._dfs(child, path + ch, words)

    
    def print_trie(self):
        print("root")
        self._print_recursive(self.root, prefix="  ")

    def _print_recursive(self, node, prefix):
        for i, (ch, child) in enumerate(node.children.items()):
            is_last = (i == len(node.children) - 1)
            branch = "└── " if is_last else "├── "
            mark = "*" if child.is_end else ""
            print(prefix + branch + ch + mark)
            next_prefix = prefix + ("    " if is_last else "│   ")
            self._print_recursive(child, next_prefix)


trie = Trie()


# Insert words into the trie
words = [
    "cat", "car", "can", "cart", "carbon",
    "dog", "door", "doll", "dorm", "dormant",
    "apple", "ape", "apex", "app", "apply",
    "bat", "batch", "bath", "banana"
]

for word in words:
    trie.insert(word)

# Search for exact words
# print(trie.search("cat"))  # True ✅
# print(trie.search("cab"))  # False ❌
# print(trie.search("bat"))  # True ✅
# print(trie.search("bats")) # False ❌


# Check for prefix
# print(trie.starts_with("ca"))   # True ✅
# print(trie.starts_with("bat"))  # True ✅
# print(trie.starts_with("dog"))  # False ❌

# Print all stored words
# all_words = trie.get_all_words()
# print("Words in Trie:", all_words)


trie.print_trie()