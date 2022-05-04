import turtle

turtle.hideturtle()
turtle.tracer(2)
turtle.pensize(1)
turtle.penup()
turtle.setposition(0, 200)
turtle.pendown()

axiom = "F"
axmTemp = ""
itr = 9

translate = {"+": "+", "-": "-", "F": "F++F-F"}
for k in range(itr):
    for ch in axiom:
        axmTemp += translate[ch]
    axiom = axmTemp
    axmTemp = ""

for ch in axiom:
    if ch == "+":
        turtle.right(90)
    elif ch == "-":
        turtle.left(90)
    elif ch == "F":
        turtle.forward(15)
turtle.update()
turtle.mainloop()
