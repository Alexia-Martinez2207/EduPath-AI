from __future__ import annotations

import streamlit as st

from ui.components import render_feature_card
from ui.styles import html


def render_home() -> None:
    html(
        """
        <section class="hero">
            <div class="hero-copy">
                <div class="hero-badge">
                    ✦ Inteligencia educativa aplicada
                </div>

                <h1>Detecta señales. Actúa a tiempo.</h1>

                <p>
                    EduPath AI convierte información académica en una lectura
                    comprensible, señales de atención y un plan de acción
                    para acompañar mejor la trayectoria de cada estudiante.
                </p>
            </div>

            <div class="hero-panel">
                <div class="hero-stat">
                    <strong>Predicción clara</strong>
                    <span>
                        Promedio académico estimado en escala de 0 a 4.
                    </span>
                </div>

                <div class="hero-stat">
                    <strong>Señales accionables</strong>
                    <span>
                        Fortalezas, alertas y recomendaciones comprensibles.
                    </span>
                </div>

                <div class="hero-stat">
                    <strong>Intervención temprana</strong>
                    <span>
                        Información útil antes de que el problema crezca.
                    </span>
                </div>
            </div>
        </section>
        """
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        render_feature_card(
            "◎",
            "Lectura integral",
            "Integra hábitos académicos, asistencia, entorno familiar "
            "y actividades."
        )

    with col2:
        render_feature_card(
            "✦",
            "Interpretación sencilla",
            "Oculta los códigos técnicos y presenta la información "
            "en lenguaje humano."
        )

    with col3:
        render_feature_card(
            "↗",
            "Plan de acción",
            "Organiza recomendaciones concretas para facilitar "
            "el seguimiento."
        )

    st.write("")

    if st.button(
        "Comenzar nueva evaluación →",
        use_container_width=True,
    ):
        st.session_state.pagina = "Nueva evaluación"
        st.rerun()

    st.caption(
        "EduPath AI es una herramienta de apoyo. No sustituye el criterio "
        "de docentes, tutores, orientadores o especialistas."
    )
