'''
424. Longest Repeating Character Replacement
Solved
Medium
Topics
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j =0,0
        freq = {}
        maxLen = 0
        while j<len(s):
            if s[j] not in freq:
                freq[s[j]]=0
            freq[s[j]]+=1
            if((j-i+1)-max(freq.values()))<=k:
                maxLen = max(maxLen,j-i+1)
            else:
                freq[s[i]]-=1
                if not freq[s[i]]:
                    del freq[s[i]]
                i+=1
            j+=1
        return maxLen
            

