import streamlit as st
st.header('Home')

# Centrar el contenido
st.markdown("<h1 style='text-align: center;'>Home</h1>", unsafe_allow_html=True)

# Centrar la imagen y ajustar el tamaño
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <img src="assets/sc_logo.png" width="400">
    </div>
    """,
    unsafe_allow_html=True
)
