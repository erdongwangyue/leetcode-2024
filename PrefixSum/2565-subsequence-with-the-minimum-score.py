class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        sLen, tLen = len(s), len(t)
        prefix = [0] * sLen
        suffix = [0] * sLen
        i, j = 0, 0
        while i < sLen and j < tLen:
            if s[i] == t[j]:
                prefix[i] += 1
                j += 1
            prefix[i] += prefix[i - 1] if i > 0 else 0
            i += 1

        i, j = sLen - 1, tLen - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                suffix[i] += 1
                j -= 1
            suffix[i] += suffix[i + 1] if i <= sLen - 2 else 0
            i -= 1
        res = float("inf")
        for i in range(sLen - 1):
            res = min(res, tLen - suffix[i + 1] - prefix[i])
        res = min(res, tLen - prefix[-1], tLen - suffix[0])
        return max(res, 0)