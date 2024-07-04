class Movie:
    def __init__(self, title, director, year):
        self.title=title
        self.director=director
        self.year=year

tlk=Movie("The Lion King", "Roger Allers and Rob Minkoff", 1994)
f=Movie("Frozen","Chris Buck and Jennifer Lee",2013)
up=Movie("Up","Pete Docter and Bob Peterson",2009)

print(tlk.title)
print(tlk.director)
print(f.title)
print(f.director)
print(up.title)
print(up.director)

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

john=Person("John",36)
print(john.name)
john.age=40
print(john.age)