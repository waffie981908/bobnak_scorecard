import streamlit as st

def start_game_loop(huidige_stand):
    if "ronde" not in st.session_state:
        st.session_state.ronde = 1
    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    if not st.session_state.game_over:
        st.header(f"Ronde {st.session_state.ronde}")
        
        with st.form(key=f"ronde_{st.session_state.ronde}"):
            ronde_inputs = {}
            for naam, score in huidige_stand.items():
                ronde_inputs[naam] = st.number_input(f"Hoeveel punten heeft {naam} behaald?", min_value=-50, max_value=150, value=0, key=f"{naam}_{st.session_state.ronde}")
            
            submit = st.form_submit_button("Ronde afronden")
            
            if submit:
                for naam in huidige_stand.keys():
                    huidige_stand[naam] = huidige_stand[naam] + ronde_inputs[naam]
                
                for naam, score in huidige_stand.items():
                    if score == 120:
                        huidige_stand[naam] = int(score / 2)
                    elif score > 120:
                        st.session_state.game_over = True
                
                st.session_state.ronde += 1
                st.rerun()

        st.subheader("Score Laatste Ronde:")
        for naam, score in huidige_stand.items():
            st.write(f"- **{naam}**: {score} punten")

    else:
        st.header("\n 🎉 Het spel is afgelopen!")
        st.subheader("Eindstand:")
        for naam, score in huidige_stand.items():
            st.write(f"- **{naam}**: {score} punten")
            
        if st.button("🔄 Speel opnieuw"):
            del st.session_state.game_started
            del st.session_state.ronde
            del st.session_state.game_over
            st.rerun()
