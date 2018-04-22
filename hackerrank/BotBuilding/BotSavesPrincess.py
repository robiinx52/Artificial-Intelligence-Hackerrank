def SavePrincess(n,grid):
	M = []
	P = []

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 'm':
				M.append(i)
				M.append(j)
			if grid[i][j] == 'p':
				P.append(i)
				P.append(j)

	rowDiff = P[0] - M[0]
	colDiff = P[1] - M[1]


	if rowDiff > 0 :
		for _ in range(abs(rowDiff)):
			print('DOWN')
	else :
		for _ in range(abs(rowDiff)):
			print('UP')

	if colDiff > 0 :
		for _ in range(abs(colDiff)):
			print('RIGHT')
	else :
		for _ in range(abs(colDiff)):
			print('LEFT')

m = int(input())
grid = []
for i in range(0,m):
	grid.append(input().strip())

SavePrincess(m,grid)
