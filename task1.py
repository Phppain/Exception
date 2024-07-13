"""task1.py"""

def access_array_element(arr, index):
    try:
        element = arr[index]
        print(f"Элемент на индексе {index}: {element}")
    except IndexError:
        print(f"Ошибка: индекс {index} выходит за границы массива")


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]

    access_array_element(array, 2)
    access_array_element(array, 10)
    access_array_element(array, -1)
