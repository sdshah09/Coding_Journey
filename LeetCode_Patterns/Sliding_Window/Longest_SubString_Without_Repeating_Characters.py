'''
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
5.8M
Submissions
16.7M
Acceptance Rate
34.9%

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        i,j=0,0
        maxCount = 0
        while j<len(s):
            if s[j] not in freq:
                freq[s[j]]=0
            freq[s[j]]+=1
            while freq[s[j]]>1 and i<=j:
                freq[s[i]]-=1
                i+=1
            maxCount = max(maxCount,j-i+1)
            j+=1
        return maxCount