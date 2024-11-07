'''
a trie is useful because it provides fast string look-ups
'''
class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False
        

    # Check if the node contains
    # a specific key (letter)
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    # Insert a new node with a specific
    # key (letter) into the Trie
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    # Get the node with a specific
    # key (letter) from the Trie
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    # Set the current node
    # as the end of a word
    def setEnd(self):
        self.flag = True

    # Check if the current node
    # marks the end of a word
    def isEnd(self):
        return self.flag
    

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    def insert_key(self,s):
        curr = self.root
        for c in s:
            if not curr.containsKey(c):
                curr.put(c,Node())
            curr = curr.get(c)
        curr.setEnd()

    def search_key(self,s):
        curr = self.root
        for c in s:
            if not curr.containsKey(c):
                return False
            curr = curr.get(c)
        return curr.isEnd()

    def starts_with(self,s):
        curr = self.root
        for c in s:
            if not curr.containsKey(c):
                return False
            curr = curr.get(c)
        return True

if __name__ == "__main__":
    trie = Trie()
    print("Inserting words: Striver, Striving, String, Strike")
    trie.insert_key("striver")
    trie.insert_key("striving")
    trie.insert_key("string")
    trie.insert_key("strike")

    print("Search if Strawberry exists in trie: " +
          ("True" if trie.search_key("strawberry") else "False"))

    print("Search if Strike exists in trie: " +
          ("True" if trie.search_key("strike") else "False"))

    print("If words in Trie start with Stri: " +
          ("True" if trie.starts_with("stri") else "False"))
                           
