'''
127. Word Ladder
Solved
Hard
Topics
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

Time Complexity: O(M * L)
Space Complexity: O(M + L)

'''
from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = deque()
        q.append((beginWord,1))

        # This is a visited hashmap which will keep the track of word in the array and check if it is visited or not. So maybe there are multiple same words then we don't have to inceaste the level because if it is in the previous level meaning it is of no use and it will increase the distance only.

        visited = {} 
        for i in wordList:
            visited[i]=1
        visited[beginWord]=0
        
        while q:
            node = q.popleft()
            wordList = list(node[0])
            if node[1]>1 and node[0]==endWord:
                return node[1]
            for i in range(0,len(wordList)): # This loop will change each and every letter of the word and try 26 different combinations and check if the word is in hashmap or not. If it is in the hashmap it will change it's status to visited and increase the level for the next word
                val = wordList[i] #  ['h','a','t']
                for j in range(0,26): # Change for h,a and t and after cmpleting all the combinations we need the original word back so we can try differnt combinations for the next letter.
                    wordList[i] = chr(ord('a')+j)
                    modifyWord = ''.join(wordList)
                    if modifyWord in visited:
                        if(visited[modifyWord]) == 1 and (modifyWord!=node[0]):
                            q.append((modifyWord,node[1]+1)) 
                            visited[modifyWord]=0
                wordList[i] = val # Keeping the original word instead of manipulating it
        return 0

        