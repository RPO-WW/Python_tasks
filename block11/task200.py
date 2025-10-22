from random import randint

# Генерируем случайный массив
arr = sorted([randint(1, 1000) for i in range(100)])

def print_elements_after_n(arr, n):
    for i, num in enumerate(arr):
        if num > n:
            result = arr[i+1:]
            if result:
                print(f"Элементы, следующие за первым элементом > {n}: {result}")
                print(f"Количество элементов: {len(result)}")
                print(f"Первый элемент > {n}: {num} (индекс {i})")
            else:
                print(f"После первого элемента > {n} нет следующих элементов")
            return

    print(f"В массиве нет элементов, больших {n}")

# Тестирование
print("Весь массив:", arr)
print(f"Минимальный элемент: {min(arr)}")
print(f"Максимальный элемент: {max(arr)}")
print("-" * 50)

print_elements_after_n(arr, 500)
print("-" * 50)
print_elements_after_n(arr, 900)
print("-" * 50)
print_elements_after_n(arr, 1000)