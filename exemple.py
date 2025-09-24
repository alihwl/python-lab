def formater(n, mot):
    return f"{n} {mot}{'' if n == 1 else 's'}"  

def main():
    try:
        total = int(input("Entrez un nombre de secondes: ").strip())
        if total < 0:
            print("Le nombre doit être positif.")
            return
    except ValueError:
        print("Entrée invalide.")
        return

    minutes = total // 60
    secondes = total % 60

    print(f"{formater(minutes, 'minute')} et {formater(secondes, 'seconde')}.")

if __name__ == "__main__":
    main()