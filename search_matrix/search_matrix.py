class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = -1

        for i in range(len(matrix) - 1):
            if(target >= matrix[i][0] and target < matrix[i+1][0]):
                row = i
                break
        
        if(row == -1):
            row = len(matrix) - 1

        return True if self.search(matrix[row], target) != -1 else False


    
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while(left<=right):
            mid =  left + ((right-left) // 2)

            if(nums[mid] == target): 
                return mid
            if(nums[mid] < target):
                left = mid + 1
            if(nums[mid] > target):
                right = mid - 1
        
        return -1