# На вход программе подаются два вещественных числа, записанных в одну строку через пробел.
# Необходимо их прочитать и вывести на экран наибольшее из этих чисел.
# Задачу решить с помощью условного оператора

# a, b = input().split()
# print(a)
# print(b)
# a = float(a)
# b = float(b)
# if a > b:
#     print(a)
# else:
#     print(b)

# ----------------------
# n = input()
# n = n.split(" ")
# a = float(n[0])
# b = float(n[1])
# print(a, type(a))
# if a > b:
#     print(a)
# else:
#     print(b)

# ----------------------
# n = [float(el) for el in input().split(" ")]
# print(n[0] if n[0] > n[1] else n[1])

# ----------------------

# num = list(map(float, input().split(" ")))
# print(num)

# n = input()
# n = n.split(" ")
# a = float(n[0])
# b = float(n[1])
# print(a, type(a))
# if a > b:
#     print(a)
# else:
#     print(b)

# ----------------------

# print(list(map(int, "123123131321")))

# ----------------------

# your_lambda = lambda x: x * str(x)

# map_result = map(your_lambda, [1, 2, 3])
# numbers = list(map_result)
# print(numbers)

# ----------------------

# n = [i for i in range(10) if i % 2 == 0]
# n = [i for i in range(10)]

# n = [-i for i in range(10, 0, -1)]
# print(n)

# ----------------------

# print({str(el): el for el in [i for i in range(10, 0, -1)]})  # {'10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}

# ----------------------

# string = "Element"
# print(string[4])
# print(string[0::2]) #Eeet
# print(string[::-1])  # tnemelE #полиндром
# print("okko"[::-1] == "okko") #True

# ----------------------


# class Car:
#     def __init__(self, color, engine):
#         self.color = color
#         self.engine = engine
#         self.engine_started = False

#     def start_engine(self):
#         print("Engine started!")
#         self.engine_started = True

#     def __str__(self):
#         return f"Car {self.color}, {self.engine}"


# gentra = Car("black", 1.5)
# print(gentra) # Car black, 1.5
# print(gentra.color) # black
# print(gentra.engine * 2) #3.0
# gentra.start_engine()
# print(gentra.engine_started)


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

    def __str__(self):
        return f"Beer {self.color} {self.alco} {self.price}"


guinness = Beer("dark", 5, "75 000")
print(guinness)
print("price", guinness.price)
print("alco ", guinness.alco, "%")
guinness.is_available()
