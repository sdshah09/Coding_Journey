'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example
Example 1:

Input: ["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"

'''
from typing import (
    List
)
from collections import defaultdict,deque

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def dfs(self,node,visited,adj,res):
        if node in visited:
            return visited[node]
        visited[node] = True
        for i in adj[node]:
            self.dfs(i,visited,adj,res)
        visited[node] = False
        res.append(node)
    
    def bfs(self,words):
        n = len(words)
        adj = [[] for _ in range(26)]
        in_degree = [0] * 26
        all_chars = set()

        # Initialize the in-degree count and the set of all characters
        for word in words:
            for char in word:
                all_chars.add(char)
        print(all_chars)
        # Build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # Check for invalid order (prefix situation) # apple,app
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if ord(w2[j]) - ord('a') not in adj[ord(w1[j]) - ord('a')]:
                        adj[ord(w1[j]) - ord('a')].append(ord(w2[j]) - ord('a'))
                        in_degree[ord(w2[j]) - ord('a')] += 1
                    break

        # Initialize the queue with characters that have zero in-degree
        q = deque()
        for char in all_chars:
            if in_degree[ord(char) - ord('a')] == 0:
                q.append(ord(char) - ord('a'))

        # Perform BFS
        res = []
        while q:
            node = q.popleft()
            res.appenjd(chr(node + ord('a')))
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        # If result length does not match the number of unique characters, there's a cycle
        if len(res) != len(all_chars):
            return ""

        return ''.join(res)


    def alien_order(self, words: List[str]) -> str:
        n = len(words)
        adj = {c:set() for w in words for c in w}
        print(adj)
        for i in range(n-1):
            w1,w2 = words[i],words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit,res = {},[]
        for i in adj:
            if self.dfs(i,visited=visit,adj=adj,res=res):
                return ""
        res.reverse()
        ans = self.bfs(words)
        return "".join(res),ans
if __name__ == "__main__":
    sol = Solution()
    res = sol.alien_order(["wrt","wrf","er","ett","rftt"])
    print(res)