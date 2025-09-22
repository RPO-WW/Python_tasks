def print_elements_after_n(arr, n):
    # Проверяем, есть ли элементы больше n
    found = False
    for i in range(len(arr)):
        if arr[i] > n:
            found = True

            for j in range(i, len(arr)):
                print(arr[j], end=' ')
            print()
            break

    if not found:
        print("В массиве нет элементов, больших", n)


arr = [1, 3, 5, 7, 9, 11]
n = 6
print_elements_after_n(arr, n)
