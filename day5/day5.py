f = open("input.txt", "r").read().split("\n\n")


rules = f[0].split("\n")
updates = f[1].split("\n")


order = []
value = 0

for rule in rules:
    print(order)

    rule = rule.split("|")
    x = int(rule[0])
    y = int(rule[1])

    xi = order.index(x) if x in order else -1
    yi = order.index(y) if y in order else -1

    print(f"{rule[0]} ({xi}) | {rule[1]} ({yi})")

    if xi == -1:
        if yi <= 0:
            order.insert(0,x)
            print(f"- inserted {x} at beginning")
        else:
            order.insert(yi-1,x)
            print(f"- inserted {x} before {y}")
    if yi == -1:
        if xi == -1:
            order.insert(order.index(x)+1, y)
            print(f"- inserted {y} behind {x}")
        else:
            order.append(y)
            print(f"- appended {y} at end")
        continue

    if yi > xi or (yi == -1 and xi == -1):
        print(f"- ok")
        continue

    order.pop(yi)
    #order.insert(xi+1, y)
    order.append(y)
    print(f"- moved {y} to the end")

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
