
f = open('input.txt', "r")

safe = 0

for full_line in f.readlines():
    full_line = list(map(int, full_line.strip().split(" ") ))

    # iterate through 
    for removed_i in range(-1, len(full_line)):
        line = full_line.copy()
        if removed_i >= 0:
            line.pop(removed_i)
            print(" / ", end="")
        print(line, end=" ")

        # get sort direction
        sorted_dir = 0
        if line[0] < line[-1]:
            sorted_dir = 1
        elif line[0] > line[-1]:
            sorted_dir = -1
        else:
            print("first and last equal??", end="")
            continue
        
        # validate
        for i in range(1, len(line)):
            x0 = line[i-1]
            x1 = line[i]

            # check sorted
            if (x0*sorted_dir < x1*sorted_dir) == False:
                print("unsorted", end="")
                break

            # check distance
            diff = abs(x0-x1)
            if diff > 3 or diff < 1:
                print("wrong distance", end="")
                break
        else:
            safe += 1
            print(" - safe")
            break

        print(" - unsafe")



print("\nSAFE NUMBERS:", safe)