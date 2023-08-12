import pandas
import turtle

BG_IMAGE = "images\\blank_states_img.gif"

screen = turtle.Screen()
screen.title("Guess the US State Name")

screen.addshape(BG_IMAGE)
turtle.shape(BG_IMAGE)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
