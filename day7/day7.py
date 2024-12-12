
f = open("input.txt", "r")

correct = 0


for line in f.readlines():
    _line = line.strip().split(":")
    testvalue = int(_line[0])
    values = list(map(int, _line[1].strip().split(" ")))

    #print(f"{testvalue}: {values}")
    for n in range(pow(2, len(values)-1)):
        
        result = values[0]
        bitval = n
        #print(f"n:{n}")
        i = 0
        for j in range(len(values)-2, -1, -1):
            op_val = pow(2, j)
            if bitval >= op_val:
                bitval -= op_val
                result = result*values[i+1]
                #print(f"{i}: {values[i]}*{values[i+1]}")
            else:
                result = result+values[i+1]
                #print(f"{i}: {values[i]}+{values[i+1]}")
            i+=1

        #print(f"result: {result}")
        
        if result == testvalue:
            correct += testvalue
            break



print(correct)