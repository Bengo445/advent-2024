f = open("input.txt", "r").readlines()

result = 0

board = []
for line in f:
    board.append(line.strip())

DIRS = [ [-1,0], [0,1], [1,0], [0,-1] ]
CH = "|"
used_nines = []

def CheckSlope(pos, height, level):
    #print(CH*level, f"- checking [{pos[0]}, {pos[1]}]")
    if height == 9 and not (pos in used_nines):
        used_nines.append(pos)
        #print(CH*level, f"- got up, returning 1")
        return 1

    val = 0

    for branch , dir in enumerate(DIRS):
        pos2 = [pos[0]+dir[0], pos[1]+dir[1]]
        #print(CH*level, f"- dir {DIRS[branch]}")
        # check OOB
        if pos2[0] < 0 or pos2[0] >= len(board) or pos2[1] < 0 or pos2[1] >= len(board):
            #print(CH*level, f"- OOB")
            continue
        # next step
        if int(board[pos2[0]][pos2[1]]) == height+1:
            #print(CH*level, f"- proceeding height:{height+1}")
            val += CheckSlope(pos2, height+1, level+1)
    
    #print(CH*level, f"- returning {val}")
    return val



for y in range(len(board)):
    for x in range(len(board[y])):
        if board[y][x] != "0":
            continue
        
        used_nines = []
        print(f"new tailhead at [{y}, {x}]")
        height = 0

        value = CheckSlope([y,x], height, 1)
        print(f"- tailhead value: {value}")
        result += value

print(result)

