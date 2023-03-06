'''

Leetcode: 54 - Spiral Matrix


	  right ->
	* * * * * * *     
	            *   
     ^	* * * * *   *     
     |	*       *   * down
     up *   *   *   *  |
	*   * * *   *  V
	*           *     
	* * * * * * *  
	   <- left


Solution Logic:

Keep following the right, down, left, up pattern and have a cursor
keep track of the current element and save it to the spiral array
as the cursor moves along the spiral. Each time the spiral changes
direction we must decrease the x and y values because the spiral
is getting smaller and thus the distance the cursor must move
along each line also gets smaller.

'''

def spiralOrder(matrix: list[list[int]]) -> list[int]:

	x, y = len(matrix[0]) - 1, len(matrix) - 1
	num_elements = (x+1) * (y+1)
	c = [0, 0]
	outer_finished = False
	# We need to count the first spot before moving
	spiral = [matrix[0][0]]

	while True:

		# Move Right
		for i in range(x):
			c[1] = c[1] + 1
			spiral.append(matrix[c[0]][c[1]]) 
		if outer_finished == True:
			x = x - 1
		# Let the first right run pass over as the first right pass
		# will not change the bottom outer x wall (first left pass)
		outer_finished = True
		# Finish case - We have all the elements so don't keep going
		if len(spiral) == num_elements:
			break

		# Move Down
		for i in range(y):
			c[0] = c[0] + 1
			spiral.append(matrix[c[0]][c[1]])
		y = y - 1
		if len(spiral) == num_elements:
			break

		# Move Left
		for i in range(x):
			c[1] = c[1] - 1
			spiral.append(matrix[c[0]][c[1]])
		x = x - 1
		if len(spiral) == num_elements:
			break

		# Move Up
		for i in range(y):
			c[0] = c[0] - 1
			spiral.append(matrix[c[0]][c[1]])
		y = y - 1
		if len(spiral) == num_elements:
			break

	return spiral


if __name__ == '__main__':
	test_matrix_one = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16]]

	test_matrix_two = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12]]

	test_matrix_three = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]]

	test_matrix_four = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9],
		[10, 11, 12]]

	assert spiralOrder(test_matrix_one) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
	print("Test Case 1 Passed")
	assert spiralOrder(test_matrix_two) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
	print("Test Case 2 Passed")
	assert spiralOrder(test_matrix_three) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
	print("Test Case 3 Passed")
	assert spiralOrder(test_matrix_four) == [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
	print("Test Case 4 Passed")
