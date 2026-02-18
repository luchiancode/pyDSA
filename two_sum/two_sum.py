class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = []

        i = 0
        size = len(numbers)
        while i < size:
            if((target - numbers[i]) in numbers):
                number = numbers.index((target - numbers[i]))
                if(number != i):
                    solution.append(i+1)
                    solution.append(number + 1)
                    numbers.pop(number)
                    i-=1
                    size-=2
            i+=1
        return solution