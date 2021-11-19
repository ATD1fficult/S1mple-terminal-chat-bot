def greet(bot_name, birth_year):
    print(f'Hello! My name is (Привет, меня зовут:) {bot_name}.')
    print(f'I was created in (Я был создан в:) {birth_year}.')


def remind_name():
    print('Please, remind me your name. (Пожалуйста, скажи своё имя.)')
    name = input()
    print(f'What a great name you have, (Какое классное у тебя имя) {name}!')


remainders_of_age = "(Для этого введи остатки от деления твоего возраста на 3, 5 и на 7)"


def guess_age():
    print('Let me guess your age. (Сейчас я попытаюсь угадать твой возраст)')
    print(f'Enter remainders of dividing your age by 3, 5 and 7. {remainders_of_age}')

    rem3 = int(input("Enter number (Введи число:)"))
    rem5 = int(input("Enter number (Введи число:)"))
    rem7 = int(input("Enter number (Введи число:)"))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is (Тебе {age} лет) that's a good time to start programming! (Хорошее время для того чтобы начать программировать)")


translate = "(Сейчас я докажу тебе, что я могу досчитать до любого числа до которого ты захочешь.)"


def count():
    print(f'Now I will prove to you that I can count to any number you want.{translate}')

    num = int(input("Enter number: (Введи число:)"))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


ask2_russian = "(Чтобы разбить программу на несколько небольших подпрограмм.)"


def quiz():
    number = 2
    ask1 = "To repeat a statement multiple times. (Чтобы повторить, что либо несколько раз)"
    ask2 = f"To decompose a program into several small subroutines. {ask2_russian}"
    ask3 = "To determine the execution time of a program. (Чтобы определить время выполнения программы.)"
    ask4 = "To interrupt the execution of a program. (Чтобы прервать выполнение программы)"

    print("Let's test your programming knowledge. (Давай проверим твои знания в программировании)")
    print("Why do we use methods? (Почему мы используем методы?)")
    print(f"1. {ask1} \n 2. {ask2} \n 3. {ask3} \n 4. {ask4}")
    answer = int(input())
    while answer != number:
        print("Why do we use methods? (Почему мы используем методы?)")
        answer = int(input())
    if answer == number:
        print('Completed, have a nice day! (Молодец!)')


def end():
    print('Have a nice day! (Пока, пока!)')


greet('S1ave', '2021')
remind_name()
guess_age()
count()
quiz()
end()
