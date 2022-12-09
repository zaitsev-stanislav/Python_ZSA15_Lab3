#!/usr/bin/env python3
# coding=utf-8

# Имеется двумерный массив 4x5. Реализовать возможность заполнения его
# случайными числами. Реализовать команду выполнить задание, которая выполняет:
#Если все элементы второго столбца равны 1, то заменить максимальный элемент таблицы на 100, а
#минимальный элемент на 5


import random  # импортируем модуль random для генерации случайных чисел


# Функция генерирует nxm массив случайных чисел до max_value, у которого
# стандартное значение 20
def random_array(n, m, max_value=20):
    array = []  # инициализируем массив
    # Цикл for. Оператор range выдает диапазон чисел, в данном случае
    # от 0 до n-1
    for i in range(0, n):
        sub_array = []  # инициализируем подмассив
        # Если передать range один аргумент, то нижняя граница 0, в данном
        # случае диапазон чисел будет от 0 до m-1
        for j in range(m):
            # Генерируем слуйчаное число от 0 до 19 и добавляем его в подмассив
            number = random.randint(0, max_value)
            sub_array.append(number)
        # Добавляем полученный подмассив в основной массив
        array.append(sub_array)
    return array  # возвращаем массив из случайных чисел


def print_array(array):  # функция выводит массив в удобочитаемой форме
    print()  # переход на новую строку
    # Циклу for также можно давать массивы, тогда перебирается каждый элемент
    for i in array:
        # Так как массив состоит из подмассивов, тогда каждый элемент тоже
        # можно перебрать используя цикл for
        for j in i:
            print("%d\t" % j, end='')  # выводим каждое значение и табуляцию
        print()  # переход на новую строку

def main():
    array = random_array(4, 5)  # заполняем массив случайными числами




    print_array(array)  # выводим массив на экран
    try:
        while True:
            key = int(input('Пересоздать массив? (1 - ДА/ 2 - Нет): '))
            if key == 1:
                array = random_array(4, 5)
                print_array(array)
            elif key == 2:
                if 1:
                    for i in range(0, 4):
                        array[i][1] = 1


                max = array[0][0]
                max_cors = [0, 0]
                min = array[0][0]
                min_cors = [0, 0]

                for i in range(0, 4):
                    for j in range(0, 5):
                        if (array[i][j] > max):  # max elem
                            max = array[i][j]
                            max_cors[0] = i
                            max_cors[1] = j

                        if (array[i][j] < min):  # min elem
                            min = array[i][j]
                            min_cors[0] = i
                            min_cors[1] = j

                uslovie = False

                for i in range(0, 4):  # проверка условия
                    if (array[i][1] == 1):
                        uslovie = True
                    else:
                        uslovie = False

                if (uslovie):
                    print("Условие выполнено")
                    array[max_cors[0]][max_cors[1]] = 100
                    array[min_cors[0]][min_cors[1]] = 5

                print_array(array)

            else:
                exit()
    except:
        print("ОШИБКА! Я ПОНИМАЮ ТОЛЬКО ЦИФРЫ")

if __name__ == '__main__':
    main()