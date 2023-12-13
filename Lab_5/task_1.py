from typing import Union

class Notebook:
    def __init__(self, pages: int, thickness: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Блокнот"
        :param pages: Количество страниц
        :param thickness: Толщина блокнота в см
        Примеры:
        >>> notebook = Notebook(96, 1)  # инициализация экземпляра класса
        """
        self.pages = None
        self.init_pages(pages)

        self.thickness = None
        self.init_thickness(thickness)

    def read_notebook(self, number: int) -> None:
        """
        Чтение страниц в блокноте.
        :param number: Прочитанные страницы
        :raise ValueError: Если количество прочитанных страниц превышает общее количество страниц, то вызываем ошибку
        Примеры:
        >>> note = Notebook(96, 1)
        >>> note.read_notebook(100)
        """
        if not isinstance(number, int):
            raise TypeError("Количество страниц должно быть типа int")
        if number < 0:
            raise ValueError("Прочитанные страницы должны быть положительным числом")
        ...

    def delete_pages(self, number_minus: Union[int, float]) -> None:
        """
        Вырывание страниц из блокнота.
        :param number_minus: Количество вырванных страниц
        :raise ValueError: Если количество вырванных страниц превышает количество страниц,
        то возвращается ошибка.
        :return: Количество действительно вырванных страниц
        Примеры:
        >>> note = Notebook(96, 1)
        >>> note.delete_pages(40)
        """
        ...

    def init_pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def init_thickness(self, thickness: Union[int, float]):
        if not isinstance(thickness, (int, float)):
            raise TypeError("Толщина должна быть int или float")
        if thickness <= 0:
            raise ValueError("Толщина должна быть не может быть отрицательным числом или равным нулю")
        self.thickness = thickness

class Table:
    def __init__(self, high: Union[int, float], number: int):
        """
        Создание и подготовка к работе объекта "Стол"
        :param high: Высота стола в мм
        :param number: Количество столов в магазине
        Примеры:
        >>> table = Table(1000, 5)  # инициализация экземпляра класса
        """
        self.high = None
        self.init_high(high)

        self.number = None
        self.init_number(number)

    def buy_table(self, number_sale: Union[int, float]) -> None:
        """
        Покупка столов.
        :param number_sale: Купленные столы
        :raise ValueError: Если количество купленных столов превышает общее количество столов в магазине, то вызываем ошибку
        Примеры:
        >>> buy = Table(1000, 5)
        >>> buy.buy_table(100)
        """
        if not isinstance(number_sale, (int, float)):
            raise TypeError("Количество столов должно быть типа int или float")
        if number_sale < 0:
            raise ValueError("Количество столов должно быть положительным числом")
        ...

    def is_zero_hight(self) -> bool:
        """
        Функция которая проверяет является ли высота нулевой
        :return: Является ли высота нулевой
        Примеры:
        >>> zero = Table(1000, 5)
        >>> zero.is_zero_hight()
        """
        ...

    def init_high(self, high: Union[int, float]):
        if not isinstance(high, (int,float)):
            raise TypeError("Высота должна быть типа int или float")
        if high <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.high = high

    def init_number(self, number: int):
        if not isinstance(number, int):
            raise TypeError("Количество должно быть int")
        if number < 0:
            raise ValueError("Количество не может быть отрицательным числом")
        self.number = number


class Mug:
    def __init__(self, metal_volume: Union[int, float], water_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Кружка"
        :param metal_volume: Объем основы
        :param water_volume: Объем жидкости
        Примеры:
        >>> mug = Mug(5, 4)  # инициализация экземпляра класса
        """
        self.metal_volume = None
        self.init_metal_volume(metal_volume)

        self.water_volume = None
        self.init_water_volume(water_volume)

    def is_empty_mug(self) -> bool:
        """
        Функция которая проверяет является ли чашка пустой
        :return: Является ли чашка пустой
        Примеры:
        >>> mug = Mug (10, 5)
        >>> mug.is_empty_mug(4)
        """
        ...

    def add_tea_to_mug(self, tea: float) -> None:
        """
        Добавление чая в кружку.
        :param tea: Объем добавляемой жидкости
        :raise ValueError: Если количество чая превышает свободное место в кружке, то вызываем ошибку
        Примеры:
        >>> mug = Mug(5, 4)
        >>> mug.add_tea_to_mug(200)
        """
        if not isinstance(tea, (int, float)):
            raise TypeError("Чай должен быть типа int или float")
        if tea < 0:
            raise ValueError("Чай должен быть положительным числом")
        ...

    def init_metal_volume(self, metal_volume: Union[int, float]):
        if not isinstance(metal_volume, (int, float)):
            raise TypeError("Объем основы должен быть типа int или float")
        if metal_volume < 0:
            raise ValueError("Объем основы должен быть положительным числом")
        self.metal_volume = metal_volume

    def init_water_volume(self, water_volume: Union[int, float]):
        if not isinstance(water_volume, (int, float)):
            raise TypeError("Объем жидкости должен быть типа int или float")
        if water_volume < 0:
            raise ValueError("Объем жидкости должен быть положительным числом")
        self.water_volume = water_volume


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass