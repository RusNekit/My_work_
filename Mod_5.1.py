class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей {self.number_of_floors} "

    def __int__(self):
        return f"Название: {self.name}, количество этажей {self.number_of_floors} "

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self.number_of_floors
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        else:
            if isinstance(other, House):
                return self.name == other.name and self.number_of_floors == other.number_of_floors
            else:
                return NotImplemented

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        else:
            if isinstance(other, House):
                return self.number_of_floors < other.number_of_floors or self.name < other.name
            else:
                return NotImplemented

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors <= other
        else:
            if isinstance(other, House):
                return self.number_of_floors <= other.number_of_floors and self.name <= other.name
            else:
                return NotImplemented

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        else:
            if isinstance(other, House):
                return self.number_of_floors > other.number_of_floors or self.name > other.name
            else:
                return NotImplemented

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(f"Название: ЖК Эльбрус, количество этажей {h1}")
print(h1 == h2)

h1 += 10  # __iadd__
print(f"Название: ЖК Эльбрус, количество этажей {h1}")

h2 = 10 + h2  # __radd__
print(f"Название: ЖК Акация, количество этажей {h2}")

print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)