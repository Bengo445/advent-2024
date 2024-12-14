import re
chunks = [[[int(y) for y in re.findall(r'\d+', x)] for x in l.split('\n')] for l in open('input.txt').read().split('\n\n')]
total = 0
part2 = True
for c in chunks:
    print()
    if part2:
        c[-1][0] += 10000000000000
        c[-1][1] += 10000000000000
    x1, x2, y1, y2 = c[0][0], c[1][0], c[0][1], c[1][1] # set up matrix 
    det_denom = x1 * y2 - x2 * y1 # denominator of determinant of matrix under question
    if det_denom == 0: # A and B are linearly dependent
        n1 = c[-1][0] // x1 # number of times to press A to get to goal if integer
        n2 = c[-1][0] // x2 # number of times to press B to get to goal if integer
        if [n1 * x1, n1 * y1] == c[-1] and 3 * n1 < n2: # button A is better and works
            total += 3 * n1
        elif [n2 * x2 , n2 * y2] == c[-1]: # button B is better and works
            total += n2
    else: # A and B are linearly independent, so solve the system of 2 equations in 2 unknowns
        x, y = c[-1][0], c[-1][1]
        a, b = int((x*y2 - x2* y)/det_denom), int((x1* y -x * y1)/ det_denom)
        if a * x1 + b * x2 == x and a * y1 + b * y2 == y: # if integer solution exists
            total += 3 * a + b
print(total)