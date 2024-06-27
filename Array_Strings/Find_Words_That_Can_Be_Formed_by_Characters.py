'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

'''
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}
        summ = 0
        for i in chars:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
        for word in words:
            flag = 1
            freq1 = freq.copy()
            for i in word:
                if i not in freq1 or freq1[i]==0:
                    flag = 0
                    break
                freq1[i]-=1
            if flag:
                summ+=len(word)
        return summ
            
