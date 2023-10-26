# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические, методы, методы класса
def isfloat(s):
    try:
        float(s)
        return True
    except(ValueError, TypeError):
        return False


def isint(s):
    try:
        int(s)
        return True
    except(ValueError, TypeError):
        return False


class Deposit:
    __massive_users = []

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.__arrears = 0
        test_users = [self.name, self.balance, self.__arrears]
        self.__massive_users.append(test_users)

    def add_user(self, name, balance):
        for el in self.__massive_users:
            if el[0] == name:
                return "Данный пользователь уже существует"
        self.name = name
        self.balance = balance
        self.__arrears = 0
        test_users = [self.name, self.balance, self.__arrears]
        self.__massive_users.append(test_users)

    def __del__(self):
        pass

    def set_arrears(self, name, money):
        for el in self.__massive_users:
            if el[0] == name:
                el[2] = money
                return "Задолжность была установлена"
        return "Пользователь был не найден"

    def stats_users(self):
        for el in self.__massive_users:
            print(f"\nПользователь: {el[0]}\nБаланс: {el[1]}\nЗадолжность: {el[2]}")

    def add_balance(self, name, money):
        for el in self.__massive_users:
            if el[0] == name:
                el[1] = el[1] + money
                return "Баланс был пополнен"
        return "Пользователь не найден"

    def arriears_dep(self, name, money):
        for el in self.__massive_users:
            if el[0] == name and el[1] >= money:
                if el[2] > money:
                    el[2] = el[2] - money
                    el[1] = el[1] - money
                    return "Операция прошла успешно"
                else:
                    el[1] = el[1] - money
                    el[2] = 0
                    return "Операция прошла успешно"
        return "Пользователь был не найден или на счету недостаточно денег "


def main():
    name = input("Введите имя пользователя: ")
    while True:
        balance = input("Баланс пользователя: ")
        if isfloat(balance):
            if float(balance) > 0:
                balance = float(balance)
                obj = Deposit(name, balance)
                menu(obj)
            else:
                print("Введите положительное значение")
        else:
            print("Неверный тип данных")


def menu(object):
    print("\n1. Добавить нового пользователя\n2. Установить задолженность пользователю\n3. Пополнить балланс\n"
          "4. Выплатить задолженность(можно только с личного счета)\n5. Вывести статистику пользователей)\n6. Выход")
    choice = input("Enter: ")
    if isint(choice):
        if 6 >= int(choice) > 0:
            choice = int(choice)
            if choice == 1:
                name = input("\nВведите имя пользователя: ")
                while True:
                    balance = input("Баланс пользователя: ")
                    if isfloat(balance):
                        if float(balance) > 0:
                            balance = float(balance)
                            print(object.add_user(name, balance))
                            menu(object)
                        else:
                            print("Введите положительное значение")
                    else:
                        print("Неверный тип данных")
            if choice == 2:
                name = input("\nВведите имя пользователя: ")
                while True:
                    balance = input("Введите сумму задолженности: ")
                    if isfloat(balance):
                        if float(balance) > 0:
                            balance = float(balance)
                            print(object.set_arrears(name, balance))
                            menu(object)
                        else:
                            print("Введите положительное значение")
                    else:
                        print("Неверный тип данных")
            if choice == 3:
                name = input("\nВведите имя пользователя: ")
                while True:
                    balance = input("Введите сумму пополнения: ")
                    if isfloat(balance):
                        if float(balance) > 0:
                            balance = float(balance)
                            print(object.add_balance(name, balance))
                            menu(object)
                        else:
                            print("Введите положительное значение")
                    else:
                        print("Неверный тип данных")
            if choice == 4:
                name = input("\nВведите имя пользователя: ")
                while True:
                    balance = input("Введите сумму для выплаты задолженности: ")
                    if isfloat(balance):
                        if float(balance) > 0:
                            balance = float(balance)
                            print(object.arriears_dep(name, balance))
                            menu(object)
                        else:
                            print("Введите положительное значение")
                    else:
                        print("Неверный тип данных")
            if choice == 5:
                object.stats_users()
                menu(object)
            if choice == 6:
                del object
                exit()
        else:
            print("Введите число от 1 до 6")
            menu(object)
    else:
        print("Неверный тип данных")
        menu(object)


if __name__ == "__main__":
    main()
