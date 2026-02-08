from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:       
        pref = strs[0]
        
        for word in strs:
            while (not word.startswith(pref)):
                pref=pref[:-1]
                if( not pref): return ""
        
        return pref