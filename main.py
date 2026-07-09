import streamlit as st
from spelers import vraag_spelernamen
from scores import maak_startscores
from spel import start_game_loop

st.title("🃏 Bobnak Scorecard")

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if not st.session_state.game_started:
    de_spelers = vraag_spelernamen()
    
if de_spelers and st.button("🚀 Start het spel"):
        st.session_state.de_spelers = de_spelers
        st.session_state.huidige_stand = maak_startscores(de_spelers)
        st.session_state.game_started = True
        st.rerun()
else:
    st.header("--- DE STARTSTAND ---")
    for naam, score in st.session_state.huidige_stand.items():
        st.write(f"- **{naam}**: {score} punten")
    
    start_game_loop(st.session_state.huidige_stand)
