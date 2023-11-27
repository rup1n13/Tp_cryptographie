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
