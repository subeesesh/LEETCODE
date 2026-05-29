# Last updated: 5/29/2026, 11:59:31 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])  
            for i in range(start, len(nums)):
                path.append(nums[i])       
                backtrack(i + 1, path)     
                path.pop()                 

        backtrack(0, [])
        return result