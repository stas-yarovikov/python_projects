import random


lst = [] # Список слов для случайной выборки
mstk = None # Счётчик ошибок
# Переменные для построения виселицы
part_1 = ""
part_2 = ""
part_3 = ""
part_4 = ""
part_5 = ""
part_6 = ""
random_word = "" #Случайное слово из списка
player_word = "" #Слово для отгадывания (с измененими, по мере отгадывания игроком)


def get_hangman(m):
    """ Функция по отображению текущего состояния виселицы """
    global part_1, part_2, part_3, part_4, part_5, part_6
    mstk = m
    if mstk == 1:
        part_3 = '|    ()   '
    elif mstk == 2:
        part_4 = '|    |    '
    elif mstk == 3:
        part_4 = '|   /|    '
    elif mstk == 4:
        part_4 = '|   /|\   '
    elif mstk == 5:
        part_5 = '|    /    '
    elif mstk == 6:
        part_5 = '|    /\   '

    print("\nТекущее состояние виселицы:")
    print(part_1)
    print(part_2)
    print(part_3)
    print(part_4)
    print(part_5)
    print(part_6)


def get_word(word1, word2, letter):
    global mstk
    """ Функция по поиску введенной буквы в слове """

    word1 = list(word1)
    word2 = list(word2)
    if letter in word1 or letter.upper() == word1[0]:
        for i, x in enumerate(word1):
            if letter == x:
                word2[i] = x
    else:
        mstk += 1
    word = ''
    for x in word2:
        word += x

    return word, mstk


def main_app():
    global lst, mstk, random_word, player_word, part_1, part_2, part_3, part_4, part_5, part_6
    """ Основная функция приложения """

    # Задаем начальное значение виселицы
    part_1 = '______    '
    part_2 = '|    |    '
    part_3 = '|         '
    part_4 = '|         '
    part_5 = '|         '
    part_6 = '__________'

    # Работаем с файлом и получаем список слов
    try:
        with open("D:/Python_Projects_Learning/dictionary.txt", encoding="utf-8") as file:
            lst = file.readlines()
    except FileNotFoundError:
        print("Файл не найден. Невозможно открыть файл")
    except:
        print("Ошибка при работе с файлом")

    # Изменяем список (убираем номер слова и слишком короткие слова, длиной менее 6 символов)
    lst = [x.strip().split() for x in lst]
    lst = [x[1] for x in lst if len(x[1]) > 5]

    # Задаем случайное слово из списка и слово, которое видит игрок
    random_word = random.choice(lst)
    player_word = random_word[0] + ('_' * (len(random_word) - 2)) + random_word[-1]

    # Обнуляем счётчик ошибок
    mstk = 0
    print(f'Текущее слово: {player_word}')

    while mstk < 6:
        letter = input('Введите ОДНУ букву: ').lower()
        player_word, mstk = get_word(random_word, player_word, letter)
        get_hangman(mstk)

        if mstk < 6:
            print(f'Текущее слово: {player_word}, кол-во ошибок: {mstk}')
        else:
            print(f'Кол-во ошибок: {mstk}')
            #print(f'Случайным словом было: {random_word}')
            print('Поражение. Игра окончена\n')

        if random_word == player_word:
            print(f'Загаданное слово: {random_word}')
            print('Победа! Игра окончена\n')
            break

    #mstk = 0


if __name__ == '__main__':
    command = ""
    while command != 0:
        print("Нажмите 1, чтобы начать новую игру")
        print("Нажмите 0, чтобы выйти из приложения")
        command = int(input("Выберите номер команды из списка: "))

        if command == 1:
            main_app()  # Запуск основной функции программы