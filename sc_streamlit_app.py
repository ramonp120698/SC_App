import streamlit as st
# --- SHARED ON ALL PAGES ---
with st.sidebar:
    st.image("assets/SC_logo2.png", width=200)

# --- PAGE SETUP ---
about_page = st.Page(
    "pages/taka_page.py",
    title="Taka",
    icon=":material/videocam:",
    default=True,
)
project_1_page = st.Page(
    "pages/byga_page.py",
    title="Byga",
    icon=":material/analytics:",
)
project_2_page = st.Page(
    "pages/Achamp_page.py",
    title="A-Champ",
    icon=":material/sports_and_outdoors:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)






# --- RUN NAVIGATION ---
pg.run()
