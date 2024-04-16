'''Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Sliding window
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c_dict = {}

        # Count the characters in string t
        for i in t:
            if i in c_dict:
                c_dict[i] += 1
            else:
                c_dict[i] = 1

        counter = len(c_dict)
        begin, end = 0, 0
        length = float('inf')
        ans = ""

        while end < len(s):
            end_char = s[end]

            if end_char in c_dict:
                c_dict[end_char] -= 1
                if c_dict[end_char] == 0:
                    counter -= 1

            end += 1

            while counter == 0:
                if end - begin < length:
                    length = end - begin
                    ans = s[begin:end]

                begin_char = s[begin]

                if begin_char in c_dict:
                    c_dict[begin_char] += 1
                    if c_dict[begin_char] > 0:
                        counter += 1

                begin += 1

        return ans

# Test case
sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print("Test Case: S = '{}', T = '{}'".format(s, t))
ans = sol.minWindow(s, t)
print(ans)