'''
1189. Maximum Number of Balloons
Solved
Easy
Topics
Companies
Hint
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.

'''
from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        freq = defaultdict()
        for i in text:
            if i in s:
                freq[i] = freq.get(i,0)+1
        ballon = {
            "b":1,
            "a":1,
            "l":2,
            "o":2,
            "n":1
        }

        if sum(freq.values())<len(s):
            return 0
        max_balloons = float('inf')
        for i,j in ballon.items():
            if i in freq:
                max_balloons = min(max_balloons,freq[i]//j)
            else:
                return 0
        return max_balloons
    def maxNumberOfBalloons2(self, text: str) -> int:
        s = "balloon"
        freq = defaultdict(int)
        
        # Count the frequency of each character in the given text
        for char in text:
            if char in s:
                freq[char] += 1
        
        # Calculate the number of times we can form "balloon"
        balloon_count = freq['b']
        balloon_count = min(balloon_count, freq['a'])
        balloon_count = min(balloon_count, freq['l'] // 2)
        balloon_count = min(balloon_count, freq['o'] // 2)
        balloon_count = min(balloon_count, freq['n'])
        
        return balloon_count


