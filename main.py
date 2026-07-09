from spelers import vraag_spelernamen
from scores import maak_startscores
from spel import start_game_loop

if __name__ == "__main__":
    de_spelers = vraag_spelernamen()
    huidige_stand = maak_startscores(de_spelers)

    print("\n--- DE STARTSTAND ---")
    for naam, score in huidige_stand.items():
        print(f"- {naam}: {score} punten")
    
    score_spel = start_game_loop(huidige_stand)