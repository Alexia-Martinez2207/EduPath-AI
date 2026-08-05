from __future__ import annotations

import pandas as pd
import streamlit as st

from ui.components import render_page_header


def render_history() -> None:
    render_page_header(
        "Historial",
        "Evaluaciones de esta sesión",
        "El historial se conserva mientras la aplicación permanezca abierta."
    )

    if st.session_state.historial:
        st.dataframe(
            pd.DataFrame(st.session_state.historial),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info(
            "Todavía no has generado evaluaciones en esta sesión."
        )
