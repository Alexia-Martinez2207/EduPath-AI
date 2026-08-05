from __future__ import annotations

from datetime import datetime
from typing import Any

import streamlit as st

from services.analysis_service import (
    build_edubot_message,
    build_insights,
    classify_risk,
)
from services.model_service import predict_score
from ui.components import (
    render_action,
    render_edubot,
    render_insight,
    render_page_header,
    render_result_summary,
)
from ui.styles import html


GENDER_MAP = {
    "Masculino": 0,
    "Femenino": 1,
}

ETHNICITY_MAP = {
    "Caucásico": 0,
    "Afroamericano": 1,
    "Asiático": 2,
    "Otro": 3,
}

PARENT_EDUCATION_MAP = {
    "Sin escolaridad formal": 0,
    "Educación media superior": 1,
    "Estudios universitarios incompletos": 2,
    "Licenciatura": 3,
    "Posgrado": 4,
}

FAMILY_SUPPORT_MAP = {
    "Sin acompañamiento": 0,
    "Bajo": 1,
    "Moderado": 2,
    "Alto": 3,
    "Muy alto": 4,
}

YES_NO_MAP = {
    "No": 0,
    "Sí": 1,
}


def _render_form() -> dict[str, int | float] | None:
    html(
        """
        <div class="steps">
            <div class="step-card"><b>01</b> Perfil personal</div>
            <div class="step-card"><b>02</b> Hábitos académicos</div>
            <div class="step-card"><b>03</b> Entorno y actividades</div>
        </div>
        """
    )

    with st.form("formulario_evaluacion"):
        tab1, tab2, tab3 = st.tabs(
            [
                "👤 Perfil",
                "📚 Hábitos académicos",
                "🌱 Entorno y actividades",
            ]
        )

        with tab1:
            left, right = st.columns(2)

            with left:
                age = st.slider(
                    "Edad",
                    min_value=15,
                    max_value=18,
                    value=16,
                )

                gender_text = st.selectbox(
                    "Género",
                    options=list(GENDER_MAP.keys()),
                )

            with right:
                ethnicity_text = st.selectbox(
                    "Grupo étnico",
                    options=list(ETHNICITY_MAP.keys()),
                )

                parent_education_text = st.selectbox(
                    "Escolaridad de padres o tutores",
                    options=list(PARENT_EDUCATION_MAP.keys()),
                )

        with tab2:
            left, right = st.columns(2)

            with left:
                study_hours = st.slider(
                    "Horas de estudio por semana",
                    min_value=0.0,
                    max_value=20.0,
                    value=10.0,
                    step=0.5,
                )

                absences = st.slider(
                    "Ausencias acumuladas",
                    min_value=0,
                    max_value=29,
                    value=10,
                )

            with right:
                tutoring_text = st.radio(
                    "¿Cuenta con tutorías?",
                    options=list(YES_NO_MAP.keys()),
                    horizontal=True,
                )

                family_support_text = st.selectbox(
                    "Nivel de acompañamiento familiar",
                    options=list(FAMILY_SUPPORT_MAP.keys()),
                    index=2,
                )

        with tab3:
            left, right = st.columns(2)

            with left:
                extracurricular_text = st.radio(
                    "Actividades extracurriculares",
                    options=list(YES_NO_MAP.keys()),
                    horizontal=True,
                )

                sports_text = st.radio(
                    "Práctica deportiva",
                    options=list(YES_NO_MAP.keys()),
                    horizontal=True,
                )

            with right:
                music_text = st.radio(
                    "Actividades musicales",
                    options=list(YES_NO_MAP.keys()),
                    horizontal=True,
                )

                volunteering_text = st.radio(
                    "Voluntariado",
                    options=list(YES_NO_MAP.keys()),
                    horizontal=True,
                )

        submitted = st.form_submit_button(
            "Generar análisis inteligente →",
            use_container_width=True,
        )

    if not submitted:
        return None

    return {
        "Age": age,
        "Gender": GENDER_MAP[gender_text],
        "Ethnicity": ETHNICITY_MAP[ethnicity_text],
        "ParentalEducation": PARENT_EDUCATION_MAP[parent_education_text],
        "StudyTimeWeekly": study_hours,
        "Absences": absences,
        "Tutoring": YES_NO_MAP[tutoring_text],
        "ParentalSupport": FAMILY_SUPPORT_MAP[family_support_text],
        "Extracurricular": YES_NO_MAP[extracurricular_text],
        "Sports": YES_NO_MAP[sports_text],
        "Music": YES_NO_MAP[music_text],
        "Volunteering": YES_NO_MAP[volunteering_text],
    }


def _create_result(
    model: Any,
    feature_names: list[str],
    values: dict[str, int | float],
) -> dict:
    score = predict_score(model, feature_names, values)
    risk = classify_risk(score)

    activity_count = sum(
        int(values[name])
        for name in [
            "Extracurricular",
            "Sports",
            "Music",
            "Volunteering",
        ]
    )

    strengths, alerts, actions = build_insights(
        absences=int(values["Absences"]),
        study_hours=float(values["StudyTimeWeekly"]),
        tutoring=int(values["Tutoring"]),
        family_support=int(values["ParentalSupport"]),
        activities=activity_count,
    )

    result = {
        "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "score": score,
        "risk": risk,
        "strengths": strengths,
        "alerts": alerts,
        "actions": actions,
        "absences": int(values["Absences"]),
        "study_hours": float(values["StudyTimeWeekly"]),
    }

    result["edubot_message"] = build_edubot_message(result)
    return result


def _save_result(result: dict) -> None:
    st.session_state.ultimo_resultado = result

    st.session_state.historial.insert(
        0,
        {
            "Fecha": result["date"],
            "Promedio estimado": round(result["score"], 2),
            "Nivel de riesgo": result["risk"]["name"],
            "Ausencias": result["absences"],
            "Horas de estudio": result["study_hours"],
        },
    )


def _render_result(result: dict) -> None:
    st.divider()

    render_page_header(
        "Resultado",
        "Una lectura clara para decidir mejor",
        "La estimación se acompaña de señales transparentes "
        "y acciones sugeridas."
    )

    render_result_summary(result)
    st.write("")

    left, right = st.columns(2)

    with left:
        st.markdown("### Fortalezas")

        if result["strengths"]:
            for item in result["strengths"]:
                render_insight(item, "strength")
        else:
            st.caption(
                "No se detectaron fortalezas específicas "
                "con las reglas actuales."
            )

    with right:
        st.markdown("### Señales de atención")

        if result["alerts"]:
            for item in result["alerts"]:
                render_insight(item, "alert")
        else:
            render_insight(
                "No se detectaron señales prioritarias.",
                "strength",
            )

    st.markdown("### Plan de acción recomendado")

    for index, action in enumerate(result["actions"], start=1):
        render_action(index, action)

    render_edubot(result["edubot_message"])

    st.caption(
        "La clasificación de riesgo y las recomendaciones son reglas "
        "de apoyo construidas sobre la estimación del modelo. "
        "No constituyen un diagnóstico."
    )


def render_evaluation(
    model: Any,
    feature_names: list[str],
) -> None:
    render_page_header(
        "Nueva evaluación",
        "Conozcamos el perfil del estudiante",
        "Completa las tres etapas. La plataforma traduce los datos "
        "a una lectura clara y útil."
    )

    values = _render_form()

    if values is not None:
        try:
            result = _create_result(model, feature_names, values)
            _save_result(result)
        except Exception as error:
            st.error(
                f"No fue posible generar la evaluación: {error}"
            )

    if st.session_state.ultimo_resultado is not None:
        _render_result(st.session_state.ultimo_resultado)
