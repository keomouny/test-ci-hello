word = ''


def reverse_word(word_test: str):
    global word
    if len(word_test):
        word += word_test[-1]
        reste_word_test = word_test[:-1]
        reverse_word(reste_word_test)
    return word


def reverse_number(nb: int):
    nb_random = 0
    if (nb > 0):
        nb_random = f'-{nb}'
        return nb_random
    else:
        nb_random = str(nb).replace('-', '+')
        return nb_random


def create_pyramide(hauteur_pyramide: int):
    if hauteur_pyramide == 10:
        for num in range(hauteur_pyramide):
            if num <= 5:
                for i in range(num):
                    print("*", end=" ")
            else:
                for i in range(hauteur_pyramide - num):
                    print("*", end=" ")
            print("\r")
        return hauteur_pyramide
    else:
        print("pyramide non créer car hauteur de pyramide n'est pas égal à 10")
        return False


if __name__ == "__main__":
    print(f"reverse word for 'maison' => {reverse_word('maison')}")
    print(f'reverse number -2 => {reverse_number(-2)}')
    print(f'reverse number +10 => {reverse_number(10)}')
    print('create pyramide :')
    create_pyramide(9)
