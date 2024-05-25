'''
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
16.6M
Acceptance Rate
34.8%


Topics:- Sliding Window. 
'''

from collections import defaultdict
class Solution:
    def longestSubString(self,string):
        string_dict = defaultdict()
        left,max_len = 0,0
        for i in range(len(string)):
            string_dict[string[i]] = 1+string_dict.get(string[i],0)
            while string_dict[string[i]] > 1:
                string_dict[string[left]]-=1
                left+=1
            max_len = max(max_len,i-left+1)
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubString("bbbbbbb"))
            
