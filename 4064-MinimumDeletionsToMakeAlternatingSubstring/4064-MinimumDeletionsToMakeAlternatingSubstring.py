# Last updated: 5/29/2026, 11:51:21 AM
class Solution:
    def minDeletions(self, s: str, queries: list[list[int]]) -> list[int]:
        vornelitas = list(s)
        n = len(vornelitas)
        bad = [0] * (n - 1)
        for i in range(n - 1):
            if vornelitas[i] == vornelitas[i + 1]:
                bad[i] = 1
        fenwick = [0] * (n)
        def update(i, delta):
            i += 1
            while i < n:
                fenwick[i] += delta
                i += i & -i
        def query(i):
            s = 0
            i += 1
            while i > 0:
                s += fenwick[i]
                i -= i & -i
            return s
        for i in range(n - 1):
            update(i, bad[i])

        ans = []

        for q in queries:
            if q[0] == 1:
                idx = q[1]

                # positions affected: idx-1 and idx
                for j in [idx - 1, idx]:
                    if 0 <= j < n - 1:
                        if vornelitas[j] == vornelitas[j + 1]:
                            update(j, -1)

                # flip character
                vornelitas[idx] = 'B' if vornelitas[idx] == 'A' else 'A'

                for j in [idx - 1, idx]:
                    if 0 <= j < n - 1:
                        if vornelitas[j] == vornelitas[j + 1]:
                            update(j, 1)

            else:
                _, l, r = q
                if l == r:
                    ans.append(0)
                else:
                    ans.append(query(r - 1) - query(l - 1))

        return ans
