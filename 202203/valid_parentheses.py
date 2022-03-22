from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List = [""]
        if s.count("(") == s.count(")") and s.count("{") == s.count("}") and s.count("[") == s.count("]"):
            for i in s:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(i)

            if len(stack) == 1:
                return True
        return False
