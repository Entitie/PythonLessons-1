# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

a = input('Введите ваше имя: ')
b = input('Введите вашу фамилию: ')
c = int(input('Введите ваш возраст: '))
d = int(input('Введите ваш вес: '))

if d < 50 or d > 120:
	if c > 40:
		print(a, b, ',', 'возраст', c, ', вес', d, '- следует обратится к врачу!')
	elif c > 30:
		print(a, b, ',', 'возраст', c, ', вес', d, '- следует заняться собой')
	else:
		print(a, b, ',', 'возраст', c, ', вес', d, '- вы какой-то нестандартный')
elif c <30:
	print(a, ' ', b, ', ', 'возраст ', c, ', вес ', d, ' - хорошее состояние')
else:
	print(a, b, ',', 'возраст', c, ', вес', d, '- вы какой-то нестандартный в целом')
