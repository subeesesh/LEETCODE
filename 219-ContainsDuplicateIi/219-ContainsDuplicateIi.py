# Last updated: 5/29/2026, 11:57:10 AM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map=defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in map:
                if abs(i-map[nums[i]])<=k:
                    return True
            map[nums[i]]=i
        return False