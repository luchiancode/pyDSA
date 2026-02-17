class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest_number = max(nums)
        nums = set(nums)

        if(smallest_number > 0):
            for i in range(1, smallest_number):
                if(i not in nums): return i
        else: return 1

        return smallest_number + 1