from turtle import Turtle

ALIGNMENT ="center"
FONT =("Arial",25,"normal")
SCOREBOARD_POSITION = 0,270
SCOREBOARD_COLOR = "white"
GAME_OVER_DISPLAY_COORDINATES =0,0

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
            data.close()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.speed("fastest")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt" , "w") as data:
                data.write(f"{self.high_score}")
        self.write(f"score :{self.score}  | Highest Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.update_scoreboard()


    def increase_the_score(self):
        self.score+=1


