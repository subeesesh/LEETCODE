# Last updated: 5/29/2026, 11:56:00 AM
class Solution:
  def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    ans = 0
    dp = [0] * len(envelopes)
    for _, h in envelopes:
      l = 0
      r = ans
      while l < r:
        m = (l + r) // 2
        if dp[m] >= h:
          r = m
        else:
          l = m + 1
      dp[l] = h
      if l == ans:
        ans += 1
    return ans