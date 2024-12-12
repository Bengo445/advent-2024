
f = open('input.txt', "r")

val = 0

l1 = []
l2 = {}

for line in f.readlines():
    line = line.split("   ")
    l1.append(int(line[0]))
    line[1] = line[1].strip("\n")
    if line[1] in l2.keys():
        l2[line[1]] += 1
    else:
        l2[line[1]] = 1


for i in range(len(l1)):
    if str(l1[i]) in l2.keys():
        val += l1[i] * l2[str(l1[i])]


print(val)