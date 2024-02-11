'''
You are at start location [0, 0] in mountain area of NxN and 
you can only move in one of the four cardinal directions 
(i.e. North, East, South, West). 

Return minimal number of climb rounds to target location [N-1, N-1]. 
Number of climb rounds between adjacent locations is defined as
difference of location altitudes (ascending or descending).

Location altitude is defined as an integer number (0-9).
'''

from collections import defaultdict
from heapq import heappush, heappop

def neighbours(grid, v):
    n_coords = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    results = []
    for n in n_coords:
        v_next = (v[0] + n[0], v[1] + n[1])
        if v_next in grid:
            results.append(v_next)
    return results

def heuristic(a, b):
    (c1, r1) = a
    (c2, r2) = b
    return abs(c1 - c2) + abs(r1 - r2)

def a_star(grid, start, target):

    frontier = [(0, start)]
    came_from = defaultdict(list)
    cost_so_far = {start: 0}

    while frontier:
        _, current = heappop(frontier)

        if current == target:
            break

        for v_next in neighbours(grid, current):
            new_cost = cost_so_far[current] + abs(grid[current] - grid[v_next])
            if v_next not in cost_so_far or new_cost < cost_so_far[v_next]:
                cost_so_far[v_next] = new_cost
                priority = new_cost + heuristic(target, v_next)
                heappush(frontier, (priority, v_next))
                came_from[v_next] = current
                
    return came_from, cost_so_far



def path_finder(maze):
    g_maze = maze.split('\n')
    mX, mY = len(g_maze[0]), len(g_maze)
    start = (0, 0)
    target = (mX - 1, mY - 1)

    if start == target: return 0

    g = {(c, r) : int(x) for r, l in enumerate(g_maze) for c, x in enumerate(l)}

    came_from, cost_so_far = a_star(g, start, target)
    if came_from[target]:
        return cost_so_far[target]
    else:
        return False





a = "\n".join([
  "000",
  "000",
  "000"
])

b = "\n".join([
  "010",
  "010",
  "010"
])

c = "\n".join([
  "010",
  "101",
  "010"
])

d = "\n".join([
  "0707",
  "7070",
  "0707",
  "7070"
])

e = "\n".join([
  "700000",
  "077770",
  "077770",
  "077770",
  "077770",
  "000007"
])

f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

g = "\n".join([
  "000000",
  "000000",
  "000000",
  "000010",
  "000109",
  "001010"
])

print(path_finder(a), 0)
print(path_finder(b), 2)
print(path_finder(c), 4)
print(path_finder(d), 42)
print(path_finder(e), 14)
print(path_finder(f), 0)
print(path_finder(g), 4)

