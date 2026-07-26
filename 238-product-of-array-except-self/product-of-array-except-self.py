class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))

        #Prefix Product = product of all elements before the current index.
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        #Postfix Product = product of all elements after the current index.
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
#Time Complexity: O(n)
#Space Complexity: O(1)