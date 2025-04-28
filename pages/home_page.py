import streamlit as st


# Espaciador
st.markdown("<br>", unsafe_allow_html=True)

# Cargar imagen de forma correcta
st.image("assets/sc_logo.png", width=400)

# Centramos toda la imagen con el contenedor
st.markdown(
    """
    <style>
    .stImage > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)
