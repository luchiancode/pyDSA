class Solution:
    def isValid(self, s: str) -> bool:
        openingStack = []
        if(len(s) < 2): return False

        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                openingStack.append(s[i])
            elif len(openingStack) > 0:
                top = openingStack.pop()
                if not (
                    (s[i] == ")" and top == "(")
                    or (s[i] == "]" and top == "[")
                    or (s[i] == "}" and top == "{")
                ):
                    return False
            elif len(openingStack) == 0: return False

        return not len(openingStack)
