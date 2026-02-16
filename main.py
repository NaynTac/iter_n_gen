from functools import wraps


class FibonacciLst():
    """
    Итератор возвращающий числа из списка instance, принадлежащие ряду Фибоначчи
    Основан на методах __iter__() и __next__()
    """
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                res = self.instance[self.idx]

            except IndexError:
                raise StopIteration

            # Генерируем пару последних значений ряда Фибоначчи    
            pair = [0, 1]

            while sum(pair) <= res:
                pair = pair[::-1]
                pair[1] = sum(pair)

            # Возвращаем нужный элемент
            if res in pair:
                self.idx += 1
                return res

            self.idx += 1


class FibonacciLstGetitem():
    """
    Итератор возвращающий числа из списка instance, принадлежащие ряду Фибоначчи
    Основан на методе __getitem__()
    """
    def __init__(self, instance):
        # Создаем результирующий спиок
        self.data = list()
        
        # Генерируем ряд Фибоначчи (до минимального необходимого значения)
        fib_list = [0, 1]
        if instance:
            while fib_list[-1] <= max(instance):
                fib_list.append(sum(fib_list[-2:]))

            # Выбираем подходящие значения
            self.data = [x for x in instance if x in fib_list]

    def __getitem__(self, index):
        # Проверка значения индекса
        if 0 > index <= len(self.data):
            raise IndexError

        # Возвращение элемента
        return self.data[index]


def fibonacci_generator():
    """Генератор чисел Фибоначчи"""
    pair = [0, 1]
    while True:
        yield pair[0]
        pair = pair[::-1]
        pair[1] = sum(pair)


def my_coro():
    """Корутина (сопрограмма)"""
    while True:
        number_of_fib_elem = yield
        fib_list = [0, 1]

        if number_of_fib_elem >= 3:
            for _ in range(number_of_fib_elem - 2):
                fib_list.append(sum(fib_list[-2:]))

        else:
            fib_list = fib_list[:number_of_fib_elem]

        yield fib_list


def fib_coroutine(g):
    @wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


if __name__ == "__main__":
    coro = fib_coroutine(my_coro)
    gen = coro()
    print(gen.send(-1))