from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_counter = nums.count(val)
        nums[:] = [x for x in nums if x != val]
        nums_counter = len(nums)
        for i in range(1,val_counter):
            nums.append('_') 

        return nums_counter