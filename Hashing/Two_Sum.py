class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s ={}

        for i in range (len(nums)):
            n= target - nums[i]

            if n in s:
                return [s[n],i]
            s[nums[i]]=i
