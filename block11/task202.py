def find_adjacent_pairs(arr):
    if len(arr) < 2:
        return False, None, None

    for i in range(len(arr) - 1):

        if arr[i] == arr[i + 1]:
            return True, i, i + 1

    return False, None, None


def main():
    arr = [1, 2, 2, 3, 4, 4, 5]

    found, first_index, second_index = find_adjacent_pairs(arr)

    if found:
        print(f"Найдена пара одинаковых соседних элементов на позициях {first_index} и {second_index}: {arr[first_index]}, {arr[second_index]}")
    else:
        print("Одинаковых соседних элементов не найдено")


if __name__ == "__main__":
    main()
