from table import *
kt1 = KitchenTable(2, 2, 0.7, 5)
dt2 = DeskTable(1.5, 0.8, 0.75)
kt3 = KitchenTable(1, 1.2, 0.8, 3)
ct4 = ComputerTable(1.5, 0.8, 0.75)

# function to display only defined decimal numbers
def to_fixed(n):
    f = format(n, '.2f')
    return f

print('Kitchen table for', kt1.places, 'seat places')
print('Desk table with square', to_fixed(dt2.square()), 'meters')
print('Computer table with square', to_fixed(ct4.square(0.2)), 'meters')

