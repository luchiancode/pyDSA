class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)

        for v in nums:
            if(my_dict[v]):
                return v
            else:
                my_dict[v] +=1