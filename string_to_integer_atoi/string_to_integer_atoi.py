class Solution:
    def myAtoi(self, s: str) -> int:
        signed = ""
        placeholder = ""

        for i in range(len(s)):
            if s[i].isdigit():
                placeholder += s[i]
            elif (s[i] == "-" or s[i] == "+") and (signed == "") and placeholder == "":
                signed = s[i]
            elif (
                (s[i] == "-" or s[i] == "+")
                or signed == "-"
                or signed == "+"
                or (not s[i].isdigit() and s[i] != " " and placeholder == "")
                or (not s[i].isdigit() and placeholder != "")
            ):
                break

        if placeholder == "":
            return 0

        number = int("".join([signed, placeholder]))

        if number > 2**31 - 1:
            return 2**31 - 1
        if number < -(2**31):
            return -(2**31)

        return number
