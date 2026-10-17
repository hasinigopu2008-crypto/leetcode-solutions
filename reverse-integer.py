#approach 1
class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        x=abs(x)
        ans=0
        while x>0:
            d=x%10
            ans=ans*10+d
            x=x//10
        ans*=sign
        if ans<-(2**31) or ans>2**31-1:
            return 0
        return ans
#approach 2
class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        reverse_str=str(abs(x))[::-1]
        ans=sign*int(reverse_str)
        if ans<-(2**31) or ans>2**31-1:
            return 0
        return ans
