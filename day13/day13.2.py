
import time
start = time.time()


result = 0

FIBB_COUNT = 60
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

def fibonacci(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    return computed[n]


for machine in machines:
    #print(f"\nmachine: {machine}")
    buttons:list = machine["buttons"]
    prize = [machine["prize"][0]*10_000_000_000_000, machine["prize"][1]*10000000000000]
    
    lowest_tokens = float("inf")
    
    buttons = sorted(buttons, key=lambda x : x[0])
    buttons.reverse()

    max_b1count = 0
    max_b2count = 0

    loop_count = 0


    for i in range(1, FIBB_COUNT+1):
        b1_count = fibonacci(i)
        loop_count += 1
        for j in range(1, FIBB_COUNT+1):
            b2_count = fibonacci(j)
            loop_count += 1
            x_sum = buttons[0][0]*b1_count + buttons[1][0]*b2_count
            y_sum = buttons[0][1]*b1_count + buttons[1][1]*b2_count
            #print(f"\n - trying BTN_1({buttons[0]}) - {b1_count} times  and BTN_2({buttons[1]}) - {b2_count} times  =  [{x_sum}, {y_sum}]", end="")
            if prize[0] < x_sum or prize[1] < y_sum:
                break
            if prize[0] % x_sum == 0 and prize[1] % y_sum == 0:
                    tokens = buttons[0][2] * (prize[0] // x_sum) + buttons[1][2] * (prize[1] // y_sum)
                    if tokens < lowest_tokens:
                        lowest_tokens = tokens
                        #print(f"  |  cost {tokens} - new lowest", end="")
                        continue
                    #print(f"  |  cost {tokens}", end="")
                    continue
            #print(f"  |  doesnt equal", end="")

    if lowest_tokens != float("inf"):
        result += lowest_tokens






print(f"{result}  loops:{loop_count}  fib_count:{FIBB_COUNT}")
print("The time of exec time", (time.time()-start) * 10**3, "ms")