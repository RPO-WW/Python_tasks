from random import randint

# Генерируем случайный массив по убыванию
my_list = sorted([randint(1, 1000) for _ in range(100)], reverse=True)
print("Массив (первые 10 элементов):", my_list[:10])
print(f"Диапазон значений: от {min(my_list)} до {max(my_list)}")
print(f"Длина массива: {len(my_list)}")

a = int(input("Введите число a: "))

try:
    index = my_list.index(a)
    print(f"Число {a} найдено на позиции: {index}")
    print(f"Элементы вокруг: ...{my_list[max(0, index-2):index+3]}...")
except ValueError:
    print(f"Числа {a} нет в списке")
    # Показываем ближайшие значения
    greater_than_a = [x for x in my_list if x > a]
    less_than_a = [x for x in my_list if x < a]
    
    if greater_than_a:
        print(f"Ближайшее большее число: {greater_than_a[-1]}")
    if less_than_a:
        print(f"Ближайшее меньшее число: {less_than_a[0]}")