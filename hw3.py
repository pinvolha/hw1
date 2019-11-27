# variant 5

class Customer:
    bill = 0

    def __init__(self, id0, name0, surname0, partonim0, card0, count0):
        self.__id = id0
        self.name = name0
        self.surname = surname0
        self.patronim = partonim0
        self.__card = card0
        self.count = count0
        print("Hello, Mr(s)", self.name, self.surname)

    def __repr__(self):
        return f"{self.surname}"

    def set_surname(self, new_surname):
        self.surname = new_surname

    def get_surname(self):
        return self.surname

    def get_card(self):
        return self.__card

    def get_count(self):
        print(self.name, "your count is", self.count)
        return self.count

    def __add__(self, bill):
        print(bill, " was added to your count")
        print(self.name, "your count is", self.count + bill, "now")
        return self.count + bill

    def __sub__(self, bill):
        print(bill, " was drawn out your count")
        print(self.name, "your count is", self.count - bill, "now")
        return self.count - bill

    def __del__(self):
        print("Good bye, Mr(s) ", self.name, self.surname)


customers = [Customer(1, "Ivan", "Ivanovich", "Ivanov", 45489584, 1000),
             Customer(2, "Kira", "Kirova", "Kirillovna", 58562365, 2000),
             Customer(3, "Adam", "Adomov", "Adamovich", 96518574, 0)]

customers[0].get_count()
customers[0].__add__(bill=300)

customers[1].set_surname("New-Kirova")
customers[1].get_count()
customers[1].__sub__(bill=50)

customers[2].get_count()
customers[2].__add__(bill=3000)


def bySurname(Customer):
    return Customer.surname

sorted_customers = sorted(customers, key=bySurname)
print("List of customers:", sorted_customers)

min_range = int(input("Enter min range for card number "))
max_range = int(input("Enter max range for card number "))
for i in range(len(customers)):
    if min_range < customers[i].get_card() < max_range:
        print(customers[i].get_surname(), "card in given range")
