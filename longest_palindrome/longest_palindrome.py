class Solution:
    def longestPalindrome(self, s: str) -> str:
        new_string = ''

        if(len(s) == 1): return s
        if(s == s[::-1]): return s

        for index in range(0, len(s) - 1):
            for r_index in range(len(s), -1, -1):
                placeholder = s[index:r_index]
                if(placeholder == placeholder[::-1] and len(placeholder) > len(new_string)): 
                    new_string = placeholder

    
        return new_string