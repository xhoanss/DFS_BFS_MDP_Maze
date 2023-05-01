import Generate_maze as GM
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
sys.setrecursionlimit(3000)

#This parameter controls the size of the maze
width = 17
height = 19
GM.main(width,height)
maze = GM.maze
maze_array = np.array([[maze[x][y] for x in range(width)] for y in range(height)])
def draw_maze(maze,path):
    rows, cols = len(maze), len(maze[0])
    img = np.zeros((rows, cols), dtype=np.uint8)
    img[maze == 0] = 255
    plt.axis('off')
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    for i in range(len(path)):
        plt.scatter(path[i][1], path[i][0], c='b', marker='o')  # 在坐标 (i, i+1) 处添加蓝色的圆形点
        plt.pause(0.0001)
    plt.show()


def DFS(maze, start, end, path=[]):
    #每次都把新的节点加进去，只有正确的路径能返回，否则返回的是None
    if start == end:
        path.append(start)
        return path
    x, y = start
    maze[x][y] = 1
    for x_add, y_add in directions:
        nx, ny = x + x_add, y + y_add
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            path.append(start)
            new_path = DFS(maze, (nx, ny), end, path)
            if new_path:
                return new_path
            path.pop()
    return None

#this is the start point and end point and the directions that robot need
#The result shows the coordinates of the correct path and is animated
s = time.time()
start = (0,1)
end = (height-2,width-1)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maze_use = maze_array.tolist()

path = DFS(maze_use, start, end)
if path:
    print("Maze has path！")
    print("Path is：", path)
else:
    print("Maze do not have path.")
e = time.time()
for i in range(10000):
    continue
print(e-s)
draw_maze(maze_array,path)


