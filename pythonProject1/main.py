from turtle import Turtle, Screen

anas = Turtle()
print(anas)
anas.shape("turtle")
anas.color("magenta")
anas.shapesize()
for i in range(10):
    for c in ("RoyalBlue", "LightCoral", "orchid", "salmon"):
        anas.pencolor(c)
        anas.left(10)
        anas.forward(300)
        anas.left(10)
        anas.backward(300)


my_display = Screen()
print(my_display.canvheight)
my_display.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokerman", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
#
# table.align = "l "
#
# print(table)
