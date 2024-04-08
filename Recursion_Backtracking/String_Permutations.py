'''
Find Permutations of a String

I/P "ABC"
O/P = ["ABC","ACB","BCA","BAC","CBA","CAB"]

'''

class Solution:
    def __init__(self):
        pass
    def recurse(self,res,string,prefix):
        if len(string)==0:
            res.append(prefix)
            return
        for i in range(len(string)):
            remaining = string[:i]+string[i+1:]
            self.recurse(res,remaining,prefix+string[i])
    def permutations(self,res,string,prefix):
        self.recurse(res,string,prefix)
        return res

if __name__ == "__main__":
    sol = Solution()
    x = sol.permutations([],"ABC","")
    print(x)