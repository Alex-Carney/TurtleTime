import turtle as tur
import lsystem as ls

class TurtleInterpreter:
    def __init__(self, sequence, ulen, delta, inHeading):
        self.sequence = sequence
        self.ulen = ulen
        self.delta = delta
        self.inHeading = inHeading

    def draw(self):


        cansize = 3000 * self.ulen

        t = tur.Turtle()
        screen = tur.Screen()
        t.pensize(2)
        t.pencolor("white")
        tur.Screen().bgcolor("black")
        tur.tracer(0, 0)

        tur.screensize(canvwidth=cansize, canvheight=cansize)
        t.speed(0)

        t.left(self.inHeading)

        posStack = []
        headStack = []

        for i in range(len(self.sequence)):
            if self.sequence[i] == "+":
                t.left(self.delta)  # Turn left from heading
            elif self.sequence[i] == "-":
                t.right(self.delta)  # Turn right from heading
            elif self.sequence[i] == "F":
                t.forward(self.ulen)
            elif self.sequence[i] == "f":
                t.penup()
                t.forward(self.ulen)
                t.pendown()
            elif self.sequence[i] == "[":
                posStack.append(t.pos())
                headStack.append(t.heading())
            elif self.sequence[i] == "]":
                t.penup()
                t.setpos(posStack.pop())
                t.setheading(headStack.pop())
                t.pendown()

        tur.update()
        ts = tur.getscreen()
        screen.exitonclick()
        #tur.mainloop()


def main():
    # Tree d
    treeDdic = {'X': 'F[+X]F[-X]+X',
                'F': 'FF',
                "[":"[",
                "]":"]",
                "+":"+",
                "-":"-"}
    treeDsys = ls.LSystem(['X', 'F'], 'X', treeDdic)
    treeDsysStr = treeDsys.l_string(7)

    treeD = TurtleInterpreter(treeDsysStr[7], 5, 20, 90)
    #treeD.draw()



    # CustomTree
    customDic = {'X': 'F[X]F[+X]F[-X]F[X]',
                'F': 'FF',
                "[": "[",
                "]": "]",
                "+": "+",
                "-": "-"}
    #customsys = ls.LSystem(['X', 'F'], 'X', customDic)
    #customsysStr = customsys.l_string(7)

    #custom = TurtleInterpreter(customsysStr[6], 5, 25, 90)
    #custom.draw()

    # CustomTree
    customDic2 = {'X': 'F[+X[---X]]F[---X]+X',
                 'F': 'FF',
                 "[": "[",
                 "]": "]",
                 "+": "+",
                 "-": "-"}
    customsys2 = ls.LSystem(['X', 'F'], 'X', customDic2)
    customsysStr2 = customsys2.l_string(7)

    custom2 = TurtleInterpreter(customsysStr2[6], 5, 15, 90)
    custom2.draw()


if __name__ == '__main__':
    main()