# КЛАСС МИНИМУМ 3 МЕТОДА + 3 СВОЙСТВА, ПОЧИТАТЬ ПРО МАГИЧЕСКИЕ МЕТОДЫ


class Beer:
    def __init__(self, color, alco, price):
        self.color = color
        self.alco = alco
        self.price = price
        self.beer_is_available = False

    def is_available(self):
        print("Есть в наличии")
        self.beer_is_available = True

    def info(self):
        status = "B наличии" if self.beer_is_available else "Hет в наличии"
        return f"Beer: {self.color}, {self.alco}%, цена: {self.price}, статус: {status}"


guinness = Beer("dark", 5, "75 000")
print(guinness.info())
print("price", guinness.price)
print("alco ", guinness.alco, "%")

print(guinness.beer_is_available)
guinness.is_available()
print(guinness.beer_is_available)

print(guinness.info())
