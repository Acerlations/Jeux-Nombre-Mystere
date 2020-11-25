from random import randint  # Importe la fonction radint qui met un nombre aleatoire entre deux valeurs ex : randint(a,b)


def messageindice(proposition, mystere, nb_essais_restants):  # Fonction aidant le joueur à trouver le nombre mystère
    if proposition < mystere:
        difference = mystere - proposition
        if difference > 20:  # Vérifie si la différence est plus grande que 20 et affiche Trop bas pour mieux aider le joueur sinon s'il affiche "Plus"
            afficher(f"Trop Bas | Encore {nb_essais_restants} essai(s)")
        else:
            afficher(f"Plus | Encore {nb_essais_restants} essai(s)")
    elif proposition > mystere:  # Vice-versa car il ne faut pas avoir un nombre négatif comme différence
        difference = proposition - mystere
        if difference > 20:
            afficher(f"Trop Haut | Encore {nb_essais_restants} essai(s)")
        else:
            afficher(f"Moins | Encore {nb_essais_restants} essai(s)")


def afficher(text):  # Fonction afficher
    print(text)


def demander(mini, max, nb_essais_restants):  # Fonction demande le nombre mystère
    demande = input("Quel est le mystere ? : ")
    if demande.isdigit():
        demande = int(demande)
        if demande > max or demande < mini:  # Vérifie si le joueur a mis un nombre entre mini et max qui correspond aux valeurs a et b dans randint(a,b) qui sera défini dans la ligne 53
            afficher(f"Mets un resultat compris entre {mini} et {max}")
            return demander(mini, max, nb_essais_restants)
        return demande
    else:
        afficher("Merci de mettre un entier")
        return demander(mini, max, nb_essais_restants)


def resultat(proposition, mystere, essais):
    if proposition == mystere:
        afficher("BRAVOOO !!! Voici tes essais :")
    elif proposition != mystere:
        afficher("Perdu :( Voici tes essais :")
    print(*essais, sep=", ")
    afficher(f"Le chiffe mystere était {mystere}")


def jouer(mini, max, nb_essais_restants):
    essais = []  # Liste qui va enregistrer tous les essais
    mystere = int(randint(mini, max))
    proposition = int()
    afficher(f"Bienvenue dans le jeu du nombre mystère ! Tu dois deviner un nombre ou un chiffre compris entre {mini} et {max}, à toi de jouer !")
    while proposition != mystere and nb_essais_restants > 0:
        nb_essais_restants -= 1
        proposition = demander(mini, max, nb_essais_restants)
        essais.append(proposition)
        # afficher( f"{mystere}, {proposition}, {mini}, {max}, {nb_essais_restants}")  # Afficher le nombre mystère et le nombre donné par le joueur pour debug s'il y à un problème
        messageindice(proposition, mystere, nb_essais_restants)
    resultat(proposition, mystere, essais)


jouer(1, 100, 5)
