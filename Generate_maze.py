import sys
import random

# The maze.
maze = dict()

# Display the maze.
#不同key里面的第n个
def display_maze(width,height):
   for y in range(0, height):
      for x in range(0, width):
         if maze[x][y] == 0:
            sys.stdout.write("  ")
         else:
            sys.stdout.write("[]")
      sys.stdout.write("\n")

# Initialize the maze.
def init_maze(width,height):
   for x in range(0, width):
      maze[x] = dict() #把宽变成字典的key
      for y in range(0, height):
         maze[x][y] = 1

# Carve the maze starting at x, y.
def carve_maze(x, y,width,height):
   dir = random.randint(0, 3)
   count = 0
   while count < 4:
      dx = 0
      dy = 0
      if dir == 0:
         dx = 1
      elif dir == 1:
         dy = 1
      elif dir == 2:
         dx = -1
      else:
         dy = -1
      x1 = x + dx
      y1 = y + dy
      x2 = x1 + dx
      y2 = y1 + dy
      if x2 > 0 and x2 < width and y2 > 0 and y2 < height:
         if maze[x1][y1] == 1 and maze[x2][y2] == 1:
            maze[x1][y1] = 0
            maze[x2][y2] = 0
            carve_maze(x2, y2,width,height)
      count = count + 1
      dir = (dir + 1) % 4

# Generate the maze.
def generate_maze(width,height):
   random.seed()
   maze[1][1] = 0 #(1,1)做为起点
   carve_maze(1, 1,width,height)
   maze[1][0] = 0 #(1,1)上面的口打开作为起点
   maze[width - 1][height - 2] = 0 #规定终点

# Generate and display a random maze.
def main(width,height):
   init_maze(width,height)
   generate_maze(width,height)

   display_maze(width,height)

# The size of the maze (must be odd).
# width = 9
# height = 19
# main(width,height)




