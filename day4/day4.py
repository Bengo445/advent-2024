f = open("input.txt", "r")


# turn input into array of lines
letterboard = []  #[y,x]
for line in f.readlines():
    letterboard.append(line.strip())
#print(letterboard)

value = 0
WORD = "XMAS"
SEARCH_DIRS = [  #from first letter  [x,y]
    [1,0],  # →
    [-1,0], # ←
    [0,-1], # ↑
    [0,1],  # ↓
    [1,-1],  # ↗
    [1,1],   # ↘
    [-1,1],  # ↙
    [-1,-1]  # ↖
]

for y in range(len(letterboard)):
    for x in range(len(letterboard[y])):
        if letterboard[y][x] != "X":
            continue
        for dir in SEARCH_DIRS:
            #check OOB
            temp = [y+dir[1]*(len(WORD)-1),x+dir[0]*(len(WORD)-1)]
            if temp[0] < 0 or temp[0] > len(letterboard[y])-1:
                continue
            if temp[1] < 0 or temp[1] > len(letterboard)-1:
                continue

            #check word
            for i in range(1, len(WORD)):
                if letterboard[y+dir[1]*i][x+dir[0]*i] != WORD[i]:
                    break
                if i == len(WORD)-1:
                    value += 1







print(value)