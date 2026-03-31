class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l - r))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l / r))
            else:
                stack.append(int(c))
        return stack[-1]
            