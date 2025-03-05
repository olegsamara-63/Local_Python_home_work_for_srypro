import random
import os

# Функция для перемешивания букв в выбранном случайно слове из задания
def shuffle_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

# Проверка существования файла words.txt
if not os.path.exists("words.txt"):
    # файл words.txt на каком либо компьютере скорее всего
    # отсутствует, поэтому создаем его и заполняем словами из задания
    with open("words.txt", "w") as file:
        file.write("python\nsquirrel\nflask\ncucumbers\n")
    print("Файл words.txt создан и заполнен словами.")

# Чтение слов из файла
try:
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
except FileNotFoundError:
    print("Ошибка: файл words.txt не найден.")
    exit()  # Завершаем програму, если файл отсутствует

# Инициализация счета пользователя, того, кто сейчас угадывает слова
score = 0

# Основной цикл программы
for word in words:
    # Перемешивание букв в слове
    shuffled_word = shuffle_word(word)

    # Предложение пользователю угадать слово
    print(f"Угадайте слово: {shuffled_word}")
    user_guess = input("Ваш ответ: ").lower()

    # Проверка ответа пользователя, угадал тогда == word или нет
    if user_guess == word:
        print("Верно! Вы получаете 10 очков.")
        score += 10
    else:
        print(f"Неверно! Правильное слово: {word}")

# Когда все слова заканчиваются , тогда ...вывод сообщения и счёта
print("\nИгра завершена!")
print(f"Ваш итоговый счет: {score}")

# Запрос имени пользователя - что бы знать кому говорить
# счёт и что бы знать как обращаться к пользователю, кто играл
user_name = input("Введите ваше имя для сохранения результата: ").capitalize()

# Запись результата в файл history.txt
with open("history.txt", "a") as history_file:
    history_file.write(f"{user_name} , ваш результат -  {score}\n")

print("Ваш результат сохранен в файл history.txt.")

# Чтение истории результатов для вывода статистики
try:
    with open("history.txt", "r") as history_file:
        lines = history_file.readlines()
except FileNotFoundError:
    # Если файл "history.txt" не существует,
    # а такой файл на компе точно вряд ли кто то создавал раньше,
    # то создаем его и начинаем с пустого списка
    lines = []
    with open("history.txt", "w") as history_file:
        pass  # Создаем пустой файл

# Подсчет общего количества игр и максимального рекорда
total_games = len(lines)
max_score = max(int(line.split()[-1]) for line in lines) if lines else 0

# Вывод статистики - сколько штук игр, и максимально,
# что на-прибавляла прибавлялка из 39-ой строки

print("\nСтатистика игр:")
print(f"Уважаемый {user_name}, Вами сыграно игр всего: {total_games}")
print(f"Максимальный рекорд: {max_score}")
