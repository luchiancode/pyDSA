class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        size = len(numbers)

        while i < size:
            if((target - numbers[i]) in numbers):
                number = numbers.index((target - numbers[i]))
                if(number != i):
                    return [i+1, number+1]
            i+=1
            
        return []