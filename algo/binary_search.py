from typing import List

def binary_search(list: List[int], target: int) -> int: 
    low, high = 0, len(list) - 1

    while (low < high):
        mid = low + (low+high)//2

        if(target > list[mid]): 
            low = mid + 1
        if(target < list[mid]):
            high = mid - 1
        else: return mid

    return -1
    

list = [2, 3, 4, 10, 40]
target = 10
print(binary_search(list, target))