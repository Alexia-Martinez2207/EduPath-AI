from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib
import pandas as pd
import streamlit as st


DEFAULT_FEATURES = [
    "Age",
    "Gender",
    "Ethnicity",
    "ParentalEducation",
    "StudyTimeWeekly",
    "Absences",
    "Tutoring",
    "ParentalSupport",
    "Extracurricular",
    "Sports",
    "Music",
    "Volunteering",
]


@st.cache_resource
def load_model(model_path: Path) -> tuple[Any, list[str]]:
    """Load the trained model and validate its expected feature names."""

    if not model_path.exists():
        raise FileNotFoundError(
            "No se encontró 'modelo_gpa.pkl'. Colócalo en la carpeta principal "
            "de EduPath AI, junto a app.py."
        )

    model = joblib.load(model_path)

    features = (
        list(model.feature_names_in_)
        if hasattr(model, "feature_names_in_")
        else DEFAULT_FEATURES.copy()
    )

    if "StudentID" in features:
        raise ValueError(
            "El archivo modelo_gpa.pkl todavía fue entrenado con StudentID. "
            "Utiliza el modelo corregido con las 12 variables predictoras."
        )

    missing_expected = [
        feature for feature in DEFAULT_FEATURES if feature not in features
    ]
    unexpected = [
        feature for feature in features if feature not in DEFAULT_FEATURES
    ]

    if missing_expected or unexpected:
        raise ValueError(
            "Las variables del modelo no coinciden con la aplicación. "
            f"Faltantes: {missing_expected or 'ninguna'}. "
            f"No reconocidas: {unexpected or 'ninguna'}."
        )

    return model, features


def prepare_input(
    values: dict[str, int | float],
    feature_names: list[str],
) -> pd.DataFrame:
    """Create one prediction row in the exact order expected by the model."""

    frame = pd.DataFrame([values])

    missing = [
        feature for feature in feature_names if feature not in frame.columns
    ]
    if missing:
        raise ValueError(
            f"Faltan variables requeridas para generar la predicción: {missing}"
        )

    return frame[feature_names]


def predict_score(
    model: Any,
    feature_names: list[str],
    values: dict[str, int | float],
) -> float:
    """Predict and constrain the academic score to the dataset's 0–4 scale."""

    frame = prepare_input(values, feature_names)
    prediction = float(model.predict(frame)[0])
    return max(0.0, min(4.0, prediction))
