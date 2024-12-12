f = open("input.txt", "r")

memory = f.read().split("mul(")
memory.pop(0)

value = 0

for block in memory:
    values = block.split(",", 1)
    print(values)
    
    # check if valid syntax
    if len(values) <= 1:
        continue
    if len(values[0]) > 3:
        continue
    if values[0].isnumeric() == False:
        continue
    
    #get values
    x1 = int(values[0])
    x2 = ''
    for i in range(len(values[1])):
        if values[1][i].isnumeric() and i < 3:
            x2 += str(values[1][i])
        else:
            if (values[1][i] == ")") == False:
                x2 = ''
            break

    if x2 == '':
        continue
    x2 = int(x2)
    print(x1, x2, "=", x1*x2)

    value += x1*x2
    
print(value)