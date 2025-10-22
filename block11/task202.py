def find_all_adjacent_pairs(arr):
    pairs = []
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            pairs.append((i, i + 1))
    return pairs

# Пример использования:
arr = [1, 2, 2, 3, 4, 4, 5]
pairs = find_all_adjacent_pairs(arr)
if pairs:
    for first_index, second_index in pairs:
        print(f"Пара на позициях {first_index} и {second_index}: {arr[first_index]}")
else:
    print("Одинаковых соседних элементов не найдено")