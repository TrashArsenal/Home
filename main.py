# Задача 10: 
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

N = int(input('Введите количество монет '))
orel = reshka = 0
for i in range(N):
@@ -12,4 +17,67 @@ if orel < reshka:
elif orel == reshka:
    print(f'Количество орлов и решек одинаково, по {orel} штук')
else:
    print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))
    print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))