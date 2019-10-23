# main class Table: properties and methods of subclasses are not available for class
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

# subclass KitchenTable of class Table: can use all properties and methods of class Table
class KitchenTable(Table):
    def __init__(self, l, w, h, p):     # call parent constructor __init__() with child own additions
        Table.__init__(self, l, w, h)
        self.places = p

# subclass DeskTable of class Table
class DeskTable(Table):
    def square(self):
        return self.width * self.length
# to avoid duplicates in child class we can call parent class's method and manipulate with this one.
class ComputerTable(DeskTable):
    def square(self, e):
        return DeskTable.square(self) - e