

ROTATE_TABLE = {
    "[-1, 0]": [0, 1],
    "[0, 1]": [1, 0],
    "[1, 0]": [0, -1],
    "[0, -1]": [-1, 0]
}

board = []

start_pos = [0,0] #y,x
start_face = [-1,0]#y,x

possible_loops = 0

#get board
for y, line in enumerate(open("input.txt", "r").readlines()):
    board.append(line)
    x = line.find("^")
    if x > -1:
        start_pos = [y, x] # y,x

#get visited
visited = []
for ln in open("visited.txt", "r").readlines():
    coords = ln.strip().split(" ")
    visited.append([int(coords[0]), int(coords[1])])


def rotate(cur_facing):
    return ROTATE_TABLE[str(cur_facing)]




for block_pos in visited:
    print("trying", block_pos)
    
    pos = start_pos
    dir = start_face
    rotated_at = []

    while True:
        next_pos = [pos[0]+dir[0], pos[1]+dir[1]]
        #print(next_pos)

        #print(active_pos)
        if next_pos[0] < 0 or next_pos[0] > len(board)-1:
            print("out")
            break
        if next_pos[1] < 0 or next_pos[1] > len(board[0])-1:
            print("out")
            break

        if board[next_pos[0]][next_pos[1]] == "#" or [next_pos[0],next_pos[1]] == block_pos:
            if [pos, dir] in rotated_at:
                possible_loops += 1
                print("looped")
                break
            rotated_at.append([pos, dir])
            dir = rotate(dir)
        else:
            pos = next_pos

    #break

print(possible_loops)