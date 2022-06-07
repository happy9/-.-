from ЛУКАШОВ_ЗБПИ211с import *

def test_fact():
    print("Задача 1.")
    list_test = [3, 2, 7, 8, 6, 9]
    for item in list_test:
        print("Факториал", item, "равен:", fact(item))

def test_filter_even():
    print("\nЗадача 2.")
    list_test = [[1, 2, 3, -4, 5, 6], [4, 3, -6, 12, 6, 9], [1, 2, 3, 3, 7, 8], [0, 0, 0, 0, 0, 0], [-2, 11, 53, 73, 252, 6334], [11, 14124, -1234, 5245, 242, 234]]
    for item in list_test:
        print("Список:", item, "Только четные:", filter_even(item))

def test_square():
    print("\nЗадача 3.")
    list_test = [[1, 2, 3, -4, 5, 6], [4, 3, -6, 12, 6, 9], [1, 2, 3, 3, 7, 8], [0, 0, 0, 0, 0, 0], [-2, 11, 53, 73, 252, 6334], [11, 14124, -1234, 5245, 242, 234]]
    for item in list_test:
        print("Квадрат", item, "равен:", square(item))

def test_bin_search():
    print("\nЗадача 4.")
    list_test = [[[2, 3, 6, 14, 20, 26, 45], 3], [[15, 34, 43, 56, 57, 78, 234], 234], [[0, 24, 345, 466, 565, 655, 765], 0], [[-10, -5, -1, 0, 2, 34, 56], -1], [[24, 34, 35, 56, 67, 97, 100], 100], [[0, 1, 2, 3, 4, 5, 6], 10]]

    for item in list_test:
        print("Список:", item[0], "Искомое значение:", item[1], "Индекс:", bin_search(item[0], item[1]))

def test_is_palindrome():
    print("\nЗадача 5.")
    list_test = ["А роза упала на лапу Азора", "Madam, I'm Adam", "MAM", "MMA", "M!A!M!", "M   A    M"]
    for item in list_test:
        print("Предложение:", item, "Полиндром -", is_palindrome(item))

def test_calculate():
    print("\nЗадача 6.")
    print(calculate("test_input_file_1.txt"))

def test_substring_slice():
    print("\nЗадача 7.")
    print(substring_slice("test_import_file_2_11.txt", "test_import_file_2_22.txt"))

def test_decode_ch():
    print("\nЗадача 8.")
    print(decode_ch("NOTiFICaTiON"))

def test_Student():
    print("\nЗадача 9.")
    student1 = Student("Кирилл", "Лукашов")
    student2 = Student("Иван", "Петров")
    print(student1.greeting())
    print("Средняя оценка:", student1.mean_grade())
    print("Отличник:", student1.is_otlichnik())
    student1 + student2

def test_MyError():
    print("\nЗадача 10.")
    raise MyError('Ошибка 404')


test_fact()
test_filter_even()
test_square()
test_bin_search()
test_is_palindrome()
test_calculate()
test_substring_slice()
test_decode_ch()
test_Student()
test_MyError()