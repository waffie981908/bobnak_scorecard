import streamlit as st

def start_game_loop(huidige_stand, ronde_inputs):
    if "ronde" not in st.session_state:
        st.session_state.ronde = 1
    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    # Tel de nieuwe ronde_inputs op bij de huidige stand
    for naam in huidige_stand.keys():
        huidige_stand[naam] = huidige_stand[naam] + ronde_inputs[naam]
    
    # Jouw exacte Bobnak & Game over regels
    for naam, score in huidige_stand.items():
        if score == 120:
            huidige_stand[naam] = int(score / 2)
        elif score > 120:
            st.session_state.game_over = True
            
    st.session_state.ronde += 1
