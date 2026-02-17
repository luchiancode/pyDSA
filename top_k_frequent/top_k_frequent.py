class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_f = defaultdict(int)

        for i in range(len(nums)):
            dict_f[nums[i]] +=1
        
        result = []
        for i in range(0,k):
            count = 0
            val = -1
            for i in dict_f:
                if(dict_f.get(i) > count):
                    count = dict_f.get(i)
                    val = i
            dict_f.pop(val)
            result.append(val)
            
        return result