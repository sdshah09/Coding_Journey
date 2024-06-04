'''
409. Longest Palindrome
Solved
Easy
Topics
Companies
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
732K
Submissions
1.3M
Acceptance Rate
54.8%

'''

class Solution:
    def countOccurence(self,s):
        p = {}
        for i in s:
            if i not in p:
                p[i] = 0
            p[i]+=1
        return p
    def longestPalindrome(self, s: str) -> int:
        p = self.countOccurence(s)
        maxCount = 0
        odd = False
        for j in p.keys():
            if p[j]%2==0:
                maxCount+=p[j]
            else:
                odd = True
                maxCount += p[j]-1
        if odd:
            maxCount+=1
        return maxCount