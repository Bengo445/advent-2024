
f = open('input.txt', "r")

val = 0

l1 = []
l2 = []

for line in f.readlines():
    line = line.split("   ")
    l1.append(int(line[0]))
    l2.append(int(line[1]))

l1.sort()
l2.sort()

for i in range(len(l1)):
    val += abs(l1[i] - l2[i])

print(val)