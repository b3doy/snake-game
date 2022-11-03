from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier new", 12, "bold")

class Papanskor(Turtle):
    def __init__(self):
        super().__init__()
        self.skor = 0
        self.penup()
        self.color("white")
        self.setpos(0, 280)
        self.hideturtle()
        self.update_papanskor()

    def update_papanskor(self):
        self.write(f"Score: {self.skor}", move=False, align=ALIGNMENT, font=FONT)

    def tambah_skor(self):
        self.clear()
        self.skor += 1
        self.update_papanskor()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)