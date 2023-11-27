# Tp_cryptographie
--------------Chiffrement et dechiffrement affine -------------------------

Fonction affine

La fonction affine() prend trois arguments :

texte : le texte à chiffrer ou à déchiffrer
a : le coefficient de rotation
b : le décalage
La fonction affine() fonctionne en effectuant une rotation de l'alphabet par un certain nombre de positions. Le coefficient de rotation a détermine le nombre de positions de la rotation, et le décalage b détermine la position de départ de la rotation.

La fonction affine() fonctionne comme suit :

Elle convertit chaque lettre du texte en minuscule.
Elle calcule la position de la lettre dans l'alphabet, en partant de la lettre a.
Elle effectue la rotation en multipliant la position de la lettre par le coefficient de rotation a et en ajoutant le décalage b.
Elle calcule la nouvelle position de la lettre dans l'alphabet, en arrondissant le résultat à l'entier inférieur.
Elle convertit la lettre en majuscule si elle l'était initialement.
Paramètre mode

Le paramètre mode permet de déterminer si le texte doit être chiffré ou déchiffré. La valeur par défaut de mode est +, ce qui signifie que le texte est chiffré. Pour déchiffrer le texte, il faut spécifier mode à -.

Lorsque mode est égal à +, la fonction affine() effectue le chiffrement en multipliant la position de la lettre par le coefficient de rotation a et en ajoutant le décalage b.

Lorsque mode est égal à -, la fonction affine() effectue le déchiffrement en multipliant la position de la lettre par le coefficient de rotation a et en soustrayant le décalage b.

Conclusion

La fonction affine() permet de chiffrer ou de déchiffrer un texte en utilisant un chiffrement affine. Le coefficient de rotation a doit être premier avec 26 pour que le chiffrement soit sécurisé.


--------------------Chiffrement de polybe --------------------------------------

Le code ci-dessus permet de chiffrer ou déchiffrer un texte en utilisant le chiffrement de Polybe.

Le chiffrement de Polybe est un chiffrement par substitution qui utilise un carré de Polybe. Un carré de Polybe est un tableau de 5x5 contenant les lettres de l'alphabet.

Pour chiffrer un texte, on remplace chaque lettre par sa position dans le carré de Polybe. Par exemple, la lettre "A" est remplacée par "11", la lettre "B" par "12", etc.

Le code ci-dessus fonctionne comme suit :

La fonction polybe() prend deux arguments :
message : le texte à chiffrer ou à déchiffrer
operation : l'opération à effectuer (chiffrement ou déchiffrement)
La fonction commence par créer une variable grille qui contient le carré de Polybe.
Si l'opération est le chiffrement, la fonction parcourt chaque lettre du message.
Si la lettre est J, elle est remplacée par I.
Pour chaque lettre, la fonction parcourt chaque cellule de la grille.
Si la cellule contient la lettre, la fonction ajoute la position de la cellule à la variable chiffre.
La fonction renvoie la variable chiffre.
Si l'opération est le déchiffrement, la fonction parcourt le texte chiffré.
Pour chaque paire de chiffres, la fonction calcule la ligne et la colonne correspondantes dans la grille.
La fonction renvoie la lettre à la position (ligne, colonne).
Par exemple, pour chiffrer le texte "HELLO", on obtient le texte chiffré "12345".

Pour déchiffrer le texte "12345", on obtient le texte clair "HELLO".
