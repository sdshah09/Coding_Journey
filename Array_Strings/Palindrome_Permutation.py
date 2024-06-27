'''
Give a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangemenet of letters. The palindrome does not need to be limited to just dictionary words.

Example:-  Tact Coa
O/P: True(permutations: "taco cat","atco cta" etc)

'''

class Solution:
    def isPermutation(self,s):
        freq = {}
        countOdd = 0
        for i in s:
            freq[i] = freq.get(i,0)+1
            if freq[i]%2==1:
                countOdd+=1
            else:
                countOdd-=1
        return countOdd<=1        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPermutation("tactcoa"))