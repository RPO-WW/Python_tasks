def process_array_optimized(arr, a):
    # Проверка упорядоченности
    if not all(arr[i] >= arr[i+1] for i in range(len(arr)-1)):
        print("Ошибка: массив не упорядочен по убыванию!")
        return
    
    # Бинарный поиск первого элемента < a
    left, right = 0, len(arr) - 1
    first_smaller_index = None
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < a:
            first_smaller_index = mid
            right = mid - 1  # Ищем первое вхождение
        else:
            left = mid + 1
    
    if first_smaller_index is None:
        print("В массиве нет элементов, меньших заданного числа a.")
        return
    
    following_elements = arr[first_smaller_index + 1:]
    greater_than_a = arr[:first_smaller_index]  # Более эффективно
    
    print(f"Первое число, меньшее {a}: {arr[first_smaller_index]} (индекс {first_smaller_index})")
    print("Элементы, следующие за ним:", following_elements)
    print("Все элементы, большие a:", greater_than_a)