import calendar


MOIS_FR = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


def afficher_titre(mois, annee):
    titre = f"{MOIS_FR[mois].capitalize()} {annee}"
    largeur = max(26, len(titre))
    print("=" * largeur)
    print(titre.center(largeur))
    print("=" * largeur)


def afficher_entete():
     print("Lu Ma Me Je Ve Sa Di")


def numero_jour(jour, mois, annee):
    return calendar.weekday(annee, mois, jour)


def suite_numeros_jours(mois, annee):
    nb_jours = calendar.monthrange(annee, mois)[1]
    numeros = []
    for jour in range(1, nb_jours + 1):
        numeros.append(f"{jour:2d} ")
    return "".join(numeros)
