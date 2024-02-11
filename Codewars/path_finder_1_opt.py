from collections import defaultdict
from heapq import heappush, heappop

def neighbours(grid, v):
    n_coords = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    results = []
    for n in n_coords:
        v_next = (v[0] + n[0], v[1] + n[1])
        if v_next in grid and grid[v_next] != 'W':
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
            new_cost = cost_so_far[current] + 1 
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

    if start == target: return True

    g = {(c, r) : x for r, l in enumerate(g_maze) for c, x in enumerate(l)}

    came_from, _ = a_star(g, start, target)
    return True if came_from[target] else False





'''
#################### optional stuff

def reconstruct_path(came_from, start, target):
    current = target
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path


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

print(path_finder(a), True)
print(path_finder(b), False)
print(path_finder(c), True)
print(path_finder(d), False)

'''