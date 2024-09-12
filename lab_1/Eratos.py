import numpy


def sieve_of_eratosthenes(n):
    # Создаем массив от 2 до n, инициализируем True
    is_prime = numpy.ones(n + 1, dtype=bool)
    is_prime[0:2] = False  # 0 и 1 не являются простыми числами

    # Проходим по всем числам от 2 до n
    for i in range(2, n + 1):
        if is_prime[i]:
            # зануляем кратные числа
            is_prime[i * 2:n + 1:i] = False

    # Возвращаем массив простых чисел (индексы, где True)
    return numpy.nonzero(is_prime)[0]

# Пример использования
n = 30
print(sieve_of_eratosthenes(n))
