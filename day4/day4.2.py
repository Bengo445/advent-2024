f = open("input.txt", "r")


# turn input into array of lines
letterboard = []  #[y,x]
for line in f.readlines():
    letterboard.append(line.strip())
#print(letterboard)

value = 0
SEARCH_DIRS = [  #from first letter  [x,y]
    [1,-1],  # ↗
    [1,1],   # ↘
    [-1,1],  # ↙
    [-1,-1]  # ↖
]
POSSIBLE_COMBOS = [ # "↗↘↙↖"
    "MMSS", "SMMS", "SSMM", "MSSM"
]

for y in range(len(letterboard)):
    for x in range(len(letterboard[y])):
        if letterboard[y][x] != "A":
            continue
        #print("Start found at x", x, "y", y)
        #check OOB
        if x-1 < 0 or x+1 > len(letterboard[y])-1:
            #print("- OOB")
            continue
        if y-1 < 0 or y+1 > len(letterboard)-1:
            #print("- OOB")
            continue

        #check word
        for combo in POSSIBLE_COMBOS:
            #print("- TRYING COMBO:", combo)
            for i, dir in enumerate(SEARCH_DIRS):
                
                #print("- dir[",x,y,"] has", letterboard[y+dir[1]][x+dir[0]])
                if letterboard[y+dir[1]][x+dir[0]] != combo[i]:
                    #print("- breaking")
                    break
                if i == len(SEARCH_DIRS)-1:
                    #print("- full X")
                    value += 1









print(value)