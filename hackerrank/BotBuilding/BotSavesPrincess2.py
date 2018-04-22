def SavePrincess(n,grid,r,c):
	P=[]
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 'p':
				P.append(i)
				P.append(j)



	rowDiff = r- P[0]
	colDiff = c - P[1]

	nextmove = abs(rowDiff) - abs(colDiff)

	if nextmove > 0 :
		if rowDiff > 0 :
			print('UP')
		else :
			print('DOWN')

	else :
		if colDiff > 0 :
			print('LEFT')
		else :
			print('RIGHT')



m = int(input())
r,c = map(int,input().strip().split(" "))
grid =[]
for _ in range(0,m):
	grid.append(input().strip())

SavePrincess(m,grid,r,c)
