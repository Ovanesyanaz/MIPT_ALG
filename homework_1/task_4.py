class Solution(object):
    def findJudge(self, n, trust):
        candidates = {}

        if not trust and n == 1:
            return 1

        for pair in trust:
            first = pair[0]
            second = pair[1]
            candidates[first] = candidates.get(first, 0) - 1
            candidates[second] = candidates.get(second, 0) + 1
        
        for (candidate, count) in candidates.items():
            if count == n - 1:
                return candidate
        
        return -1