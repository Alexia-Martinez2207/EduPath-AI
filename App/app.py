from __future__ import annotations

from pathlib import Path

import streamlit as st

from services.model_service import load_model
from ui.styles import apply_styles, render_topbar
from views.evaluation import render_evaluation
from views.history import render_history
from views.home import render_home


st.set_page_config(
    page_title="EduPath AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "modelo_gpa.pkl"


def initialize_state() -> None:
    if "pagina" not in st.session_state:
        st.session_state.pagina = "Inicio"

    if "ultimo_resultado" not in st.session_state:
        st.session_state.ultimo_resultado = None

    if "historial" not in st.session_state:
        st.session_state.historial = []


def main() -> None:
    initialize_state()
    apply_styles()
    render_topbar()

    try:
        model, feature_names = load_model(MODEL_PATH)
    except Exception as error:
        st.error(str(error))
        st.stop()

    pages = ["Inicio", "Nueva evaluación", "Historial"]

    selected_page = st.radio(
        "Navegación",
        pages,
        horizontal=True,
        label_visibility="collapsed",
        index=pages.index(st.session_state.pagina),
    )

    st.session_state.pagina = selected_page

    if selected_page == "Inicio":
        render_home()
    elif selected_page == "Nueva evaluación":
        render_evaluation(model, feature_names)
    else:
        render_history()


if __name__ == "__main__":
    main()
