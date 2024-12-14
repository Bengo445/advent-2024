
result = 0

MAX_TRIES = 100
BUTTONA_COST = 3
BUTTONB_COST = 1

machines = []  #{buttons:[[x,y,cost],[x,y,cost]], prize:[x,y]}
with open("input.txt", "r") as f:
    entries = f.read().split("\n\n")
    for entry in entries:
        machine = {}
        split = entry.split("\n")
        button1 = split[0].strip("Button A: X+").split(", Y+") + [BUTTONA_COST]
        button2 = split[1].strip("Button B: X+").split(", Y+") + [BUTTONB_COST]
        machine["buttons"] = [list(map(int, button1)),list(map(int, button2))]
        machine["prize"] = list(map(int, split[2].strip("Prize: X=").split(", Y=") ))
        machines.append(machine)


for machine in machines:
    print(f"\nmachine: {machine}")
    buttons:list = machine["buttons"]
    prize = machine["prize"]
    
    lowest_tokens = float("inf")
    
    buttons = sorted(buttons, key=lambda x : x[0])
    buttons.reverse()

    loop_count = 0

    for b1_count in range(100, -1, -1):
        loop_count += 1
        for b2_count in range(100, -1, -1):
            loop_count += 1
            x_sum = buttons[0][0]*b1_count + buttons[1][0]*b2_count
            y_sum = buttons[0][1]*b1_count + buttons[1][1]*b2_count
            #print(f"\n - trying BTN_1({buttons[0]}) - {b1_count} times  and BTN_2({buttons[1]}) - {b2_count} times  =  [{x_sum}, {y_sum}]", end="")
            if prize[0] > x_sum or prize[1] > y_sum:
                break
            if prize[0] == x_sum:
                if prize[1] == y_sum:
                    tokens = b1_count * buttons[0][2] + b2_count * buttons[1][2]
                    if tokens < lowest_tokens:
                        lowest_tokens = tokens
                        #print(f"  |  cost {tokens} - new lowest", end="")
                        continue
                    #print(f"  |  cost {tokens}", end="")
                    continue
                #print(f"  |  x equals", end="")
                continue
            #print(f"  |  doesnt equal", end="")

    if lowest_tokens != float("inf"):
        result += lowest_tokens






print("\n", result, loop_count)