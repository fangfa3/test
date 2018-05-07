# 快排

import random

def quick_sort(array, start, end):
    if start == end :
        return  
    index = random_Partition(array, start, end)
    if index > start:
        quick_sort(array, start, index - 1)
    if index < end:
        quick_sort(array, index + 1, end)

def Partition(array, start, end):
    small = start 
    for index in range(start, end):
        if array[index] < array[end]:
            array[index], array[small] = array[small], array[index]
            small += 1
    array[small], array[end] = array[end], array[small]
    return small

def random_Partition(array, start, end):
    random_index = random.randint(start, end)
    array[random_index], array[end] = array[end], array[random_index]
    small = start
    for index in range(start, end):
        if array[index] < array[end]:
            array[index], array[small] = array[small], array[index]
            small += 1
    array[small], array[end] = array[end], array[small]
    return small
    

if __name__ == '__main__':
    A = [8, 3, 5, 2, 6, 7, 1, 4]
    quick_sort(A, 0, 7)
    print(A)