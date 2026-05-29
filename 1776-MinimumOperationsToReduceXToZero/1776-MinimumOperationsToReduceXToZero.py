# Last updated: 5/29/2026, 11:52:58 AM
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total=sum(nums)-x
        if total<0:
            return -1
        if total==0:
            return len(nums)
        freq={0:-1}
        max_len=-1
        curr=0
        for i,n in enumerate(nums):
            curr+=n
            if curr-total in freq:
                max_len=max(max_len,i-freq[curr-total])
            freq[curr]=i
        return len(nums)-max_len if max_len!=-1 else -1
