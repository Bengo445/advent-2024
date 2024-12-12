
f = open('input.txt', "r")

safe = 0

for line in f.readlines():
    line = list(map(int, line.strip().split(" ") ))
    print(line)

    # get sort direction
    sorted_dir = 0
    if line[0] < line[-1]:
        sorted_dir = 1
    elif line[0] > line[-1]:
        sorted_dir = -1
    else:
        print("first and last equal??")
        continue
    
    # validate
    for i in range(1, len(line)):
        x0 = line[i-1]
        x1 = line[i]

        # check sorted
        if (x0*sorted_dir < x1*sorted_dir) == False:
            print("unsorted")
            break

        # check distance
        diff = abs(x0-x1)
        if diff > 3 or diff < 1:
            print("wrong distance")
            break
    else:
        print("- safe")
        safe += 1
        continue

    print("- unsafe")



print("\nSAFE NUMBERS:", safe)