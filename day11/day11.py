
f = open("input.txt", "r").readline()


def add_to_stones(val, amount, dict):
    if val in dict.keys():
        dict[val] += amount
    else:
        dict[val] = amount


stones = {}
for v in f.strip().split(" "):
    add_to_stones(int(v), 1, stones)
print(stones)


blinks = 0
MAX_blinks = 75  # PART1 = 25, PART2 = 75

while MAX_blinks > blinks:
    print(f"blink #{blinks}")
    blinks += 1

    new_stones = {}

    for stone, amount in stones.items():
        if stone == 0:
            add_to_stones(1, amount, new_stones)
            continue
        elif len(str(stone))%2 == 0:
            string = str(stone)
            add_to_stones(int(string[:len(string)//2]), amount, new_stones)
            add_to_stones(int(string[len(string)//2:]), amount, new_stones)
            continue
        else:
            add_to_stones(stone*2024, amount, new_stones)
    
    stones = new_stones.copy()

    print(stones)


result = sum(stones.values())
print(result)

