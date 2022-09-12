numbers = [31, 1006, 26, 508, 28, 401, 205, 696, 5, 1, 0] #массив чисел

def bubble_sort(numbers): #функция сортировки массива
    count = len(numbers) # len - функция которая считает количество элементов в массиве
    indexes = range(count) # range - функция создает массив от 0 до count [0, 1, 2, 3, ...., count - 1]

    while True: # while команда для определения бесконечного цикла после идет условие
        has_rearrange = False
        for index in indexes: #for in - команды для определения цикла, между for и in переменная в которую складывается значение из массива по порядку после команды i
            if (index + 1 == count):
                break # команда для выхода из цикла
            if numbers[index] > numbers[index + 1]:
                has_rearrange = True
                box = numbers[index]
                numbers[index] = numbers[index + 1]
                numbers[index + 1] = box
        if not has_rearrange:
             break

    return numbers

result = bubble_sort(numbers)

print(result)