from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        if side == "right":
            self.goto(x=350, y=0)
        else:
            self.goto(x=-350, y=0)

    def up(self):
        if 250 > self.ycor():
            new_y = self.ycor() + 20
        else:
            new_y = self.ycor()
        self.sety(new_y)

    def down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
        else:
            new_y = self.ycor()
        self.sety(new_y)

