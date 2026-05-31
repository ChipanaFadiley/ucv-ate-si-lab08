"""Mono-agente academico construido con Google ADK."""

from numbers import Real
try:
    from google.adk.agents.llm_agent import Agent  # type: ignore[reportMissingImports]
except ImportError:
    class Agent:
        """Fallback Agent stub when google.adk is unavailable."""

        def __init__(self, *args, **kwargs):
            self.config = {"args": args, "kwargs": kwargs}

        def __repr__(self):
            return "Agent(dummy)"

conceptos_7 = {
    "api": "Una API permite comunicacion entre sistemas.",
    "algoritmo": "Un algoritmo es una secuencia de pasos.",
    "base de datos": "Una base de datos almacena informacion.",
    # nuevos conceptos
    "idempotencia": "La idempotencia permite repetir una operacion sin cambiar el resultado final.",
    "serializacion": "La serializacion convierte datos u objetos a un formato que se puede guardar o enviar.",
    "concurrencia": "La concurrencia permite que varias tareas progresen durante el mismo periodo de tiempo.",
    "latencia": "La latencia es el tiempo que tarda un sistema en responder a una solicitud.",
    "hash": "Un hash es una huella digital generada a partir de datos de entrada.",
}


def explicar_concepto(concepto: str) -> dict:
    """Verificación de Entrada"""
    if not isinstance(concepto, str):
        return {
            "status": "error",
            "explicacion": "El concepto debe ser un texto.",
        }

    concepto_normalizado = concepto.lower().strip()

    if not concepto_normalizado:
        return {
            "status": "error",
            "explicacion": "El concepto no puede estar vacio.",
        }

    if concepto_normalizado in conceptos_7:
        return {
            "status": "success",
            "explicacion": conceptos_7[concepto_normalizado],
        }

    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado.",
    }


def calcular_promedio(notas: list[float]) -> dict:
    """Calcula el promedio de una lista de notas."""
    if not isinstance(notas, list):
        return {
            "status": "error",
            "promedio": None,
            "mensaje": "Las notas deben enviarse en una lista.",
        }

    if not notas:
        return {
            "status": "error",
            "promedio": None,
            "mensaje": "La lista de notas no puede estar vacia.",
        }

    # Validacion sencilla para evitar promedios con textos o valores fuera de rango.
    for nota in notas:
        if isinstance(nota, bool) or not isinstance(nota, Real):
            return {
                "status": "error",
                "promedio": None,
                "mensaje": "Todas las notas deben ser numeros.",
            }

        if nota < 0 or nota > 20:
            return {
                "status": "error",
                "promedio": None,
                "mensaje": "Las notas deben estar entre 0 y 20.",
            }

    promedio = round(sum(notas) / len(notas), 2)

    return {
        "status": "success",
        "promedio": promedio,
        "mensaje": "Promedio calculado correctamente.",
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
    tools=[explicar_concepto, calcular_promedio],
)
