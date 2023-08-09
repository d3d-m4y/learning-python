from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
GO_FONT = ("Arial", 28, "bold")

class Scoreboard(Turtle):
    
    
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.hideturtle()
        self.goto(x=0, y=265)
        self.color("white")
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER, nerd...", align=ALIGNMENT, font=GO_FONT)