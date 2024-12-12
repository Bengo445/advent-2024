
result = 0
DIRS = [ [-1,0], [0,1], [1,0], [0,-1] ]

# get map
map = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        map.append(line.strip())

MAP_HEIGHT = len(map)
MAP_WIDTH = len(map[0])


def is_OOB(pos:list): #pos[y,x]
    if pos[0] < 0 or pos[0] > MAP_HEIGHT-1:
        return True
    if pos[1] < 0 or pos[1] > MAP_WIDTH-1:
        return True
    return False

def fill(pos:list):
    done_plots.append(pos)
    region = map[pos[0]][pos[1]]

    area = 1
    walls = []

    # check around plot
    for dir in DIRS:
        new_pos = [pos[0]+dir[0], pos[1]+dir[1]]
        # outside of region
        if is_OOB(new_pos) or map[new_pos[0]][new_pos[1]] != region:
            walls.append([new_pos, dir]) #walls[wall[new_pos, dir], ..]
            continue
        # already checked plot
        if new_pos in done_plots:
            continue
        # found new plot of same region
        new_area, new_walls = fill(new_pos)
        area += new_area
        walls += new_walls

    #print(f" - plot y{pos[0]} x{pos[1]}, found {walls} walls")
    return area, walls

def check_sides_from_walls(walls:list):
    sides = 0


    for wall_i in range(len(walls)):
        wall = walls[wall_i]
        if wall == []:
            continue
        wall_pos, wall_dir = wall
        walls[wall_i] = []
        sides += 1

        # check continunation of side in perpendicular dirs
        # and count all walls of side as checked
        side_dir_i = DIRS.index(wall_dir)
        for dir in [ DIRS[(side_dir_i-1)%4], DIRS[(side_dir_i+1)%4] ]:
            l = 1
            while True:
                new_pos = [wall_pos[0]+dir[0]*l, wall_pos[1]+dir[1]*l]
                finding_wall = [new_pos, wall_dir]
                if finding_wall in walls:
                    walls[walls.index(finding_wall)] = []
                else:
                    break
                l += 1
    
    return sides



done_plots = []

# go thought each plot
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        # check if plot is part of new region
        if not ([y,x] in done_plots):
            region = map[y][x]
            print(f"checking region {region} starting at y{y} x{x}")
            # fill region
            region_area, region_walls = fill([y,x])
            print(f"- area: {region_area}  walls: {region_walls}")
            result += region_area * check_sides_from_walls(region_walls)

print(result)
