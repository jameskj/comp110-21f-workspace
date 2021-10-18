"""Working with Variables and Operators."""

__author__ = "730463762"

Left = input("Left-hand side: ")
Right = input("Right-hand side: ")
Answer1 = int(Left) ** int(Right)
Answer2 = int(Left) / int(Right)
Answer3 = int(Left) // int(Right)
Answer4 = int(Left) % int(Right)
print(str(Left) + " ** " + str(Right) + " is " + str(Answer1))
print(str(Left) + " / " + str(Right) + " is " + str(Answer2))
print(str(Left) + " // " + str(Right) + " is " + str(Answer3))
print(str(Left) + " % " + str(Right) + " is " + str(Answer4))