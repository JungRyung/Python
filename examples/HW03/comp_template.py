prologue = '''
from turtle import *
def main():
    t = Turtle()
'''

epilogue = '''
    t.hideturtle()
    exitonclick()
main()
'''

def translate(ofile, pgm):
    for instr in pgm:
        switch = {
            'F':lambda: ofile.write('    t.forward(10)\n'),
            'L':lambda: ofile.write('    t.left(60)\n'),
            'R':lambda: ofile.write('    t.right(120)\n')
        }
        switch[instr]()

import sys

if len(sys.argv) < 2:
    print('Usage: {} {}'.format(sys.argv[0], 'Koch_pgm'))
else:
    ifile = open(sys.argv[1], 'r')
    ofile = open('a.py', 'w')
    pgm = ifile.readline().strip()
    ofile.write(prologue)
    translate(ofile, pgm)
    ofile.write(epilogue)
    ofile.close()
    ifile.close()
