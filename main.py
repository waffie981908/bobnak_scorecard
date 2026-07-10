import streamlit as st
from scores import maak_startscores
from spel import start_game_loop

st.title("Bobnak Scorecard")

if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "laatste_ronde_scores" not in st.session_state:
    st.session_state.laatste_ronde_scores = {}

if not st.session_state.game_started:
    st.subheader("Welkom, hoeveel mensen spelen mee?")
    
    aantal = st.number_input("Aantal spelers:", min_value=1, max_value=15, value=3)
    
    de_spelers = []
    
    for i in range(aantal):
        extensie = "ste" if (i + 1) == 1 or (i + 1) == 8 else "de"
        naam = st.text_input(f"Voer de {i + 1}{extensie} naam in:", key=f"speler_naam_{i}")
        if naam.strip():
            de_spelers.append(naam.strip())
    
    st.write("---")
    
    if len(de_spelers) == aantal:
        if st.button("🚀 Start het spel"):
            st.session_state.de_spelers = de_spelers
            st.session_state.huidige_stand = maak_startscores(de_spelers)
            st.session_state.game_started = True
            st.rerun()
    else:
        st.info("Vul alle spelersnamen in om de startknop te activeren.")

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
            st.session_state.laatste_ronde_scores = ronde_inputs
            
            start_game_loop(st.session_state.huidige_stand, ronde_inputs)
            st.rerun()

    if st.session_state.laatste_ronde_scores:
        st.subheader("⏱️ Punten laatste ronde")
        for naam, score in st.session_state.laatste_ronde_scores.items():
            st.write(f"- {naam}: {score} punten")
            
    st.write("---")

    st.subheader("📊 Tussenstand")
    for naam, score in st.session_state.huidige_stand.items():
        st.write(f"- **{naam}**: {score} punten")

else:
    st.balloons()
    st.header("🏁 Het spel is afgelopen!")
    
    st.subheader("Eindstand:")
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
