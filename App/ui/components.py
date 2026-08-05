from __future__ import annotations

import streamlit as st

from ui.styles import html


def render_feature_card(icon: str, title: str, body: str) -> None:
    html(
        f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """
    )


def render_page_header(label: str, title: str, subtitle: str) -> None:
    html(
        f"""
        <div class="page-label">{label}</div>
        <div class="page-title">{title}</div>
        <div class="page-subtitle">{subtitle}</div>
        """
    )


def render_result_summary(result: dict) -> None:
    html(
        f"""
        <div class="result-grid">
            <div class="score-card">
                <div class="score-label">
                    Promedio académico estimado
                </div>

                <div class="score-value">
                    {result["score"]:.2f}
                </div>

                <div class="score-scale">
                    Escala académica de 0.00 a 4.00
                </div>

                <div class="risk-pill {result["risk"]["css_class"]}">
                    {result["risk"]["icon"]}&nbsp;
                    Nivel de riesgo {result["risk"]["name"].lower()}
                </div>
            </div>

            <div class="summary-card">
                <h3>Lectura del perfil</h3>
                <p>{result["risk"]["summary"]}</p>
            </div>
        </div>
        """
    )


def render_insight(item: str, kind: str) -> None:
    symbol = "✓" if kind == "strength" else "!"
    html(
        f"""
        <div class="insight-card">
            <strong>{symbol}</strong>&nbsp; {item}
        </div>
        """
    )


def render_action(index: int, action: str) -> None:
    html(
        f"""
        <div class="action-card">
            <div class="action-number">{index}</div>

            <div>
                <strong>{action}</strong><br>
                <span style="color:#69758C;font-size:.87rem;">
                    Acción sugerida para seguimiento institucional.
                </span>
            </div>
        </div>
        """
    )


def render_edubot(message: str) -> None:
    html(
        f"""
        <div class="edubot">
            <div class="edubot-tag">
                ✦ Asistente de interpretación
            </div>

            <h3>EduBot</h3>
            <p>{message}</p>
        </div>
        """
    )
