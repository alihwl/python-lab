import calendrier
import textwrap


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
        
        calendrier.afficher_titre(mois, annee)
        
        calendrier.afficher_entete()
        
        premier_jour = calendrier.numero_jour(1, mois, annee)
        
        numeros = calendrier.suite_numeros_jours(mois, annee)
        
        decalage = "   " * premier_jour  
        suite_complete = decalage + numeros
        
        calendrier_formate = textwrap.fill(suite_complete, width=21)
        print(calendrier_formate)
        
        print("=" * 26)
        
    except ValueError:
        print("Entrée invalide. Veuillez entrer u nombre valide.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    main()