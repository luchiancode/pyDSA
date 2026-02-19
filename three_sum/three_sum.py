class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                difference = nums[i]+nums[j]
                if(-difference in nums):
                    index = nums.index(-difference)
                    if(i!=j and i!=index and j!=index):
                        pair = sorted([nums[i], nums[j], nums[index]])
                        if(pair not in solution):
                            solution.append(pair)
        
        return solution
