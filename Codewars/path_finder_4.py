import re
pos = [0, 0, 0] # r, c, direction (0 - north, 1 - west, 2 - south, 3 - east)

def i_am_here(path):
    global pos
    dirs = {0: (-1, 0),
            1: (0, 1),
            2: (1, 0),
            3: (0, -1)}
    turn = {'r': 1, 'l': -1}

    for instr in re.findall(r'[RLrl]|\d+', path):
        if instr.isnumeric():
            pos[0] += dirs[pos[2]][0] * int(instr)
            pos[1] += dirs[pos[2]][1] * int(instr)
        elif instr in 'RL':
            pos[2] = (pos[2] + 2) % 4
        elif instr in 'rl':
            pos[2] = (pos[2] + turn[instr]) % 4
    return pos[:2]


'''

### the intructions are:
#   number: walk in direction n steps
#   R, L: reverse direction in place (dir + / - 2)
#   r, l: turn in direction

where_are_you('',       [0, 0])
where_are_you('RLrl',   [0, 0])
where_are_you('r5L2l4', [4, 3])
'''