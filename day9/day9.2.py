import time
start_time = time.time()

line = open("input.txt", "r").readline()

data = []
for i in range(len(line)):
    if line[i] == "0":
        continue
    if i%2 == 1:
        data.append( [int(line[i]), "."] )
    else:
        data.append( [int(line[i]), i//2] )

# [[<COUNT>, <VALUE>], [<COUNT>, "."] ...]

checksum = 0

tried_files = []

moving_i = len(data)
while True:
    moving_i -= 1

    if moving_i < 0:
        break

    moving = data[moving_i]
    if moving in tried_files:
        continue
    if moving[1] == ".":  # ignore spaces (dont wanna move spaces)
        continue

    #print(data)
    #print(f"- moving_i: {moving_i} moving: {moving}")
    tried_files.append(moving)

    for j in range(moving_i+1):
        if data[j][1] != ".":  # only look for spaces
            continue

        if moving[0] <= data[j][0]:  # if file can fit in space
            # lower the space or delete it
            data[j][0] -= moving[0]
            if data[j][0] == 0:
                data.pop(j)
            # insert new instance
            data.insert(j, moving.copy())
            # turn previous instance into space
            data[data.index(moving, j+1)][1] = "."

            #print(f"- moved file")

            moving_i = len(data)-1
            break
    else:
        #print(f"- couldn't move file")
        continue

    
# count result
i = 0
for block in data:
    if block[1] == ".":
        i += block[0]
    else:
        for j in range(i, i+block[0]):
            checksum += j * block[1]
            i += 1
            #print(f"checksum += j:{j} * val:{block[1]}")

print(checksum)
print("--- %s seconds ---" % (time.time() - start_time))