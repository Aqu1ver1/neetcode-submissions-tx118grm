class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if stack and ord(char) - ord(stack[-1]) in range(1, 3):
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0