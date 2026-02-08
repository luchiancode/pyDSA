class Solution:
    def isValid(self, s: str) -> bool:
        opening_stack = []
        if(len(s) < 2): return False

        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                opening_stack.append(s[i])
            elif len(opening_stack) > 0:
                top = opening_stack.pop()
                if not (
                    (s[i] == ")" and top == "(")
                    or (s[i] == "]" and top == "[")
                    or (s[i] == "}" and top == "{")
                ):
                    return False
            elif len(opening_stack) == 0: return False

        return not len(opening_stack)
