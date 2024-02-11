from collections import defaultdict
from heapq import heappush, heappop
import random


def heuristic(a, b):
    (c1, r1) = a
    (c2, r2) = b
    return abs(c1 - c2) + abs(r1 - r2)

def reconstruct_path(came_from, start, target):
    current = target
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path


# returns a dictionary of paths from start to each accessible square in the grid
def a_star(grid, start, target):
    n_coords = [(0, -1), (1, 0), (0, 1), (-1, 0)] # coordinates of neighbours
    frontier = [(0, start)]     # our priority queue with starting values
    came_from = defaultdict(list)   # path of visited nodes
    cost_so_far = {start: 0}    # cost of the path so far

    while frontier:
        _, current = heappop(frontier)

        if current == target:
            break

        for n in n_coords:
            v_next = (current[0] + n[0], current[1] + n[1])
            # check if neighbour is a valid grid component
            if (v_next in grid 
                and grid[v_next] != 1):
                new_cost = cost_so_far[current] + 1 # cost for moving in grid is always 1 - change if there is a specific cost for movements e.g. for terrain
                # if we have not found cost for v_next, or found
                # a cheaper path to v_next, add it to the queue
                if (v_next not in cost_so_far or 
                    new_cost < cost_so_far[v_next]):
                    cost_so_far[v_next] = new_cost
                    # estimate the cost to the goal
                    priority = new_cost + heuristic(target, v_next)
                    heappush(frontier, (priority, v_next))
                    came_from[v_next] = current
                
    return came_from, cost_so_far



def path_finder(maze):
    g_maze = maze.split('\n')
    mX, mY = len(g_maze[0]), len(g_maze)
    start = (0, 0)
    target = (mX - 1, mY - 1)

    if start == target:
        return True

    g = dict()
    for r, l in enumerate(g_maze):
        for c, x in enumerate(l):
            if x == '.':
                z = 0
            elif x == 'W':
                z = 1
            g[(c, r)] = z


    came_from, cost_so_far = a_star(g, start, target)
    
    # check if we found a path
    if came_from[target]:
        p = reconstruct_path(came_from, start, target)
        print_path(g, (mX, mY), p, start, target)
        print('From %s to %s: %d steps' % (str(start), str(target), cost_so_far[target]))
        return True
    else:
        print('No path from %s to %s found.' % (str(start), str(target)))
        return False


def print_path(grid, dims, path, start, target):
    types = {0: '.', 1: 'W'}
    for r in range(dims[1]):
        line = ''
        for c in range(dims[0]):
            if (c, r) == start:
                x = 'S'
            elif (c, r) == target:
                x = 'T'
            elif (c, r) in path:
                x = 'o'
            else:
                x = types[grid[(c, r)]]
            line += x
        print(line)


a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

#### test cases to sort out

e = '\n'.join([
    '.'
])

print(path_finder(a), True)
print(path_finder(b), False)
print(path_finder(c), True)
print(path_finder(d), False)

print(path_finder(e), True)


'''
Solutions from codewars:

def path_finder(maze):
    g = maze.splitlines()
    end, bag = len(g[0]) -1 + len(g) * 1j - 1j, {0}
    grid = {x + y * 1j for y,l in enumerate(g) for x,c in enumerate(l) if '.' == c}
    while bag:
        if end in bag: return True
        grid -= bag
        bag = grid & set.union(*({z + 1j ** k for k in range(4)} for z in bag))
    return False

#### what the hell... using set unions and complex numbers???
It is a flood fill algorithm.
Starting from a bag with upper left corner - coordinates (0, 0), it tests all directions and adds all neighbours where you can go and you haven't already visited into the bag.
It stops when bottom right corner is into the bag - meaning a path exists between start and end (returns True) - or when there is no more cell to visit into the bag - meaning no path exists (returns False).
The only difference with a more traditional implementation is that I used a unique complex number x + 1j * y to represent cell coordinates instead of a pair of integers (x, y).


def path_finder(maze):
    matrix = list(map(list, maze.splitlines()))
    stack, length = [[0, 0]], len(matrix)
    while len(stack):
      x, y = stack.pop()
      if matrix[x][y] == '.':
        matrix[x][y] = 'x'
        for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
          if 0 <= x < length and 0 <= y < length:
            stack.append((x, y))
    return matrix[length-1][length-1] == 'x'

#### this is a very simple BFS implementation - quite clever.