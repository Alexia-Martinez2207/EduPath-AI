from __future__ import annotations

from typing import Any


def classify_risk(score: float) -> dict[str, str]:
    """Convert the predicted score into a practical follow-up level."""

    if score < 2.0:
        return {
            "name": "Alto",
            "icon": "●",
            "css_class": "risk-high",
            "summary": (
                "El perfil requiere atención prioritaria. Las señales "
                "identificadas justifican una intervención cercana y medible."
            ),
        }

    if score < 3.0:
        return {
            "name": "Medio",
            "icon": "●",
            "css_class": "risk-medium",
            "summary": (
                "El perfil presenta oportunidades de mejora. Una intervención "
                "temprana puede prevenir una disminución del rendimiento."
            ),
        }

    return {
        "name": "Bajo",
        "icon": "●",
        "css_class": "risk-low",
        "summary": (
            "El perfil es favorable. Conviene conservar los apoyos actuales "
            "y mantener un seguimiento preventivo."
        ),
    }


def build_insights(
    absences: int,
    study_hours: float,
    tutoring: int,
    family_support: int,
    activities: int,
) -> tuple[list[str], list[str], list[str]]:
    """Generate transparent, rule-based strengths, alerts and actions."""

    strengths: list[str] = []
    alerts: list[str] = []
    actions: list[str] = []

    if absences <= 7:
        strengths.append("Mantiene un nivel favorable de asistencia.")
    elif absences >= 20:
        alerts.append("Presenta un nivel elevado de ausencias.")
        actions.append(
            "Revisar las causas del ausentismo durante la próxima semana."
        )
    elif absences >= 12:
        alerts.append("Presenta un nivel moderado de ausencias.")
        actions.append(
            "Activar un seguimiento quincenal de asistencia."
        )

    if study_hours >= 12:
        strengths.append("Dedica un tiempo favorable al estudio semanal.")
    elif study_hours < 5:
        alerts.append("Dedica poco tiempo al estudio semanal.")
        actions.append(
            "Crear un plan de estudio con metas semanales alcanzables."
        )

    if tutoring == 1:
        strengths.append("Cuenta con acompañamiento mediante tutorías.")
    else:
        alerts.append("Actualmente no recibe tutorías.")
        actions.append(
            "Evaluar su incorporación a un programa de tutorías."
        )

    if family_support >= 3:
        strengths.append("Cuenta con acompañamiento familiar favorable.")
    elif family_support <= 1:
        alerts.append("El acompañamiento familiar reportado es bajo.")
        actions.append(
            "Fortalecer la comunicación entre la institución y la familia."
        )

    if activities >= 2:
        strengths.append(
            "Participa activamente en actividades formativas."
        )

    if not actions:
        actions.append(
            "Mantener los apoyos actuales y realizar seguimiento mensual."
        )

    return strengths, alerts, actions


def build_edubot_message(result: dict[str, Any]) -> str:
    """Create a personalized interpretation without pretending to be a diagnosis."""

    risk = result["risk"]["name"]
    strengths = result["strengths"]
    alerts = result["alerts"]
    actions = result["actions"]
    score = result["score"]
    absences = result["absences"]
    study_hours = result["study_hours"]

    alert_text = (
        ", ".join(item.lower().rstrip(".") for item in alerts[:3])
        if alerts
        else "ninguna señal prioritaria"
    )

    strength_text = (
        ", ".join(item.lower().rstrip(".") for item in strengths[:2])
        if strengths
        else "sin fortalezas específicas identificadas"
    )

    primary_action = actions[0].rstrip(".").lower()

    if risk == "Alto":
        return (
            f"El promedio académico estimado es {score:.2f} de 4.00. "
            f"Las principales señales detectadas son {alert_text}. "
            f"El perfil registra {absences} ausencias y {study_hours:.1f} "
            f"horas semanales de estudio. La acción prioritaria es "
            f"{primary_action}. También conviene asignar una persona "
            f"responsable y una fecha concreta de revisión."
        )

    if risk == "Medio":
        return (
            f"El promedio académico estimado es {score:.2f} de 4.00. "
            f"Las señales que requieren seguimiento son {alert_text}. "
            f"Entre las fortalezas se encuentran {strength_text}. "
            f"Como siguiente paso, recomiendo {primary_action} y volver "
            f"a evaluar el perfil durante las próximas semanas."
        )

    return (
        f"El promedio académico estimado es {score:.2f} de 4.00. "
        f"Sus principales fortalezas son {strength_text}. "
        f"No se identificaron señales críticas. Se recomienda "
        f"{primary_action} para mantener una trayectoria favorable."
    )
