def find_adjacent_pairs(arr):
    # Проверяем, есть ли в массиве хотя бы 2 элемента
    if len(arr) < 2:
        return False, None, None
    
    # Проходим по массиву до предпоследнего элемента
    for i in range(len(arr) - 1):
        # Если текущий элемент равен следующему
        if arr[i] == arr[i + 1]:
            return True, i, i + 1
    
    # Если пара не найдена
    return False, None, None

# Пример использования
def main():
    # Пример массива
    arr = [1, 2, 2, 3, 4, 4, 5]
    
    # Вызываем функцию
    found, first_index, second_index = find_adjacent_pairs(arr)
    
    # Выводим результат
    if found:
        print(f"Найдена пара одинаковых соседних элементов на позициях {first_index} и {second_index}: {arr[first_index]}, {arr[second_index]}")
    else:
        print("Одинаковых соседних элементов не найдено")

if __name__ == "__main__":
    main()
