from string import *
import random
spe_chars = "éèçàùêâôîüïöëäµ"
chars = list( ascii_letters + " " + digits + punctuation + spe_chars + spe_chars[:-1].upper())
enc_chars = chars.copy()
random.shuffle(enc_chars)

def crypt(word: str):
    enc = ""
    for char in word:
        enc += enc_chars[chars.index(char)]
    return enc

def decryppt(word: str):
    enc = ""
    for char in word:
        enc += chars[enc_chars.index(char)]
    return enc

def choisir(list_choix: list[str] | tuple[str] | set[str | str]):
    liste = [str(x) for x in list_choix]
    lenght = max([len(x) for x in liste]) + 2
    for i in range(len(liste)):
        print(f"{f"{i + 1}":<2}. {liste[i].capitalize()}")

    print()
    choix = input("Faites votre choix: ")
    while True:
        print()
        if not choix:
            choix = input("Veuillez inserer quelque choses: ")
        elif not choix.isdigit():
            choix = input("Veuillez inserer un entier naturel: ")
        elif int(choix) not in range(1, len(liste) + 1):
            choix = input(f"Veuillez inserer une valeur comprise entre 1 et {len(liste)}: ")
        else:
            return int(choix)
        
def main():
    print("Que voulez vous faire?:")
    liste = ("crypter", "decrypter", "quitter")
    choix = choisir(liste)
    while choix in range(len(liste)):
        word = input("Quel est votre mot: ")
        if choix == 1:
            word = crypt(word)
            print(f"Voici votre mot crypté: {word}")
        else:
            word = decryppt(word)
            print(f"Voici votre mot décrypté: {word}")
        
        print()
        print("Que voulez-vous faire ensuite? ")
        choix = choisir(liste)
    
    else:
        print("Au plaisir de vous revoir!")

if __name__ == '__main__':
    main()