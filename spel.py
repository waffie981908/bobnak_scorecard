def start_game_loop(huidige_stand):
    ronde = 1
    game_over = False

    while not game_over:
        print(f"\n--- RONDE {ronde} ---")
        for naam, score in huidige_stand.items():
            print(f"\nHoeveel punten heeft {naam} behaald in deze ronde?")
            behaalde_punten = int(input())
            huidige_stand[naam] = huidige_stand[naam] + behaalde_punten
        
        for naam, score in huidige_stand.items():
            if score == 120:
                huidige_stand [naam] = int(score / 2)
            elif score > 120:
                game_over = True

        print("\n--- DE TUSSENSTAND ---")
        for naam, score in huidige_stand.items():
            print(f"- {naam}: {score} punten")
        


    ronde += 1

    print("\n Het spel is afgelopen!")