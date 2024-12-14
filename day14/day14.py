
class Vector2:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    def __str__(self):
        return f"[{self.x}, {self.y}]"
class Robot:
    def __init__(self, pos:Vector2, vel:Vector2):
        self.pos = pos
        self.vel = vel
    def __str__(self):
        return f"Robot(pos{self.pos} vel{self.vel})"
    


robots:list[Robot] = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip().strip("p=").split(" v=")
        posx, posy = list(map(int, line[0].split(",")))
        vx, vy = list(map(int, line[1].split(",")))
        robots.append(Robot(Vector2(posx,posy), Vector2(vx,vy)))

WIDTH = 101
HEIGHT = 103
TIME_TO_PASS = 100
quads = [[0,0], [0,0]] # [[tl,tr], [bl,br]]

# board = []
# for y in range(HEIGHT):
#     board.append([])
#     for x in range(WIDTH):
#         board[y].append(0)

for robot in robots:
    robot.pos.x = (robot.pos.x + robot.vel.x * TIME_TO_PASS) % WIDTH
    robot.pos.y = (robot.pos.y + robot.vel.y * TIME_TO_PASS) % HEIGHT
    #print(robot)
    if robot.pos.y < (HEIGHT//2):
        if robot.pos.x < (WIDTH//2):
            quads[0][0] += 1
            #print("tl")
        elif robot.pos.x > (WIDTH//2):
            quads[0][1] += 1
            #print(f"tr ({robot.pos.x} < {(WIDTH//2)}-{robot.pos.x < (WIDTH//2)})")
    elif robot.pos.y > (HEIGHT//2):
        if robot.pos.x < (WIDTH//2):
            quads[1][0] += 1
            #print(f"bl ({robot.pos.x} < {(WIDTH//2)}-{robot.pos.x < (WIDTH//2)})")
        elif robot.pos.x > (WIDTH//2):
            quads[1][1] += 1
            #print(f"br ({robot.pos.x} > {(WIDTH//2)}-{robot.pos.x > (WIDTH//2)})")
    #board[robot.pos.y][robot.pos.x] += 1

# for y in range(HEIGHT):
#     print()
#     for x in range(WIDTH):
#         print(board[y][x], end=" ")
# print()


print(quads[0][0] * quads[0][1] * quads[1][0] * quads[1][1])
#print(quads, HEIGHT//2, WIDTH//2)



