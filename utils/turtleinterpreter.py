import turtle
import turtle as tur
import lsystem as ls


class TurtleInterpreter:
    def __init__(self, ulen):
        # self.sequence = sequence
        # self.ulen = ulen
        # self.delta = delta
        # self.inHeading = inHeading

        self.ulen = ulen

        self.harold = tur.Turtle()
        self.screen = tur.Screen()

        self.cansize = 400 * self.ulen

        tur.screensize(canvwidth=self.cansize, canvheight=self.cansize)
        self.harold.speed(0)

        self.screen.onclick(self.clear_screen)

    def draw(self, sequence, delta, inHeading):

        print(sequence)

        # t = tur.Turtle()
        # screen = tur.Screen()
        # tur.TurtleScreen.resetscreen(screen)

        # t.left(self.inHeading)

        self.harold.clear()

        self.harold.penup()
        self.harold.setpos(0, 0)
        self.harold.pendown()
        self.harold.left(inHeading)

        pos_stack = []
        head_stack = []

        for i in range(len(sequence)):
            if sequence[i] == "+":
                self.harold.left(delta)  # Turn left from heading
            elif sequence[i] == "-":
                self.harold.right(delta)  # Turn right from heading
            elif sequence[i] == "F":
                self.harold.forward(self.ulen)
            elif sequence[i] == "f":
                self.harold.penup()
                self.harold.forward(self.ulen)
                self.harold.pendown()
            elif sequence[i] == "[":
                pos_stack.append(self.harold.pos())
                head_stack.append(self.harold.heading())
            elif sequence[i] == "]":
                self.harold.penup()
                self.harold.setpos(pos_stack.pop())
                self.harold.setheading(head_stack.pop())
                self.harold.pendown()

        # tur.mainloop()

        # tur.getscreen()
        # screen.clear()

        # self.screen.exitonclick()

        # self.screen.onclick(self.clear_screen)

        # self.screen.exitonclick()

        # screen.clear()
        # screen.exitonclick()
        # tur.clear()
        # t.clear()

        # t.clear()

        #self.harold.clear()




        turtle.onclick(self.do_nothing)
    def do_nothing(self, float1, float):
        return None

        #tur.mainloop()

    def clear_screen(self, float1, float2):
        self.harold.clear()
        return


def main():
    cancer_hilbert_string = '+-+BF-AFA-FB+F+-AF+BFB+FA-F-AF+BFB+FA-+F+BF-AFA-FB+-F-+-AF+BFB+FA-F-+BF-AFA-FB+F+BF-AFA-FB+-F-AF+BFB+FA-+F+-AF+BFB+FA-F-+BF-AFA-FB+F+BF-AFA-FB+-F-AF+BFB+FA-+-F-+BF-AFA-FB+F+-AF+BFB+FA-F-AF+BFB+FA-+F+BF-AFA-FB+-+'

    ti = TurtleInterpreter(10)

    # ti.draw('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 90, 0)

    ti.draw(cancer_hilbert_string, 90, 0)

    ti.draw(cancer_hilbert_string, 90, 0)



    ti.draw("+-AF+BFB+FA-F-+BF-AFA-FB+F+BF-AFA-FB+-F-AF+BFB+FA-+", 90, 0)


if __name__ == '__main__':
    main()
