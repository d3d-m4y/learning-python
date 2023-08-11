from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
GO_FONT = ("Arial", 28, "bold")


class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.goto(x=0, y=265)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def write_high_score(self):
        with open("high_score", "w") as file:
            file.write(str(self.high_score))

    def read_high_score(self):
        with open("high_score") as file:
            high_score = file.read()
            return high_score

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER, nerd...", align=ALIGNMENT, font=GO_FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()
