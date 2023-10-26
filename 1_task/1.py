# Задание 1:
# Класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первый метод: создайте переменную и выведите её.
# Второй метод: верните сумму 2-ух глобальных переменных.
# Третий метод: верните результат возведения первой динамической
# переменной во вторую динамическую переменную.
# Создайте объект класса. Напечатайте оба метода. Напечатайте переменную a.
def isint(s):
    try:
        int(s)
        return True
    except(ValueError, TypeError):
        return False


class Example:
    pem = 4
    pam = 10

    def __init__(self, dm1, dm2):
        self.dm1 = dm1
        self.dm2 = dm2

    @staticmethod
    def method_1():
        #a = input("Переменная a = ")
        a = 5
        return f"Переменная a = {a}"

    def method_2(self):
        return f"Сумма : {self.pem + self.pam}"

    def method_3(self):
        return f"Возведение в степень: {self.dm1**self.dm2}"


def main():
    dinam_1 = input("dinam1 = ")
    dinam_2 = input("dinam2 = ")
    if isint(dinam_1) and isint(dinam_2):
        dinam_1 = int(dinam_1)
        dinam_2 = int(dinam_2)
        Obj = Example(dinam_1, dinam_2)
        print(Obj.method_2())
        print(Obj.method_3())
        print(Obj.method_1())
    else:
        print("Некоректный ввод")
        main()


if __name__ == "__main__":
    main()
