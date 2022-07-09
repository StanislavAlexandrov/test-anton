class Solution(object):
    def isPalindrome(self, x):
        s_var = str(x)
        s_var_rev=""
        for x in s_var:
            s_var_rev=x+s_var_rev
        if s_var==s_var_rev:
            return True
        else:
            return False


               
p=Solution()
print(p.isPalindrome(121))
        