 def decodeString(self, s: str) -> str:
        i, stack = 0, []
        num, string = 0, ""
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "[":
                stack.append((num, string))
                num = 0
                string = ""
            elif s[i] == "]":
                last_num, last_str = stack.pop()
                string = last_str + string * last_num
            else:
                string += s[i]
            i += 1
        return string
