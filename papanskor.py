from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier new", 12, "bold")

class Papanskor(Turtle):
    def __init__(self):
        super().__init__()
        self.skor = 0
        with open("data.txt") as data_skor:
            self.skor_tertinggi = int(data_skor.read()) 
        self.penup()
        self.color("white")
        self.setpos(0, 280)
        self.hideturtle()
        self.update_papanskor()

    def update_papanskor(self):
        self.clear()
        self.write(f"Score: {self.skor}, Highscore: {self.skor_tertinggi}", move=False, align=ALIGNMENT, font=FONT)

    def tambah_skor(self):
        self.skor += 1
        self.update_papanskor()

    def game_over(self):
        if self.skor > self.skor_tertinggi:
            self.skor_tertinggi = self.skor
            with open("data.txt", mode='w') as data_skor:
                data_skor.write(str(self.skor_tertinggi))
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)