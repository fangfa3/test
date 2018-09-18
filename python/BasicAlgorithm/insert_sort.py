def insert_sort(array):
    length = len(array)
    for i in range(1, length):
        j = i 
        while array[j] < array[j - 1] and j > 0:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1


if __name__ == '__main__':
    A = [2, 4, 5, 8, 1, 9, 7, 6, 3]
    insert_sort(A)
    print(A)			