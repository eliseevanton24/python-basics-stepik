import random

word_list = ["python", "programming", "computer", "science", "algorithm"]

def random_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    # начало игры
    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input("Введите букву или слово целиком: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже называли эту букву:", guess)
            elif guess not in word:
                print(f"Буквы {guess} нет в слове:")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Отлично! Буква {guess} есть в слове:")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Вы уже называли это слово:", guess)
            elif guess != word:
                print("Это не правильное слово:", guess)
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Неверный ввод — введите букву или слово целиком.")

        print(display_hangman(tries))
        print(word_completion)

    # конец игры
    if guessed:
        print("Поздравляем, вы угадали слово! Вы победили!")
    else:
        print(f"Попытки закончились. Загаданное слово: {word}")

word = random_word()
play(word)