# # LSystem.py
# """
# Created on Thu Feb  3 15:42:41 2022
#
# @author: Vinny Houh
# """
# import turtle as tur
# import lsystem as ls
#
#
# class TurtleInterpreter:
#     def __init__(self, sequence, ulen, delta, in_heading):
#         self.sequence = sequence
#         self.ulen = ulen
#         self.delta = delta
#         self.inHeading = in_heading
#
#     def draw(self):
#
#         can_size = 3000 * self.ulen
#
#         t = tur.Turtle()
#         screen = tur.Screen()
#         t.pensize(2)
#         t.pencolor("white")
#         tur.Screen().bgcolor("black")
#         tur.tracer(0, 0)
#
#         tur.screensize(canvwidth=can_size, canvheight=can_size)
#         t.speed(0)
#
#         t.left(self.inHeading)
#
#         pos_stack = []
#         head_stack = []
#
#         position_stack = []
#
#         for i in range(len(self.sequence)):
#             if self.sequence[i] == "+":
#                 t.left(self.delta)  # Turn left from heading
#             elif self.sequence[i] == "-":
#                 t.right(self.delta)  # Turn right from heading
#             elif self.sequence[i] == "F":
#                 t.forward(self.ulen)
#             elif self.sequence[i] == "f":
#                 t.penup()
#                 t.forward(self.ulen)
#                 t.pendown()
#             elif self.sequence[i] == "[":
#
#                 position_stack.append((t.pos(), t.heading()))
#
#             elif self.sequence[i] == "]":
#                 t.penup()
#
#                 new_pos, new_heading = position_stack.pop()
#                 t.setpos(new_pos)
#                 t.setheading(new_heading)
#
#                 t.pendown()
#
#         tur.update()
#         ts = tur.getscreen()
#         screen.exitonclick()
#         # tur.mainloop()
#
#
# def main():
#
#     # CustomTree
#     # custom_dict2 = {'X': 'F[+X[---X]]F[---X]+X',
#     #               'F': 'FF',
#     #               "[": "[",
#     #               "]": "]",
#     #               "+": "+",
#     #               "-": "-"}
#     # customsys2 = ls.LSystem(['X', 'F'], 'X', custom_dict2)
#     # customsysStr2 = customsys2.l_string(7)
#
#     example_dict = {'F': 'FF[+X]', 'X': '-X[+F]+X[-F]-X', '[': '[', ']': ']', '+': '+', '-': '-'}
#     sys = ls.LSystem([], 'F', example_dict)
#     sys_str = sys.l_string(7)
#
#     custom2 = TurtleInterpreter(sys_str[6], 5, 31.2, 90)
#     custom2.draw()
#
#
# if __name__ == '__main__':
#     main()
