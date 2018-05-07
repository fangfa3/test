# 冒泡排序

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def bubble_sort_flag(array):
    for i in range(len(array)):
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if not flag:
            return array
            
    return array

if __name__ == '__main__':
    A = [8, 3, 5, 2, 6, 7, 1, 4]
    print(bubble_sort_flag(A))
    