# Базовый класс Worker (работник).
# 1. Определить атрибуты: name, surname, position (должность), income
# (доход);
# 2. Последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus":
# bonus};
# 3. Создать класс Position (должность) на базе класса Worker;
# 4. В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# 5. Проверить работу примера на реальных данных: создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать
# методы экземпляров. – 3 балла
def isfloat(s):
    try:
        float(s)
        return True
    except(ValueError, TypeError):
        return False


def inic_dict():
    test_dict = {}
    while True:
        wage = input("Введите зарплату сотрудника: ")
        if isfloat(wage):
            if float(wage) >= 0:
                wage = float(wage)
                while True:
                    bonus = input("Введите премию сотрудника: ")
                    if isfloat(bonus):
                        if float(bonus) >= 0:
                            bonus = float(bonus)
                            test_dict["wage"] = wage
                            test_dict["bonus"] = bonus
                            return test_dict
                        else:
                            print("Введите положительное число")
                    else:
                        print("Некорректный ввод данных")
            else:
                print("Введите положительное число")
        else:
            print("Некорректный ввод данных")


class Worker:
    def __init__(self, *args):
        self.name = args[0]
        self.surname = args[1]
        self.position = args[2]
        self._income = args[3]

    def __del__(self):
        pass

    @property
    def income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        return f'\nПолное имя сотрудника: {self.name + " " +self.surname}\nДолжность: {self.position}'

    def get_total_income(self):
        return f'Доход сотрудника с учетом премии: {self._income["wage"] + self._income["bonus"]}'


name = input("Введите имя сотрудника: ")
surname = input("Введите фамилию сотрудника: ")
position = input("Введите должность сотруднкиа: ")
test_dict = inic_dict()
obj = Position(name, surname, position, test_dict)
print(obj.get_full_name())
print(obj.get_total_income())
print(f"\nПроверка значения атрибутов:\nАтрибут name: {obj.name}\nАтрибут surname: {obj.surname}"
      f"\nАтрибут position: {obj.position}\nАтрибут _income: {obj.income}")
del obj
