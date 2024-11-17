import numpy as np
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def game_core_v3(number: int = 1) -> int:
    """Используем бинарный поиск, а потом уменьшаем
    или увеличиваем границы диапазона в зависимости от того, больше середина диапазона или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    low, high = 1, 100

    while low <= high:
        mid = (low + high) // 2
        count += 1

        if mid < number:
            low = mid + 1
        elif mid > number:
            high = mid - 1
        else:
            return count   # Загаданное число угадано!

    # Ваш код заканчивается здесь

    return count
# RUN
if __name__ == '__main__':
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)
