import Generate_maze as GM
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
sys.setrecursionlimit(50000)

width = 17
height = 19
GM.main(width,height)
maze = GM.maze
maze_array = np.array([[maze[x][y] for x in range(width)] for y in range(height)])
def draw_maze(maze,policy,start,end):
    rows, cols = len(maze), len(maze[0])
    img = np.zeros((rows, cols), dtype=np.uint8)
    img[maze == 0] = 255
    plt.axis('off')
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    current = start
    while current != end:
        plt.scatter(current[1], current[0], c='b', marker='o')  # 在坐标 (i, i+1) 处添加蓝色的圆形点
        if policy[current] == 'up':
            current = (current[0]-1,current[1])
        elif policy[current] == 'down':
            current = (current[0] + 1, current[1])
        elif policy[current] == 'left':
            current = (current[0], current[1]-1)
        else:
            current = (current[0], current[1]+1)
        plt.pause(0.0001)
    plt.scatter(end[1], end[0], c='b', marker='o')  # 在坐标 (i, i+1) 处添加蓝色的圆形点
    plt.show()

def state_mapping(maze):
    S = []
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if maze[i, j] == 0:
                S.append((i, j))
    return S
def transition_probabilities(S,A):
    P = {}
    for s in S:
        P[s] = {}
        for a in A:
            P[s][a] = {}
            if a == "up":
                next_s = (s[0] - 1, s[1])
            elif a == "down":
                next_s = (s[0] + 1, s[1])
            elif a == "left":
                next_s = (s[0], s[1] - 1)
            else:
                next_s = (s[0], s[1] + 1)
            if next_s in S:
                P[s][a][next_s] = 1
            else:
                P[s][a][s] = 1
    return P

def rewards(S):
    R={}
    for s in S:
        R[s] = -1 if maze_array[s[0]][s[1]] == 0 else -0.1
    R[(height-2, width-1)] = 10
    return R

def value_iteration(gamma,S,V,A,P,R):
    while True:
        delta=0
        for s in S:
            v = V[s]
            max_value = float("-inf")
            max_action = ''
            for a in A:
                next_states = list(P[s][a].keys())
                if len(next_states) == 0:
                    continue
                expected_value = sum([P[s][a][next_s] * (R[next_s] + gamma * V[next_s]) for next_s in next_states])
                if expected_value > max_value:
                    max_action = a
                max_value = max(max_value, expected_value)
            V[s] = max_value
            delta = max(delta, abs(v - V[s]))
            policy[s] = max_action
        if delta < 1e-300:
            break


def get_policy(policy,S,end,A,P,R,V):
    for s in S:
        if s == end:
            continue
        max_value = float("-inf")
        max_action = ''
        for a in A:
            next_states = list(P[s][a].keys())
            if len(next_states) == 0:
                continue
            expected_value = sum([P[s][a][next_s] * (R[next_s] + gamma * V[next_s]) for next_s in next_states])
            if expected_value > max_value:
                max_value = expected_value
                max_action = a
        policy[s] = max_action

s = time.time()
start = (0,1)
end = (height-2,width-1)
gamma = 0.9
state_space = state_mapping(maze_array)
action_space = ['up','down','left','right']
value = {s: 0 for s in state_space}
probebility = transition_probabilities(state_space,action_space)
policy = {s: action_space[0] for s in state_space}
reward = rewards(state_space)

value_iteration(gamma,state_space,value,action_space,probebility,reward)
#可以不用
#get_policy(policy,state_space,end,action_space,probebility,reward,value)
print(value)
print(policy)
e = time.time()
print(e-s)
draw_maze(maze_array,policy,start,end)
