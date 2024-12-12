f = open("input.txt", "r")

memory = f.read().split("mul(")

value = 0
enabled = True

for block in memory:
    if enabled:
        values = block.split(",", 1)
        print(values)

        # check if valid syntax
        if len(values) <= 1:
            print("- No values found")
            continue
        if len(values[0]) > 3:
            print("- First value too long")
            continue
        if values[0].isnumeric() == False:
            print("- First value is NaN")
            continue
        
        #get values
        x1 = int(values[0])
        x2 = ''
        for i in range(len(values[1])):
            if values[1][i].isnumeric() and i < 3:
                x2 += str(values[1][i])
            else:
                if (values[1][i] == ")") == False:
                    print("- Second bracket isnt )")
                    x2 = ''
                break

        if x2 == '':
            print("- No second value")
            continue
        x2 = int(x2)
        print(x1, x2, "=", x1*x2)

        value += x1*x2
    
    while ("do()" in block) or ("don't()" in block):
        do_i = block.find("do()")
        dont_i = block.find("don't()")

        if (do_i != -1) and (do_i < dont_i or dont_i == -1):
            block = block.replace("do()", "", 1)
            enabled = True
        elif (dont_i != -1) and (dont_i < do_i or do_i == -1):
            block = block.replace("don't()", "", 1)
            enabled = False



    
    
print(value)