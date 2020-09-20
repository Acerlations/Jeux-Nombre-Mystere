from random import randint # Importe la fonction radint qui met un nombre aleatoire entre deux valeurs ex : randint(a,b)

def messageindice(proposition, mystere, nb_essais): # Fonction aidant le joueur à trouver le nombre mystere
  if proposition < mystere : # Verifie si le nombre donné par le joueur et plus petit que le nombre mystere
    difference = mystere - proposition # Calcule la difference entre le nombre mystere et le nombre donné par le joueur. En faisant une soustraction
    if difference > 20: # Verifie si la difference est plus grande que 20 et affiche Trop bas pour mieux aider le joueur sinon si il affiche "Plus"
      afficher(f"Trop Bas | Encore {nb_essais} essai(s)")
    else :
      afficher(f"Plus | Encore {nb_essais} essai(s)")
  elif proposition > mystere: # Vice versa car il ne faut pas avoir un nombre négatif comme difference
    difference = proposition - mystere
    if difference > 20:
      afficher(f"Trop Haut | Encore {nb_essais} essai(s)")
    else :
      afficher(f"Moins | Encore {nb_essais} essai(s)")

def afficher(text): # Fonction afficher
  print(text)
  return text

def demander(mini, max, nb_essais): # Fonction demande le nombre mystere
  x = input("Quel est le mystere ? : ")
  if x.isdigit(): # Verifie si le joueur à mis un nombre
    x = int(x)
    if x > max or x < mini: # Verifie si le joueur à mis un nombre entre mini et max qui la valeur a et b dans randint(a,b)
      afficher(f"Met un resulet compris entre {mini} et {max}")
    return x
  else:
    afficher("[ERREUR] MET UN NOMBRE | RELANCEMENT DU JEUX") 
    jouer(1,100,10) # Relance le programme car le joueur a mis autre choses qu'un nombre

def resultat(proposition ,mystere, coups): # Fonction de fin 
  if proposition == mystere : # Verefie que sa proposition est egale au nombre mystere 
    afficher("BRAVOOO !!! Voici tes coups :")
  elif proposition != mystere : # Verefie que sa proposition est differente au nombre mystere 
    afficher("Perdu :( Voici tes coups :")
  print(*coups, sep=", ") # Affiche tout les coups qui ont étaient enregistrés 
  afficher(f"Le chiffe mystere était {mystere}")

def jouer(mini, max, nb_essais): # Fonction principale
  coups = [] # Liste qui vas enregistrer tout les coups
  mystere = int(randint(mini,max)) # Arritbution de la variable mystere a l'aide de la fonction randint
  proposition = str()
  afficher(f"Bienvenue dans le jeu du nombre mystere ! Tu dois deviner un nombre ou un chiffre compris entre {mini} et {max}, à toi de jouer !") # Message explicative
  while proposition != mystere and nb_essais > 0 : # Boucle qui ne tant cessera tant que le nombre mystere et le nombre donné par le joueur sont differant et que nombre d'essais et inferieur a 0
    nb_essais -= 1 # On enleve -1 au nombre essais
    proposition = demander(mini, max, nb_essais) # Atribution de la variable proposition a l'aide de la fonction demander
    coups.append(proposition) # Ajoute le nombre donné par le joueur dans la liste coups
    # afficher(f"{mystere}, {proposition}") # Afficher le nombre mystere et le nombre donné par le joueur pour debug si il y a un problème
    messageindice(proposition, mystere, nb_essais) # Affiche le message d'indice
  resultat(proposition, mystere, coups) # Un fois en dehors de la boucle la fonction resultat est appele

jouer(1,100,10) # Appelle la fonction jouer 
