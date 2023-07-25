from evidence import Evidence

print("____________________")
print("Evidence pojistených")
print("____________________")
print(" ")
evidence = Evidence()

while True:
    print("Vyberte si akci: ")
    print("1. Pridat nového pojisteného")
    print("2. Vypsat všechny pojistené")
    print("3. Vyhledat pojisteného")
    print("4. Konec")
    volba = input("Zadejte číslo operace (1/2/3/4): ")

    if volba == '1':
        jmeno = input("jmeno: ")
        prijmeni = input("prijmeni: ")
        vek = input("věk: ")
        cislo = input("telefonní číslo: ")
        print(" ")
        print("Data byla uložená. Pokračujte libovolnou klávesou...")
        input()
        evidence.vloz(jmeno, prijmeni, vek, cislo)
    elif volba == '2':
        print(" ")
        evidence.vypis()
        print(" ")
        print("Pokračujte libovolnou klávesou...")
        input()
    elif volba == '3':
        jmeno = input("Zadejte jméno pojisteného: ")
        prijmeni = input("Zadejte příjmení: ")
        vyhledaj_poistenec = evidence.vyhledat_poistenec(jmeno, prijmeni)
        if vyhledaj_poistenec:
            print(" ")
            print(vyhledaj_poistenec)
            print(" ")
            print("Pokračujte libovolnou klávesou...")
            input()
        else:
            print("Pojištěný nebyl nalezen.")
            print(" ")
            print("Pokračujte libovolnou klávesou...")
            input()

    elif volba == '4':
        print("Konec programu.")
        break
    else:
        print("Neplatná volba. Zadejte prosím číslo 1-4.")
