import streamlit as st

paginas = [
    st.Page("src/laboratorio_cg/atv1.py", title="Atv 1"),
    st.Page("src/laboratorio_cg/atv2.py", title="Atv 2 - Bandeira do Brasil"),
]
st.navigation(paginas).run()
