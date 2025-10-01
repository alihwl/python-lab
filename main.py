import calendar
import textwrap


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


def main():
    try:
        entree = input("Entrez un mois et une année (format MMAAAA ou MAAAA): ").strip()
        
        if len(entree) == 5:  
            mois = int(entree[0])
            annee = int(entree[1:])
        elif len(entree) == 6: 
            mois = int(entree[:2])
            annee = int(entree[2:])
        else:
            print("Format invalide. Utilisez MMAAAA ou MAAAA.")
            return
        
        if mois < 1 or mois > 12:
            print("Le mois doit être entre 1 et 12.")
            return
        
        afficher_titre(mois, annee)
        
        afficher_entete()
        
        premier_jour = numero_jour(1, mois, annee)
        
        numeros = suite_numeros_jours(mois, annee)
        
        decalage = "   " * premier_jour  
        suite_complete = decalage + numeros
        
        calendrier_formate = textwrap.fill(suite_complete, width=21)
        print(calendrier_formate)
        
        print("=" * 26)
        
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre valide.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    main()