# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

a = 5   	                    					# int
b = 12.4     					                    # float
c = 'привет'					                    # str
d = True					                        # bool
e = [a, b, c, d]				                    # list
f = (a, b, c, d)				                    # tuple
g = {'int': a, 'float': b, 'str': c, 'bool': d}     # dict

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))

h = input('Введите какое-нибудь значение: ')

print('Вы ввели: ', h, type(h))
