class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = []

        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if(temperatures[j]>temperatures[i]):
                    solution.append(j-i)
                    break
                elif(j == len(temperatures) - 1):
                    solution.append(0)
        return solution

