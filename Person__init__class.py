class Person:
    qualit: int

    def __init__(self, n, s, qu=1):
        self.name = n
        self.surname = s
        self.qualit = qu

    def get_info(self):
        print(self.name, self.surname, self.qualit)


    def __del__(self):
        print('Goodbye Mr. ', self.surname)


# --------------------------------------------------
p1 = Person("John", "Smith")
p2 = Person("Matt", "Swan", 4)
p3 = Person("Edd", "Collins", 2)


p1.get_info()
p2.get_info()
p3.get_info()

quallist = []
for skill in p1.qualit, p2.qualit, p3.qualit:
    quallist.append(skill)
weak = min(quallist)
for pers in p1, p2, p3:
    if pers.qualit == weak:
        pers.__del__()
input()

