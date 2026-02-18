class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0): return 0

        longest = 0
        current = 1
        nums = sorted(set(nums))
        print(nums)
        for i in range(1,len(nums)):
            if(nums[i-1] + 1 == nums[i]):
                current +=1
            else: 
                if(current > longest):
                    longest = current
                current = 1
        if(current > longest):
            longest = current
            
        return longest or current