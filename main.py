import turtle

drawing_board= turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance= turtle.Turtle()
def turtle_forward():
    turtle_instance.forward(100)
def angle_right():
    turtle_instance.right(turtle_instance.heading()-10)
def angle_left():
    turtle_instance.left(turtle_instance.heading()+10)
def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()
def turtle_pen_up():
    turtle_instance.penup()
def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun= turtle_forward , key="space")
drawing_board.onkey(fun= angle_right , key="Down")
drawing_board.onkey(fun= angle_left , key="Up")
drawing_board.onkey(fun= clear_screen , key="z")
drawing_board.onkey(fun= turtle_return_home , key="x")
drawing_board.onkey(fun= turtle_pen_up , key="c")
drawing_board.onkey(fun= turtle_pen_down , key="v")



drawing_board.mainloop()
