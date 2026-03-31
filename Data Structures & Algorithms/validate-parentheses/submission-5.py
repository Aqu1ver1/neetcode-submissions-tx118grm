class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 1: return False
        stack = [s[0]]
        for i in range(1,len(s)):
            if stack and ord(s[i]) - ord(stack[-1]) in range(1, 3):
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0