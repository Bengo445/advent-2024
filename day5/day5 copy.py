f = open("input.txt", "r").read().split("\n\n")


rules = f[0].split("\n")
updates = f[1].split("\n")


order = []
value = 0



counted_nums = {}

for rule in rules:
    num = rule.split("|")[0]
    if num in counted_nums.keys():
        counted_nums[num] += 1
    else:
        counted_nums[num] = 1

rules = sorted(rules, key=lambda rule: counted_nums[rule.split("|")[0]])


holding = []
hold_point = len(order) #mozno +1
x = -50

for i in range(len(rules)):

    rule = rules[i]
    rule = rule.split("|")
    
    # x changed, insert and reset holding and point
    if int(rule[0]) != x:
        print(f"- x changed, inserting holding buffer: {holding} into order at hold_point: {hold_point}")
        for i in range(len(holding)):
            order.insert(hold_point+i, holding[i]) 
        holding = []
        hold_point = len(order) #mozno +1
        print(f"\ncurrent order: {order}")
        
        x = int(rule[0])
        xi = order.index(x) if x in order else -1

        if xi == -1:
            holding.append(x)
            print(f"- new x:{x} not in order, adding to holding ({holding})")
        else:
            hold_point = xi+1
            print(f"- new x:{x} in order, setting hold_point after it ({hold_point})")

    # new y
    y = int(rule[1])
    yi = order.index(y) if y in order else -1

    print(f"-[{rule[0]}|{rule[1]}]")

    if yi == -1:
        holding.append(y)
        print(f"- new y:{y} not in order, adding to holding ({holding})")
    elif yi < hold_point:
        hold_point = yi
        print(f"- new y:{y} in order yi:{yi}, setting hold_point after it ({hold_point})")
    else:
        print(f"- new y:{y} in order yi:{yi}, but hold_point is before so ignoring")

# clear last rule
for i in range(len(holding)):
    order.insert(hold_point, holding[i]) 


print(order)



for update in updates:
    #print(update)
    update_nums = update.split(",")
    for i in range(1, len(update_nums)):
        x1 = int(update_nums[i-1])
        x2 = int(update_nums[i])
        #print(x1,"("+str(order.index(x1))+") >=", x2,"("+str(order.index(x2))+")")
        if order.index(x1) >= order.index(x2):
            break
    else:
        #print(int(update_nums[len(update_nums)//2]))
        value += int(update_nums[len(update_nums)//2])

print(value)
