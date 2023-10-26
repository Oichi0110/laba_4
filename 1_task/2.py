# Класс House
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него два динамических
# свойства: _area и _price. Свои начальные значения они получают из
# параметров метода __init__()
# 3. Создайте метод final_price(), который принимает в качестве параметра
# размер скидки и возвращает цену с учетом данной скидки.
# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он
# создавал объект с площадью 40м2
# Класс Human
# 1. Реализуйте приватный метод make_deal(), который будет отвечать за
# техническую реализацию покупки дома: уменьшать количество денег на
# счету и присваивать ссылку на только что купленный дом. В качестве
# аргументов данный метод принимает объект дома и его цену.
# 2. Реализуйте метод buy_house(), который будет проверять, что у человека
# достаточно денег для покупки, и совершать сделку. Если денег слишком
# мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка
# на дом и размер скидки
def isfloat(s):
    try:
        float(s)
        return True
    except(ValueError, TypeError):
        return False


class House:
    def __init__(self,  area, price):
        self._area = area
        self._price = price

    def final_price(self, prec):
        print(f"\nЦена с учетом скидки: {self._price - (self._price * prec) / 100}")
        return self._price - (self._price * prec) / 100

    def __del__(self):
        pass


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)

    def __del__(self):
        pass


class Human:
    def __init__(self, dep):
        self.dep = dep

    def __del__(self):
        pass

    def __make_deal(self, obj_house, price_house):
        self.dep = self.dep - price_house
        self.obj_house_ref = obj_house

    def buy_house(self, obj_house, precent):
        price = obj_house.final_price(precent)
        if self.dep < price:
            return "Недостаточно денег на счету"
        self.__make_deal(obj_house, price)
        return f"\nДом успешно куплен\nНынешний счет пользователя: {self.dep}" \
               f"\nСсылка на объект дома: {self.obj_house_ref}"


def main():
    while True:
        price_house = input("Цена дома: ")
        if isfloat(price_house):
            if float(price_house) >= 0:
                price_house = float(price_house)
                obj_house = SmallHouse(price_house)
                while True:
                    deposit = input("Введите счет пользователя: ")
                    if isfloat(deposit):
                        if float(deposit) >= 0:
                            deposit = float(deposit)
                            new_human = Human(deposit)
                            while True:
                                pr = input("Введите скидку: ")
                                if isfloat(pr):
                                    if 100 >= float(pr) >= 0:
                                        pr = float(pr)
                                        print(new_human.buy_house(obj_house, pr))
                                        del new_human
                                        del obj_house
                                        exit(0)
                                    else:
                                        print("Некоректно введена скидка")
                                else:
                                    print("Введите корректную скидку")
                        else:
                            print("Введите положительное число")
                    else:
                        print("Введите корректный счет пользователя")
            else:
                print("Введите положительное число")
        else:
            print("Введите корректную цену дома")


if __name__ == "__main__":
    main()
