# Last updated: 5/29/2026, 12:01:35 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in result:
                return [result[diff],i]
            result[nums[i]]=i
        return -1