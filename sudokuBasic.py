board=[]
f = open('input.txt','r')
count=0
flag=0
import time

# Reading input from file

for line in f:
	line = line[:-1]
	if line[0]!='S':
		flag=1
	if flag==1 and count<9:
		temp = list(line)
		temp = [int(x) for x in temp]
		board.append(temp)
		count+=1

n=9
time_start = time.clock()

def isValid(board,row,col,value):    #### Fucntion to check if a value is valid for a variable at a particular position in the tree
	for i in range(9):
		if board[i][col] == value:    #### Check for the values in the same row
			return False
		if board[row][i] == value:    #### Check for the values in the same column
			return False
	row_start = (row/3) * 3
	col_start = (col/3) * 3
	for i in range(row_start,row_start+3):
		for j in range(col_start,col_start+3):     #### Check for the values in the same sub-box(smaller 3*3 one)
			if board[i][j] == value:
				return False
	return True


### I am going box by box for the basic backtracking.

def solveSudoku(board,row,col):
	if row>n-1:								#### Solution found if it crosses 9 rows, as all boxes are filled already and valid
		return True
	if board[row][col]!=0:
		if col==n-1:						##### Assigning the next in recursion if its the end of row and not a variable(already filled by user)
			if solveSudoku(board,row+1,0):
				return True
		else:
			if solveSudoku(board,row,col+1):   ##### Assigning the next in recursion if its not the end of row and not a variable(already filled by user)
				return True
	else:
		for value in range(1,10):			##### Check for all the values 1-9 for the variable
			if isValid(board,row,col,value):      ### If it is valid
				board[row][col] = value

				if col==n-1:							#### Call the recursive function, if its the end of row
					if solveSudoku(board,row+1,0):
						return True
				else:									#### Call the recursive function, if its not the end of row
					if solveSudoku(board,row,col+1):
						return True
				global countBT
				countBT+=1
				board[row][col] = 0						#### Re assign the value to zero if the recursive function returned False
	
	return False						#### Return False, if none of the values has returned True from recursive functions or solution found


start = "\033[1m"
end = "\033[0;0m"


##### Print soultion in a nice way to look, separating each sub-box clearly

countBT=0

if solveSudoku(board,0,0):
	print "Soultion found\n"
	for i in range(9):
		if(i%3==0):
			print start + '=====' * 8 + end
		else:
			print '-----' * 8
		print start+"||"+end,
		for j in range(8):
			if j==2 or j==5:
				print str(board[i][j])+start+ " ||"+end,
			else:
				print board[i][j], "|",
		print board[i][8],
		print start+"||"+end
	print start+'=====' * 8+end
else:
	print "No solution\n"

print "No.of backtracking's took place: ",countBT

time_end = time.clock()
print "Run time: "+str(time_end - time_start)
