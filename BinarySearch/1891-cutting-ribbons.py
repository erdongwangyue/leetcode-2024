class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l = 1
        r = max(ribbons)

        def can_cut(ribbons, k, l):
            num = 0
            for r in ribbons: 
                num += r // l
                if num >= k:
                    return True
            return False

        while l <= r:
            m = (l + r) // 2
            if can_cut(ribbons, k, m):
                l = m + 1
            else:
                r = m - 1
        return r