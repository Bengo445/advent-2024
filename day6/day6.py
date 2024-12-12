
f = open("input.txt", "r")

ROTATE_TABLE = {
    "[-1, 0]": [0, 1],
    "[0, 1]": [1, 0],
    "[1, 0]": [0, -1],
    "[0, -1]": [-1, 0]
}

board = []

visited = []
active_pos = [0,0] #y,x
facing = [-1,0] #y,x


for y, line in enumerate(f.readlines()):
    board.append(line)
    x = line.find("^")
    if x > -1:
        active_pos = [y, x] # y,x

visited.append(active_pos)


def rotate(cur_facing):
    return ROTATE_TABLE[str(cur_facing)]

while True:
    next_pos = [active_pos[0]+facing[0], active_pos[1]+facing[1]]

    #print(active_pos)
    if next_pos[0] < 0 or next_pos[0] > len(board)-1:
        break
    if next_pos[1] < 0 or next_pos[1] > len(board[0])-1:
        break

    if board[next_pos[0]][next_pos[1]] == "#":
        facing = rotate(facing)
    else:
        if not (next_pos in visited):
            visited.append(next_pos)
        active_pos = next_pos


print(len(visited))

f = open("visited.txt", "a")
for vis in visited:
    f.write(str(vis[0]))
    f.write(" ")
    f.write(str(vis[1]))
    f.write("\n")
f.close()