def polybe(message, operation='chiffremnt'):
    grille = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]

   
    if operation == 'chiffremnt' :
        chiffre = ""
        for char in message:
            # rechercher le caractère j dans le message et s'il est trouver le remplcer par I
            if char == 'J':
                char = 'I' 
            
            #Parcourir chaque cellule de la grille
            for i in range(5):
                for j in range(5):
                    if grille[i][j] == char:
                        # ajouter la position du caractère ainsi trouver dans la variable chiffre
                        chiffre += str(i+1) + str(j+1)
        return chiffre
    
    #dechiffrement
    elif operation == 'dechiffrement' :
        resultat = ""
        for i in range(0, len(message), 2) :
            ligne = int(message[i]) - 1
            colonne = int(message[i+1]) - 1
            resultat += grille[ligne][colonne]
        return resultat



# Example usage
message_clair = "HELLO"
message_chiffre = polybe(message_clair)
print(message_chiffre)

message_chiffre2 = message_chiffre
message_clair2 = polybe(message_chiffre2, 'dechiffrement')
print(message_clair2)

