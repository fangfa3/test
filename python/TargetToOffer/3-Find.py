class Solution:
	def Find(self, array, target):
		rows = len(array)
		columns = len(array[0])
		row = 0
		column = columns - 1
		while(column >= 0 and row <= rows-1):
			if target == array[row][column]:
				return 'true'
			elif target > array[row][column]:
				row += 1
			else: 
				column -= 1
		return 'false'


S = Solution()
A = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
num = 5
print(S.Find(array = A, target = num))
