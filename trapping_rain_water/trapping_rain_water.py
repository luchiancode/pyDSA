class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
  
        for i in range(1,len(height)):
            max_water = min([max(height[:i]), max(height[i:])]) - height[i]
            if(max_water > 0): total+=max_water
        

        return total

