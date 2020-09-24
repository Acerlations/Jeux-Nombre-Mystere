from random import randint # Importe la fonction radint qui met un nombre aleatoire entre deux valeurs ex : randint(a,b)

def messageindice(proposition, mystere, nb_essais_restants): # Fonction aidant le joueur à trouver le nombre mystère
  if proposition < mystere : # Verifie si le nombre donné par le joueur et plus petit que le nombre mystère
    difference = mystere - proposition # Calcule la différence entre le nombre mystère et le nombre donné par le joueur. En faisant une soustraction
    if difference > 20: # Vérifie si la différence est plus grande que 20 et affiche Trop bas pour mieux aider le joueur sinon s'il affiche "Plus"
      afficher(f"Trop Bas | Encore {nb_essais_restants} essai(s)")
    else :
      afficher(f"Plus | Encore {nb_essais_restants} essai(s)")
  elif proposition > mystere: # Vice-versa car il ne faut pas avoir un nombre négatif comme différence
    difference = proposition - mystere
    if difference > 20:
      afficher(f"Trop Haut | Encore {nb_essais_restants} essai(s)")
    else :
      afficher(f"Moins | Encore {nb_essais_restants} essai(s)")

def afficher(text): # Fonction afficher
  print(text)
  return text

def demander(mini, max, nb_essais_restants): # Fonction demande le nombre mystère
  x = input("Quel est le mystere ? : ")
  if x.isdigit(): # Vérifie si le joueur a mis un nombre
    x = int(x)
    if x > max or x < mini: # Vérifie si le joueur a mis un nombre entre mini et max qui correspond aux valeurs a et b dans randint(a,b) qui sera défini dans la ligne 53
      afficher(f"Mets un resultat compris entre {mini} et {max}")
    return x
  else:
    afficher("[ERREUR] MET UN NOMBRE") 
    jouer(mini, max, nb_essais_restants) # Relance le programme car le joueur a mis autre choses qu'un nombre

def resultat(proposition ,mystere, essais): # Fonction de fin 
  if proposition == mystere : # Vérifie que sa proposition est égale au nombre mystère 
    afficher("BRAVOOO !!! Voici tes essais :")
  elif proposition != mystere : # Vérifie que sa proposition est différente au nombre mystère 
    afficher("Perdu :( Voici tes essais :")
  print(*essais, sep=", ") # Affiche tout les essais qui ont étaient enregistrés 
  afficher(f"Le chiffe mystere était {mystere}")

def jouer(mini, max, nb_essais_restants): # Fonction principale
  essais = [] # Liste qui va enregistrer tous les essais
  mystere = int(randint(mini,max)) # Arritbution de la variable mystère a l'aide de la fonction randint
  proposition = str()
  afficher(f"Bienvenue dans le jeu du nombre mystère ! Tu dois deviner un nombre ou un chiffre compris entre {mini} et {max}, à toi de jouer !") # Message explicative
  while proposition != mystere and nb_essais_restants > 0 : # Boucle qui cessera tant que le nombre mystère et le nombre donné par le joueur sont differant et que nombre d'essais et inferieur a 0
    nb_essais_restants -= 1 # On enleve -1 au nombre essais
    proposition = demander(mini, max, nb_essais_restants) # Attribution de la variable proposition à l'aide de la fonction demander
    essais.append(proposition) # Ajoute le nombre donné par le joueur dans la liste essais
    # afficher(f"{mystere}, {proposition}") # Afficher le nombre mystère et le nombre donné par le joueur pour debug s'il y à un problème
    messageindice(proposition, mystere, nb_essais_restants) # Affiche le message d'indice
  resultat(proposition, mystere, essais) # Un fois en dehors de la boucle la fonction resultat est appelé

jouer(1,100,5) # Appelle la fonction jouer. a = 1 et b = 100 dans randint(a,b) et 5 le nombre essais possible
