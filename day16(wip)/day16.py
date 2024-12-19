import sys
print(sys.getrecursionlimit())

f = open("input.txt", "r")

result = 999999999999999999999

board = []
for y, line in enumerate(f.readlines()):
    board.append(line.strip())

COST_TURN = 1000
COST_MOVE = 1
DIRS = [     #[y,x]
    [-1, 0], #u
    [0, 1],  #r
    [1, 0],  #d
    [0, -1], #l
]

end_pos = [1, len(board[0])-2]
start_pos = [len(board)-2, 1]

def proceed(pos:list, dir_i:int, cost:int, visited:list):
    global result
    #print("|"*len(visited), pos)
    visited = visited.copy()
    visited.append(pos)
    for check_dir_offset in range(-1,2):
        check_dir_i = (dir_i+check_dir_offset)%len(DIRS)
        check_dir = DIRS[check_dir_i]
        new_pos = [pos[0]+check_dir[0], pos[1]+check_dir[1]]
        board_tile = board[new_pos[0]][new_pos[1]]
        #print("|"*len(visited), f"- dir:{check_dir} tile:{board_tile}")
        turned = (check_dir_offset != 0)
        new_cost = cost + (COST_TURN if turned else COST_MOVE)
        if new_pos in visited:
            break
        if board_tile == "#":
            continue
        elif board_tile == ".":
            proceed(new_pos, check_dir_i, new_cost, visited)
        elif board_tile == "E":
            print(f"- cost {result}, visited:{visited}")
            if new_cost < result:
                result = new_cost

proceed(start_pos, 1, 0, [])


print(result)