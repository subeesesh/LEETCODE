# Last updated: 5/29/2026, 11:58:26 AM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        low=float('inf')
        index=-1
        current=gas[0]
        for i in range(len(gas)):
            current=current-cost[i]+gas[i]
            if current<low:
                low=current
                index=(i+1)%len(gas)
        if current<0:
            return -1
        total=0
        for i in range(len(gas)):
            j=(index+i)%len(gas)
            total+=gas[j]-cost[j]
            if total<0:
                return -1
        return index

        