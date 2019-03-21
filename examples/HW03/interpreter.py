from turtle import *

def interpret(pgm):
    t = Turtle()
    for instr in pgm:
        if instr == 'F':
            t.forward(10)
        elif instr == 'L':
            t.left(60)
        elif instr == 'R':
            t.right(120)
        else:
            print('Syntax error n "{}"'.format(instr))
    t.hideturtle()
    exitonclick()

interpret('FLFRFLFRFLFRFLFRFLFRFLFR')
