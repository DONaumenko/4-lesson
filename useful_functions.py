# filter, sorted, map

# Функция filter
# Хотим выбрать из этого списка элементы, начинающиеся на букву m
# Обычный вариант
friends = ['max', 'kate', 'man', 'leo']

result = []
for friend in friends:
    if friend.startswith('m'):
        result.append(friend)

print(result)


# Вариант через функцию filter
# Пишем функцию f, которая будет параметром для функции filter
def f(x):
    if x.startswith('m'):
        return True
    else:
        return False

# Функция filter принимает два параметра - функцию (она применяется к каждому
# элементу последовательнсоти и должна возвращать True или False) и список (последовательность)
result = filter(f, friends)
print(list(result))


# Функция map
# Хотим сделать всех друзей большими буквами
# Обычный вариант
friends = ['max', 'kate', 'man', 'leo']
result = []
for friend in friends:
    result.append(friend.upper())

print('')
print(result)


# Вариант через функцию map
# Функция map принимает два параметра - функцию (которая выполняет
# какое-то действие над каждым элементом) и последовательность элементов
# параметр x здесь - это один элемент последовательности
def f(x):
    return x.upper()

# map
print(list(map(f, friends)))
print('')


# По аналогии можно привести первую букву к большой
def t(x):
    return x.title()

# map
print(list(map(t, friends)))
print('')


# Функция sorted
# Простая сортировка
print(sorted(friends))
print('')


# Сортировка списка нужным для нас образом с помощью функции, которую передаем вторым параметром.
# Сортировка будет идти по тому, что возвращает функция - в данном случае по последней букве слова
# key мы прописываем в любом случае и ему присваиваем название функции, либо лямбда функцию (см. ниже)
def f(x):
    return x[-1]

print(sorted(friends, key=f, reverse=True))
print('')
print('')


# lambda функции
# def f(x):
#     if x.startswith('m'):
#         return True
#     else:
#         return False

result = filter(lambda x: True if x.startswith('m') else False, friends)


# map
print(list(map(lambda x: x.title(), friends)))
print('')
print(list(map(lambda x: x.upper(), friends)))
print('')
def f(x):
    return x[-1]


print(sorted(friends, key=lambda x: x[-1]))
print('')

# Пример с другими именами

friends = ['anna', 'banana', 'max']

# по 1-ой букве
print(sorted(friends))
print('')

# сортировка по 1-ой букве и наоборот
print(sorted(friends, reverse=True))
print('')

# сортировка по последней букве
print(sorted(friends, key=lambda x: x[-1]))