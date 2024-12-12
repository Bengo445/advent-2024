
import time
start_time = time.time()

line = open("input.txt", "r").readline()

checksum = 0

MAX_BLOCK = len(line)-1
MAX_ID = sum(list(map(int, line)))
print(f"last_block: {MAX_BLOCK}, last_id:{MAX_ID}")

block_i = 0
id_i = 0
moved = 0
for v in line:
    space = (block_i%2==1)
    for _ in range(int(v)):
        
        if space:

            block_i2 = MAX_BLOCK
            id_i2 = 0
            for b in reversed(line):
                #print(block_i2)
                space2 = (block_i2%2==1)
                #print(space2)
                for _ in range(int(b)):
                    if space2:
                        if id_i2 == moved:
                            moved += 1
                        id_i2 += 1
                        continue
                    if id_i2 >= moved:
                        checksum += id_i * (block_i2//2)
                        #print(f"- (id_i2: {id_i2}  moved: {moved}  space2:{space2})")
                        #print(f"- checksum += {id_i} * {block_i2//2}  ({id_i * (block_i2//2)})")
                        moved += 1
                        break
                    id_i2 += 1
                else:
                    block_i2 -= 1
                    continue
                break
        else:
            checksum += id_i * (block_i//2)
            #print(f"checksum += {id_i} * {block_i//2}  ({id_i * (block_i//2)})")

        if MAX_ID - moved -1 <= id_i:
            print(f"ENDING - moved: {moved}  id_i: {id_i}")
            break
        id_i += 1
    else:
        block_i+=1
        continue
    break


print(checksum)

print("--- %s seconds ---" % (time.time() - start_time))