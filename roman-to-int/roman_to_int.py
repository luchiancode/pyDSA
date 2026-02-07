class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        stack = list(s)
        prev, curr = '',''
        total = 0

        while (len(stack)):
            curr = stack.pop()

            if(prev != '' and curr != ''  and dict[curr]< dict[prev]):
                total-=dict[curr]
            elif(curr != ''): total+=dict[curr]

            prev = curr

        return total
