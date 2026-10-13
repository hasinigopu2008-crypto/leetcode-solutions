class Solution(object):
    def brute_force(self,nums):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    return True
        return False
    def sorting(self,nums):
        n=len(nums)
        nums.sort()
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                return True
        return False
    def set(self,nums):
        seen=set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
    def containsDuplicate(self, nums):
        return self.set(nums)    
