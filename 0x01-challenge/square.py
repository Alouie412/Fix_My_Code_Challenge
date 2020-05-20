#!/usr/bin/python3
"""
Docstring
"""


class rect():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Documentation """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square
            Here is the error """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Documentation """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Documentation """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = rect(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
