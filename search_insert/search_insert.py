class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        if(target < nums[low]): return low
        if(target > nums[high]): return len(nums)

        while(low <= high):
            middle = int((low+high)/2)

            if(target == nums[middle]): 
                return middle 

            elif(target < nums[middle]): 
                high = middle - 1
                
            elif(target > nums[middle]): 
                low = middle + 1
        
        return low