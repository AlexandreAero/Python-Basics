# Ecrire un programme qui demande deux nombres à l’utilisateur et l’informe ensuite si 
# leur produit est négatif ou positif. Attention toutefois on ne doit pas calculer le 
# produit des deux nombres.

a = int(input("saisir a : "))
b = int(input("saisir b : "))

if a < 0 or b < 0 :
    print("Le resultat sera négatif")

else :
    print("Le resultat sera positif")