sea_map = [ '0000N0',
            '000000',
            'X00000',
            '000000',
            '000000']



def check_course(sea_map):
    navy = []
    l_y = len(sea_map)
    l_x = len(sea_map[0])
    for r, l in enumerate(sea_map):
        for c, x in enumerate(l):
            if x == 'X':
                ship = [r, c]
            elif x == 'N':
                d = 1 if r == 0 else -1
                navy.append([r, c, d])

    for _ in range(1, l_x + 1):
        # check if ship is near navy ships
        neighbors = [(ship[0] + r, ship[1] + c) for c in range(-1, 2) for r in range(-1, 2)]
        nearby = [1 for n in navy if (n[0], n[1]) in neighbors]
        if nearby:
            return False
        
        ship[1] += 1                    # ship moves one forward
        for n_ship in navy:             # navy ships move by one step
            n_ship[0] += n_ship[2]
            if n_ship[0] in [0, l_y - 1]:
                n_ship[2] *= -1    # change direction if at edge

    return True
