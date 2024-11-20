class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)
        visited = set([beginWord])
        q = deque([beginWord])
        time = 1
        while q:
            qLen = len(q)
            for i in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return time
                for j in range(len(curr)):
                    pattern = curr[:j] + "*" + curr[j + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            time += 1
        return 0