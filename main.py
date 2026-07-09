elif not st.session_state.game_over:
    st.header(f"🎯 Ronde {st.session_state.ronde}")
    
    if "laatste_ronde_scores" not in st.session_state:
        st.session_state.laatste_ronde_scores = {}
    
    with st.form(key=f"ronde_{st.session_state.ronde}"):
        st.write("Vul de behaalde punten van deze ronde in:")
        ronde_inputs = {}
        for naam, score in st.session_state.huidige_stand.items():
            ronde_inputs[naam] = st.number_input(f"Punten voor {naam}:", min_value=-50, max_value=150, value=0, key=f"{naam}_{st.session_state.ronde}")
        
        submit = st.form_submit_button("Ronde afronden")
        
        if submit:
            # Sla de ingevulde punten van DIT moment op als de 'laatste ronde'
            st.session_state.laatste_ronde_scores = ronde_inputs
            
            # Verwerk daarna pas de totale stand via spel.py
            from spel import start_game_loop
            start_game_loop(st.session_state.huidige_stand, ronde_inputs)
            st.rerun()

    # --- HIER TONEN WE DE BEIDE STUKKEN APART ---
    
    # Stuk 1: Punten laatste ronde (alleen tonen als er al een ronde gespeeld is)
    if st.session_state.laatste_ronde_scores:
        st.subheader("⏱️ Punten laatste ronde")
        for naam, score in st.session_state.laatste_ronde_scores.items():
            st.write(f"- {naam}: +{score} punten")
            
    st.write("---") # Trek een mooi lijntje tussen de twee stukken

    # Stuk 2: Totale tussenstand
    st.subheader("📊 Totale tussenstand")
    for naam, score in st.session_state.huidige_stand.items():
        st.write(f"- **{naam}**: {score} punten")

else:
    # (Je bestaande game over code mag hier gewoon blijven staan!)
    
    # Stap 4: Start de game loop
    start_game_loop(st.session_state.huidige_stand)
