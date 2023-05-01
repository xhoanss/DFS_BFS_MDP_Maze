import time

import Generate_maze as GM
import matplotlib.pyplot as plt
import numpy as np
from queue import Queue

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

def BFS(maze,start,end):
    visited = set()
    queue = Queue()
    queue.put((start,[]))
    while not queue.empty():
        current,path = queue.get()
        if current == end:
            return path+[current]
        if current in visited:
            continue
        visited.add(current)
        for direction in directions:
            next = (current[0]+direction[0],current[1]+direction[1])
            if 0 <= next[0] < len(maze) and 0 <= next[1] < len(maze[0]) and maze[next[0]][next[1]] == 0:
                queue.put((next,path+[current]))

s = time.time()
start = (0,1)
end = (height-2,width-1)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maze_use = maze_array.tolist()
print(maze_use)
path = BFS(maze_use, start, end)
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


