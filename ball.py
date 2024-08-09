from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(x=0, y=0)
        self.x_move = 0.2
        self.y_move = 0.2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, side):
        if side == "paddle":
            self.x_move *= -1
        else:
            self.y_move *= -1

    def increase_speed(self):
        self.x_move *= 1.01
        self.y_move *= 1.01

    def centre(self):
        self.goto(0, 0)
        self.x_move /= abs(self.x_move) * 5
        self.y_move /= abs(self.y_move) * 5
