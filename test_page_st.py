import streamlit as st
st.title("Ma première application Streamlit")
st.write("Bienvenue dans ce cours !")
nom = st.text_input("Quel est votre nom ?")
if nom:
    st.success(f"Enchanté, {nom} ! ")
age = st.slider("Quel est votre âge ?", 0, 100, 25)
st.write(f"Vous avez {age} ans")
job  = st.radio("Quel est votre Job ?", ["Policier", "Infirmier", "Autre"])
st.write(f"Genre choisi : { job}")
if st.button("Cliquez ici"):
    st.balloons()
