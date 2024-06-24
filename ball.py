import tkinter as tk
import time
import math

class BallApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Balls with Physics")
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.create_ball)
        self.balls = []
        self.max_balls = 50
        self.frame_count = 0

    def create_ball(self, event):
        if len(self.balls) < self.max_balls:
            ball = {
                "x": event.x,
                "y": event.y,
                "dx": 0,
                "dy": 2,
                "radius": 10,
                "shape": self.canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill="blue"),
                "trail": []
            }
            self.balls.append(ball)
            self.animate_ball()

    def animate_ball(self):
        while self.balls:
            self.frame_count += 1
            for ball in self.balls:
                coords = self.canvas.coords(ball["shape"])
                ball["x"], ball["y"] = (coords[0] + coords[2]) / 2, (coords[1] + coords[3]) / 2

                prev_x, prev_y = ball["x"], ball["y"]

                self.canvas.move(ball["shape"], ball["dx"], ball["dy"])

                coords = self.canvas.coords(ball["shape"])
                ball["x"], ball["y"] = (coords[0] + coords[2]) / 2, (coords[1] + coords[3]) / 2

                ball["trail"].append((prev_x, prev_y, ball["x"], ball["y"]))
                self.canvas.create_line(prev_x, prev_y, ball["x"], ball["y"], fill="gray")

                if coords[3] >= self.canvas.winfo_height():
                    ball["dy"] = -ball["dy"]
                    self.canvas.coords(ball["shape"], coords[0], self.canvas.winfo_height() - 2 * ball["radius"], coords[2], self.canvas.winfo_height())
                else:
                    ball["dy"] += 0.1

                if abs(ball["dy"]) < 0.1 and coords[3] >= self.canvas.winfo_height():
                    ball["dy"] = 0

                if coords[0] <= 0 or coords[2] >= self.canvas.winfo_width():
                    ball["dx"] = -ball["dx"]

            self.check_collisions()
            self.root.update()

            if self.frame_count % 50 == 0:
                self.cleanup_trails()

            time.sleep(0.01)

    def check_collisions(self):
        for i, ball1 in enumerate(self.balls):
            for j, ball2 in enumerate(self.balls):
                if i != j:
                    dx = ball2["x"] - ball1["x"]
                    dy = ball2["y"] - ball1["y"]
                    distance = math.sqrt(dx**2 + dy**2)
                    if distance < ball1["radius"] + ball2["radius"]:
                        angle = math.atan2(dy, dx)
                        sin = math.sin(angle)
                        cos = math.cos(angle)

                        x1 = 0
                        y1 = 0

                        x2 = dx * cos + dy * sin
                        y2 = dy * cos - dx * sin

                        vx1 = ball1["dx"] * cos + ball1["dy"] * sin
                        vy1 = ball1["dy"] * cos - ball1["dx"] * sin

                        vx2 = ball2["dx"] * cos + ball2["dy"] * sin
                        vy2 = ball2["dy"] * cos - ball2["dx"] * sin

                        vx1_final = vx2
                        vx2_final = vx1

                        ball1["dx"] = vx1_final * cos - vy1 * sin
                        ball1["dy"] = vy1 * cos + vx1_final * sin
                        ball2["dx"] = vx2_final * cos - vy2 * sin
                        ball2["dy"] = vy2 * cos + vx2_final * sin

                        overlap = 0.5 * (ball1["radius"] + ball2["radius"] - distance + 1)
                        ball1["x"] -= math.cos(angle) * overlap
                        ball1["y"] -= math.sin(angle) * overlap
                        ball2["x"] += math.cos(angle) * overlap
                        ball2["y"] += math.sin(angle) * overlap

                        self.canvas.coords(ball1["shape"], ball1["x"] - ball1["radius"], ball1["y"] - ball1["radius"],
                                           ball1["x"] + ball1["radius"], ball1["y"] + ball1["radius"])
                        self.canvas.coords(ball2["shape"], ball2["x"] - ball2["radius"], ball2["y"] - ball2["radius"],
                                           ball2["x"] + ball2["radius"], ball2["y"] + ball2["radius"])

    def cleanup_trails(self):
        for ball in self.balls:
            if len(ball["trail"]) > 100:
                ball["trail"] = ball["trail"][-100:]

root = tk.Tk()
app = BallApp(root)
root.mainloop()
