'''
438. Find All Anagrams in a String
Solved
Medium
Topics
Companies
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
876.3K
Submissions
1.7M
Acceptance Rate
51.0%

Approach:- We are given a fixed sized string from which we have to find the anagram in the big string
This is a problem of sliding window

Time Complexity:- O(N)
Space Complexity:- O(1)

Also this question can be asked as

Count Occurences of Anagrams

'''

class Solution:
    def findAnagrams(self,s,p):
        p_dict = {}
        index=[]
        for i in p:
            if i in p_dict:
                p_dict[i]+=1
            else:
                p_dict[i]=1
        i,j=0,0
        occurence = 0
        count = len(p_dict)
        while j<len(s):
            if s[j] in p_dict:
                p_dict[s[j]]-=1
                if p_dict[s[j]]==0:
                    count-=1
            while count==0:
                if (j-i+1)==len(p):
                    index.append(i)
                    occurence+=1
                if s[i] in p_dict:
                    p_dict[s[i]]+=1
                    if p_dict[s[i]]>0:
                        count+=1
                i+=1
            j+=1
        return index,occurence

if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams("aabaabaa","aaba"))