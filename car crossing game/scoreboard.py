from turtle import Turtle

FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level = {self.score}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def Game_over(self):
        self.color("red")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over..", align="center", font=FONT)
