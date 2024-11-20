class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # visited
        last_pos = {char: i for i, char in enumerate(s)}

        string_builder = []

        visited = set()

        for i, char in enumerate(s):
            if char not in visited:
                while string_builder and char < string_builder[-1] and i < last_pos[string_builder[-1]]:
                    visited.remove(string_builder.pop())
                visited.add(char)
                string_builder.append(char)
        return "".join(string_builder)