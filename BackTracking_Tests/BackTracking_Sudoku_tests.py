import time

# A Backtracking program in Pyhton to solve Sudoku 16x16 problem

n = 9
n_2 = 3

# A Utility Function to print the Grid
def print_grid(arr):
	l = ""
	for i in range(n):
		for j in range(n):
			l = l + str(arr[i][j]) + " "
			if arr[i][j] < 10: l = l + " "
			if (j+1)%n_2 == 0 and j != n-1: l = l + "| "
		print(l)
		if (i+1)%n_2 == 0 and i != n-1: print("-" * len(l))
		l = ""

		
# Function to Find the entry in the Grid that is still not used
# Searches the grid to find an entry that is still unassigned. If
# found, the reference parameters row, col will be set the location
# that is unassigned, and true is returned. If no unassigned entries
# remain, false is returned.
# 'l' is a list variable that has been passed from the solve_sudoku function
# to keep track of incrementation of Rows and Columns
def find_empty_location(arr,l):
	for row in range(n):
		for col in range(n):
			if(arr[row][col]==0):
				l[0]=row
				l[1]=col
				return True
	return False

def count_empty_location(arr):
	res = 0
	for row in range(n):
		for col in range(n):
			if(arr[row][col]==0):
				res = res + 1
	return res

# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number.
def used_in_row(arr,row,num):
	for i in range(n):
		if(arr[row][i] == num):
			return True
	return False

# Returns a boolean which indicates whether any assigned entry
# in the specified column matches the given number.
def used_in_col(arr,col,num):
	for i in range(n):
		if(arr[i][col] == num):
			return True
	return False

# Returns a boolean which indicates whether any assigned entry
# within the specified 3x3 box matches the given number
def used_in_box(arr,row,col,num):
	for i in range(n_2):
		for j in range(n_2):
			if(arr[i+row][j+col] == num):
				return True
	return False

# Checks whether it will be legal to assign num to the given row,col
# Returns a boolean which indicates whether it will be legal to assign
# num to the given row,col location.
def check_location_is_safe(arr,row,col,num):
	
	# Check if 'num' is not already placed in current row,
	# current column and current 3x3 box
	return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%n_2,col - col%n_2,num)

# Takes a partially filled-in grid and attempts to assign values to
# all unassigned locations in such a way to meet the requirements
# for Sudoku solution (non-duplication across rows, columns, and boxes)
def solve_sudoku(arr,empty_loc):
	
	# 'l' is a list variable that keeps the record of row and col in find_empty_location Function 
	l=[0,0]
	
	# If there is no unassigned location, we are done 
	if(not find_empty_location(arr,l)):
		return True

	# Assigning list values to row and col that we got from the above Function 
	row=l[0]
	col=l[1]
	
	# consider digits 1 to n
	for num in range(1,n+1):
		# if looks promising
		if(check_location_is_safe(arr,row,col,num)):
			
			# make tentative assignment
			arr[row][col]=num
			empty_loc = empty_loc - 1

			# return, if sucess, ya!
			if(solve_sudoku(arr,empty_loc)):
				return True

			# failure, unmake & try again
			arr[row][col] = 0
			empty_loc = empty_loc + 1
			
	# this triggers backtracking	 
	return False

def write_saida(arq):
	with open(arq, "w") as f:
		l = ""
		for i in range(n):
			for j in range(n):
				l = l + str(grid[i][j]) + " "
			f.write(l + '\n')
			l = ""

def init(grid,empty_loc):
	# if sucess print the grid
	t = time.time()
	if(solve_sudoku(grid,empty_loc)):
		print(time.time()-t)
		print_grid(grid)
		write_saida("saida" + str(n) + ".txt")
	else:
		print("No solution exists")

# Driver main function to test above functions
if __name__=="__main__":
	
	# creating a 2D array for the grid
	grid = [[0 for x in range(n)]for y in range(n)]
	
	# assigning values to the grid
	grid = [[3,0,6,5,0,8,4,0,0],
			[5,2,0,0,0,0,0,0,0],
			[0,8,7,0,0,0,0,3,1],
			[0,0,3,0,1,0,0,8,0],
			[9,0,0,8,6,3,0,0,5],
			[0,5,0,0,9,0,6,0,0],
			[1,3,0,0,0,0,2,5,0],
			[0,0,0,0,0,0,0,7,4],
			[0,0,5,2,0,6,3,0,0]]

	empty_loc = count_empty_location(grid)

	init(grid,empty_loc)

# The above code has been contributed by Harshit Sidhwa.
# https://github.com/harshitsidhwa?tab=repositories
# https://repl.it/@rui1337/backtrack-sudoku-solver