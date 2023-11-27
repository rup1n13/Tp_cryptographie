# coding:utf-8
import math


def affine(texte, a, b, mode):
    # Verifier si a est premeier avec 26
    if math.gcd(a, 26) == 1:
        result = ""
        for char in texte:
            if (char.isalpha()):
                # verifier si le caractère est en majuscule
                is_uppercase = char.isupper()

                # convertir le caractère en minuscule
                char = char.lower()

                # faire la rotation et obtenir la lettre après rotation
                if mode == "-":
                    # - pour faire le déchiffrement
                    char = chr(((ord(char) - ord('a')) * a - b) % 26 + ord('a'))
                else:
                    # + pour faire le chiffrement
                    char = chr(((ord(char) - ord('a')) * a + b) % 26 + ord('a'))

                # reconvertir en majuscule si elle l'etait
                if (is_uppercase):
                    char = char.upper()

                result += char
            else:
                result += char

        return result
    else:
        print(f"{a} doit être premier avec 26")


# Exemple d'exécution de la fonction
test = affine('Bonjour les amis', 1, 1, '+')
# Nous auront un retour comme ce ci : Cpokpvs mft bnjt
print(test, '\n')

#Nous allons m intenat dechiffrer le resultat du test 1 
test2 = affine(test, 1, 1, '-')
# Nous auront un retour comme ce ci : Bonjour les amis
print(test2)

