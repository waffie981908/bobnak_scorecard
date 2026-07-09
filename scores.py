def maak_startscores(speler_lijst):
    startstand = {}
    for speler in speler_lijst:
        startstand[speler] = 0
    return startstand