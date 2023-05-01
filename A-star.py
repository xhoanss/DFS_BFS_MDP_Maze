import heapq
from math import sqrt
import Generate_maze as GM
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
sys.setrecursionlimit(3000)

width = 27
height = 29
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

def manhatten(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
def A_star(maze,start,end):
    priority_q = [(0,start,[start])]
    visited = set([start])
    while priority_q:
        dis,current,path = heapq.heappop(priority_q)
        if current == end:
            return path
        for direction in directions:
            x,y = current[0]+direction[0],current[1]+direction[1]
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0 and (x,y) not in visited:
                visited.add((x,y))
                heapq.heappush(priority_q, (len(path) + manhatten((x, y), end), (x, y), path + [(x, y)]))



s = time.time()
start = (0,1)
end = (height-2,width-1)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maze_use = maze_array.tolist()

path = A_star(maze_use, start, end)
if path:
    print("Maze has path！")
    print("Path is：", path)
else:
    print("Maze do not have path.")

for i in range(10000):
    continue
e = time.time()
print(e-s)
draw_maze(maze_array,path)