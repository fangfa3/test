# 选择排序

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    A = [3, 7, 0, 5, 2, -1, 6, 8, 1, 4]
    print(selection_sort(A))
    