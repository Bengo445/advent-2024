
lines = open("input.txt", "r").readlines()

dmatrix = [] #debug

antinodes = []
antennas = {}   #"A" = [ [pos], [pos].. ]

max_y = len(lines)-1
max_x = len(lines[0].strip())-1
print(f"max_y:{max_y}  max_x:{max_x}")

for y in range(len(lines)):
    line = lines[y].strip()
    dmatrix.append([]) #debug
    for x in range(len(line)):
        char = line[x]
        dmatrix[y].append(char) #debug
        if char == ".":
            continue
        if char in antennas.keys():
            antennas[char].append([y,x])
        else:
            antennas[char] = [[y,x]]

print(f"matrix_max_y:{len(dmatrix)}  matrix_max_x:{len(dmatrix[0])}")


for name, ant_group in antennas.items():
    for i in range(len(ant_group)):
        ant1 = ant_group[i]
        for j in range(len(ant_group)):
            ant2 = ant_group[j]
            if ant1 == ant2:
                continue

            offset = [ant1[0]-ant2[0], ant1[1]-ant2[1]]
            antinode = [ant1[0]+offset[0], ant1[1]+offset[1]]

            # check OOB
            if antinode[0] < 0 or antinode[0] > max_y:
                print(f"antinode {antinode}: OOB")
                continue
            if antinode[1] < 0 or antinode[1] > max_x:
                print(f"antinode {antinode}: OOB")
                continue

            if not (antinode in antinodes):
                print(f"antinode {antinode}: valid")
                antinodes.append(antinode)
                dmatrix[antinode[0]][antinode[1]] = "#"


#debug visualize
for y in range(len(dmatrix)):
    print()
    for x in range(len(dmatrix[0])):
        print(dmatrix[y][x],end="")


print()
print(antennas)
print(len(antinodes))