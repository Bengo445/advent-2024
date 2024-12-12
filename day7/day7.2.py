
f = open("input.txt", "r")

correct = 0

def generate_ternary_combinations(n):
    if n == 0:
        return [[]]  # Base case: one combination of length 0
    smaller_combinations = generate_ternary_combinations(n - 1)
    result = []
    for combo in smaller_combinations:
        for digit in [-1, 0, 1]:
            result.append(combo + [digit])
    return result

_c = 0
for line in f.readlines():
    _c+=1
    print(_c)

    _line = line.strip().split(":")
    testvalue = int(_line[0])
    values = list(map(int, _line[1].strip().split(" ")))

    combinations = generate_ternary_combinations(len(values)-1)

    #print(f"{testvalue}: {values}")

    for combo in combinations:
        
        result = values[0]
        for i, trit in enumerate(combo):
            if trit == -1:
                result = result + values[i+1]
                #print(f"{i}: {values[i]}+{values[i+1]}")
            elif trit == 0:
                result = result * values[i+1]
                #print(f"{i}: {values[i]}*{values[i+1]}")
            else:
                result = int(str(result) + str(values[i+1]))
                #print(f"{i}: {values[i]}||{values[i+1]}")

        #print(f"result: {result}")
        
        if result == testvalue:
            correct += result
            break






print(correct)