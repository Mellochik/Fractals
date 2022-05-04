import turtle

axiom = "FX"
axmTemp = ""

itr = 15  # итераций 
dl = 3   # длина черты

turtle.hideturtle()
turtle.tracer(60)
turtle.penup()
turtle.setpos(-100, -150)
turtle.pendown()

# код переделан,
# если символ переходит в новую строку без изменений,
# то его не обязательно вносить в правила
translate={"X":"X+YF+", "Y":"-FX-Y"}

for k in range(itr):
    for ch in axiom:
        if ch in translate:
            axmTemp += translate[ch]
        else:
            axmTemp += ch
    axiom = axmTemp
    axmTemp = ""
    
for ch in axiom:
    if   ch == "+":
        turtle.right(90)
    elif ch == "-":
        turtle.left(90)
    elif ch == "F":
        turtle.forward(dl)
turtle.update()
turtle.mainloop()


























