def nom_du_mois(index):
    mois = ["", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
            "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    return mois[index]


def afficher_titre(mois, annee):
    nom_mois = nom_du_mois(mois)
    print("=" * 26)
    print(f"{nom_mois} {annee}")
    print("=" * 26)


def afficher_entete():
    print("Lu Ma Me Je Ve Sa Di")


def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)


def suite_numeros_jours(mois, annee):
    jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if mois == 2 and est_bissextile(annee):
        nombre_jours = 29
    else:
        nombre_jours = jours_par_mois[mois]
    
    numeros = []
    for jour in range(1, nombre_jours + 1):
        numeros.append(f"{jour:02d}")
    
    return " ".join(numeros)


def numero_jour(jour, mois, annee):
    if mois <= 2:
        mois += 12
        annee -= 1
    
    q = jour
    m = mois
    K = annee % 100
    J = annee // 100
    
    h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    return (h + 5) % 7