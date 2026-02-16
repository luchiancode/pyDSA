class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = []

        while(len(nums1) and len(nums2)):
            if(nums1[0]<=nums2[0]):
                merged_array.append(nums1.pop(0))
            elif(nums2[0]<=nums1[0]):
                merged_array.append(nums2.pop(0))

        while(len(nums1)): merged_array.append(nums1.pop(0))
        while(len(nums2)): merged_array.append(nums2.pop(0))

        mid = len(merged_array)//2

        if(len(merged_array) % 2 == 0):
            return (merged_array[mid-1]+merged_array[mid])/2
        else: return merged_array[mid]
