
from typing import List


def partition(list: List[int], lo: int, hi: int) -> int :
    pivot = list[hi]
    idx = lo - 1

    for i in range(lo, hi):
        if(list[i] <= pivot):
            idx+=1
            list[i], list[idx] = list[idx], list[i]
    
    idx+=1
    list[idx], list[hi] = list[hi], list[idx]

    return idx


def qs(list: List[int], lo: int, hi: int):
    if(lo > hi): return

    pivotIdx = partition(list, lo, hi)
    qs(list, lo, pivotIdx - 1)
    qs(list, pivotIdx+ 1, hi)


def quick_sort(list: List[int])-> List[int]:
    qs(list, 0, len(list) - 1)
    return list



list =[ 7,8,3,1,5,7,11,33,12]

print(quick_sort(list))