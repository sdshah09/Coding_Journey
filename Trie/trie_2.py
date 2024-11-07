'''
 Implement Trie ll
Moderate
80/80
Average time to solve is 30m
Contributed by
208 upvotes
Asked in companies
Problem statement
Ninja has to implement a data structure ”TRIE” from scratch. Ninja has to complete some functions.

1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.
Note:

1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.

2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.
Can you help Ninja implement the "TRIE" data structure?

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= “T” <= 50
1 <= “N” <= 10000
 “WORD” = {a to z}
1 <= | “WORD” | <= 1000

Where “T” is the number of test cases, “N” denotes how many times the functions(as discussed above) we call, “WORD” denotes the string on which we have to perform all the operations as we discussed above, and | “WORD” | denotes the length of the string “WORD”.

Time limit: 1 sec.
Sample Input 1:
1
5
insert coding
insert ninja
countWordsEqualTo coding
countWordsStartingWith nin
erase coding
Sample Output 1:
1
1   

'''
from os import *
from sys import *
from collections import *
from math import *
from os import *
from sys import *
from collections import *
from math import *

class Node:
    def __init__(self):
        self.child = [None]*26
        self.count_prefix = 0
        self.count_end = 0
    def containsKey(self,c):
        return self.child[ord(c)-ord('a')]!=None
    def put(self,c,node):
        self.child[ord(c)-ord('a')] = node
    def get(self,c):
        return self.child[ord(c)-ord('a')]



class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if not cur.containsKey(ch):
                cur.put(ch,Node())
            cur = cur.get(ch)
            cur.count_prefix+=1
        cur.count_end+=1

    def countWordsEqualTo(self, word):
        cur = self.root
        for ch in word:
            if not cur.containsKey(ch):
                return 0
            cur = cur.get(ch)
        return cur.count_end

    def countWordsStartingWith(self, word):
        cur = self.root
        for ch in word:
            if not cur.containsKey(ch):
                return 0
            cur = cur.get(ch)
        return cur.count_prefix
        


    def erase(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
                node.count_prefix-=1
            else:
                return
        node.count_end-=1
