from turtle import Turtle

FONT = ("Courier", 80, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(arg=self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 180)
        self.write(arg=self.r_score, align=ALIGN, font=FONT)

    def r_point(self):
        self.r_score += 1
        self.write_score()

    def l_point(self):
        self.l_score += 1
        self.write_score()
