"""Mono-agente academico construido con Google ADK."""

from google.adk.agents.llm_agent import Agent


def explicar_concepto(concepto: str) -> dict:
    """Devuelve una explicacion simple para conceptos academicos basicos."""
    conceptos = {
        "api": "Una API permite comunicacion entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos.",
        "base de datos": "Una base de datos almacena informacion.",
    }

    concepto_normalizado = concepto.lower().strip()

    if concepto_normalizado in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto_normalizado],
        }

    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado.",
    }


root_agent = Agent(
    model="gemini-flash-latest",
    name="agente_ucv",
    description="Agente academico UCV",
    instruction="""
    Eres un asistente academico.
    Responde en espanol.
    Usa lenguaje simple.
    """,
    tools=[explicar_concepto],
)
