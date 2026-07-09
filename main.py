import streamlit as st
from scores import maak_startscores
from spel import start_game_loop

st.title("🃏 Bobnak Scorecard")

# --- STAP 1: GEHEUGEN INITIALISEREN ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "laatste_ronde_scores" not in st.session_state:
    st.session_state.laatste_ronde_scores = {}

# --- STAP 2: SPELERS INVOEREN (RECHTSTREEKS IN MAIN) ---
if not st.session_state.game_started:
    st.subheader("Welkom, hoeveel mensen spelen mee?")
    
    # Dit vervangt de input() uit je oude terminal-code
    aantal = st.number_input("Aantal spelers:", min_value=1, max_value=10, value=3)
    
    de_spelers = []
    
    # Jouw exacte loop-logica om namen te verzamelen, maar dan visueel
    for i in range(aantal):
        naam = st.text_input(f"Voer de {i + 1}ste naam in:", key=f"speler_naam_{i}")
        if naam.strip():
            de_spelers.append(naam.strip())
    
    st.write("---")
    
    # Toon de startknop zodra alle spelers een naam hebben gekregen
    if len(de_spelers) == aantal:
        if st.button("🚀 Start het spel"):
            st.session_state.de_spelers = de_spelers
            st.session_state.huidige_stand = maak_startscores(de_spelers)
            st.session_state.game_started = True
            st.rerun()
    else:
        st.info("Vul alle spelersnamen in om de startknop te activeren.")

# --- STAP 3: HET SPEL IS BEZIG ---
elif not st.session_state.get("game_over", False):
    st.header(f"🎯 Ronde {st.session_state.get('ronde', 1)}")
    
    with st.form(key=f"ronde_{st.session_state.get('ronde', 1)}"):
        st.write("Vul de behaalde punten van deze ronde in:")
        ronde_inputs = {}
        
        for naam, score in st.session_state.huidige_stand.items():
            ronde_inputs[naam] = st.number_input(
                f"Punten voor {naam}:", 
                min_value=-50, 
                max_value=150, 
                value=0, 
                key=f"{naam}_{st.session_state.get('ronde', 1)}"
            )
        
        submit = st.form_submit_button("Ronde afronden")
        
        if submit:
            # 1. Sla de losse punten van deze ronde apart op
            st.session_state.laatste_ronde_scores = ronde_inputs
            
            # 2. Bereken de nieuwe totale stand via spel.py
            start_game_loop(st.session_state.huidige_stand, ronde_inputs)
            st.rerun()

    # --- DE SCOREBOARD WEERGAVE ---
    if st.session_state.laatste_ronde_scores:
        st.subheader("⏱️ Punten laatste ronde")
        for naam, score in st.session_state.laatste_ronde_scores.items():
            st.write(f"- {naam}: +{score} punten")
            
    st.write("---")

    st.subheader("📊 Totale tussenstand")
    for naam, score in st.session_state.huidige_stand.items():
        st.write(f"- **{naam}**: {score} punten")

# --- STAP 4: GAME OVER (EINDSTAND) ---
else:
    st.balloons()
    st.header("🏁 Het spel is afgelopen!")
    
    st.subheader("--- EINDSTAND ---")
    for naam, score in st.session_state.huidige_stand.items():
        st.write(f"- **{naam}**: {score} punten")
        
    if st.button("🔄 Speel opnieuw"):
        del st.session_state.game_started
        del st.session_state.laatste_ronde_scores
        if "ronde" in st.session_state:
            del st.session_state.ronde
        if "game_over" in st.session_state:
            del st.session_state.game_over
        st.rerun()
