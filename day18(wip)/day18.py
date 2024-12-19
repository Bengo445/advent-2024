

falling = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        falling.append( list(map(int, line.strip().split(",") )))
falling = set(falling)

GRID_SIZE = 7 #0-6


# pathfinding