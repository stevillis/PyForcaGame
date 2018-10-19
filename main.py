# coding: utf-8

__author__ = "Stévillis Sousa"

from random import randint


def formatWord(s):
    """
    A function to return Portuguese words based on file words.txt.
    :param s: String to format,  since the words.txt contains many words with /somecode and I didn't want to rewrite the
    file.
    :return: A Portuguese word.
    """
    if s.find("/") > -1:
        word = s[:s.index("/")]
        return word
    if s.find("\n"):
        word = s[:s.index("\n")]
        return word
    return s


def numOfWords(file):
    """
    A function to get the number of words in a file.
    :param file: The file read the words in.
    :return: The number of words found.
    """
    num_of_words = 0

    for _ in file:
        num_of_words += 1
    return num_of_words


def randWord():
    """
    Select randomly a Portuguese word in the words.txt file.
    :return: A Portuguese word.
    """
    # Open the file to count the number of words and select one of them
    with open("words.txt", encoding="utf-8") as file:
        position = randint(0, numOfWords(file))

    with open("words.txt", encoding="utf-8") as file:  # Open the file to get a specific word
        for i, line in enumerate(file):
            if i == position:
                return formatWord(line)


if __name__ == "__main__":
    playAgain = True  # If the player wants to play again

    while playAgain:
        discovered_words = []  # Words discovered
        attempts = 0  # Number of attempts
        attempts_list = []  # Attempted letters
        isCorrect = False  # If the player hit all the letters

        print("\n***** Jogo da Forca *****\n")

        rand_word = list(randWord().upper())
        print("Palavra:", "- " * len(rand_word), end="\t")
        print(f'{len(rand_word)} letras\tVocê tem {len(rand_word) * 3} tentativas\n')

        attempts_limit = len(rand_word) * 3  # Maximum of attempts allowed is 3

        for i in range(0, len(rand_word)):  # Fill the discovered_words list with - (number of letters of rand_word)
            discovered_words.append("-")

        while not isCorrect:  # While the player doesn't hit all the letters
            attempts += 1
            letter = str(input(f"(Tentativa {attempts}) Digite a letra: "))[0].upper()  # Get the first letter pressed

            # If the letter has not been used yet, add it to the attempts_list
            if len(attempts_list) == 0 or letter not in attempts_list:
                attempts_list.append(letter)

            for i in range(0, len(rand_word)):
                if letter == rand_word[i]:  # If the letter is in the rand_word, then replace the - for the letter
                    discovered_words[i] = letter

                print(f'{discovered_words[i]} ', end="")  # Show the selected word replaced with the letter

            print('\n\nLetras chutadas: ', end="")
            for letters in attempts_list:  # Show the attempted letters
                print(f'{letters}', sep=" ", end=" ")

            isCorrect = True
            print("\n")

            for x in range(0, len(discovered_words)):
                # If there's no more - in discovered_words, the player have found all the letters, thus the game ends
                if discovered_words[x] == "-":
                    isCorrect = False

            if attempts == attempts_limit:  # Check if is the maximum attempt
                break

        if attempts == attempts_limit:
            print(
                f"VOCÊ PERDEU!!! :( \nAtingiu o número máximo de tentativas: {attempts}\nA palavra correta é: {''.join(rand_word)}")
        else:
            print(f"VOCÊ VENCEU!!! :D\nNúmero de tentativas: {attempts}")

        if str(input("Jogar novamente? (Pressione ENTER)")) != '':  # Ask if player wants to play again
            print("Jogo encerrado. Até a próxima! ;)")
            playAgain = False
