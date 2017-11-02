def isValid(i,j):
	return i >=0 and i < n and j >= 0 and j < m
deltaX = [0, 0, 1, 1, -1, 1, -1, 0, -1]
deltaY = [0, 1, 0, -1, 1, 1, -1, -1, 0]
count = 0
def dfs(grid,i,j):
	global count
	for _ in xrange(8):
		x = i+deltaX[_]
		y = j+deltaY[_]
		if isValid(x,y):
			if grid[x][y] == "1":
				grid[x][y] = "X"
				count += 1
				#print count
				dfs(grid,x,y)

def get_biggest_region(grid):
	global count
	regions = []
	for i in xrange(n):
		for j in xrange(m):
			if grid[i][j] == "1":
				count = 0
				dfs(grid,i,j)
				regions.append(count)
	return max(regions)

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
	grid_temp = raw_input().strip().split(' ')
	grid.append(grid_temp)
print get_biggest_region(grid)