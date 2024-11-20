class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # q = deque(range(len(s)))

        deck.sort()
        q = deque(range(len(deck)))
        res = [0] * len(deck)
        for n in deck:
            i = q.popleft()
            res[i] = n
            if q:
                q.append(q.popleft())
        return res
