def vraag_spelernamen():
    print("welkom, hoeveel mensen spelen mee?")
    aantal = int(input())
    
    spelers = []
    
    for i in range (aantal):
        print(f"voer de {i + 1}ste naam in")
        naam = input()
        spelers.append(naam)
    return spelers