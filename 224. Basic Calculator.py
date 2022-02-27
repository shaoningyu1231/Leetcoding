class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i, signal =0, 1
        res = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res += num * signal
                i -= 1
            elif s[i] == "+":
                signal = 1
            elif s[i] == "-":
                signal = -1
            elif s[i] == "(":
                stack.append(res)
                stack.append(signal)
                res = 0
                signal = 1
            elif s[i] == ")":
                res = stack.pop() * res
                res += stack.pop()
            i += 1
        return res
