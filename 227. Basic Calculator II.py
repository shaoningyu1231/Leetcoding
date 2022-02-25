class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, "+", []
        for e in range(len(s)):
            if s[e].isdigit():
                num = num * 10 + int(s[e])
            if s[e] in "+-*/" or e == len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = s[e]
        return sum(stack)
