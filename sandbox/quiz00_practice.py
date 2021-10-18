"""Quiz practice for Quiz_00 in COMP110."""

__author__ = "730463762"

a: str = "a"
b: str = "a" + "c"
print(b + a)
b = b + "b"
a = a + b[len(a) + 1]
print(a[1])

print(type(int("20")))
print(len(str(110)))
print(55 % 2 ** 4)
print(2 + 2 / 2 ** (2 * 0))
print(int("10" + "40"))
