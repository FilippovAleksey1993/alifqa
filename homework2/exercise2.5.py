# На вход программе подаются три целых числа, записанных в одну строку через пробел.
# Необходимо прочитать их и определить наименьшее среди прочитанных чисел. Наименьшее найденное значение вывести на экран.
# P.S. Программу реализовать следует, используя условный оператор, без использования функции min.

# astr, bstr, cstr = input().split()
# a = int(astr)
# b = int(bstr)
# c = int(cstr)
# if a <= b and a <= c:
#     print(a)
# elif b <= c and b <= a:
#     print(b)
# else:
#     print(c)

# ----------------------

num = input().split()
a, b, c = int(num[0]), int(num[1]), int(num[2])
if a <= b and a <= c:
    print(a)
elif b <= c and b <= a:
    print(b)
else:
    print(c)
