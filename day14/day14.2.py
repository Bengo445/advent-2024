import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageDraw, ImageTk


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

class NumberImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("skibi")

        self.time = 6000 #---------------------------------------------------------------------- starting time value

        self.grid_rows = 9 #-------------------------------------------------------------------- rows
        self.grid_cols = 18 #------------------------------------------------------------------- cols

        self.left_button = tk.Button(root, text="\u25C0", command=self.dec_number)
        self.left_button.grid(row=0, column=0, columnspan=5)

        self.number_label = tk.Label(root, text=str(f"Time: {self.time}"), font=("Times New Roman", 24))
        self.number_label.grid(row=0, column=5, columnspan=5)

        self.right_button = tk.Button(root, text="\u25B6", command=self.inc_number)
        self.right_button.grid(row=0, column=10, columnspan=5)

        self.canvas = Canvas(root, width=10, height=10)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.canvas_grid = []
        for i in range(self.grid_rows):
            row = []
            for j in range(self.grid_cols):
                canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
                canvas.grid(row=i + 1, column=j)
                row.append(canvas)
            self.canvas_grid.append(row)

        self.update_images()

    def create_image(self, offset):
        img = Image.new("RGB", (WIDTH, HEIGHT), "black")
        draw = ImageDraw.Draw(img)

        for robot in robots:
            x = (robot.pos.x + robot.vel.x * (self.time+offset)) % WIDTH
            y = (robot.pos.y + robot.vel.y * (self.time+offset)) % HEIGHT
            draw.point((x, y), fill="white")
        draw.text((5, 5), str(offset), fill="white")
        return ImageTk.PhotoImage(img)

    def update_images(self):
        for i in range(self.grid_rows):
            for j in range(self.grid_cols):
                photo = self.create_image(self.grid_cols*i+j)
                self.canvas_grid[i][j].create_image(WIDTH//2, HEIGHT//2, image=photo)
                self.canvas_grid[i][j].photo = photo

    def inc_number(self):
        self.time += self.grid_rows * self.grid_cols
        self.number_label.config(text=str(f"Time: {self.time}"))
        self.update_images()

    def dec_number(self):
        self.time -= self.grid_rows * self.grid_cols
        self.number_label.config(text=str(f"Time: {self.time}"))
        self.update_images()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberImageApp(root)
    root.mainloop()
