import streamlit as st

def vraag_spelernamen():
    st.subheader("Welkom, hoeveel mensen spelen mee?")
    
    aantal = st.number_input("Aantal spelers:", min_value=1, max_value=10, value=3)
    
    spelers = []
    
    for i in range(aantal):
        naam = st.text_input(f"Voer de {i + 1}ste naam in:", key=f"speler_naam_{i}")
        if naam.strip(): 
            spelers.append(naam.strip())
            
    return spelers
