# Laboratorio ADK UCV

Mono-agente academico construido con Python, Google ADK y Poetry para el
laboratorio de Sistemas Inteligentes.

## Requisitos

- Python 3.10 o superior
- Poetry
- Cuenta de Google AI Studio o API key compatible con Google ADK

## Instalacion

```powershell
poetry install
```

Crear un archivo `.env` en la raiz del proyecto con la variable:

```env
GOOGLE_API_KEY="TU_API_KEY"
```

## Estructura

```text
agente_ucv/
  __init__.py
  agent.py
tests/
  test_agent.py
.github/workflows/
  sonarqube.yml
pyproject.toml
README.md
```

## Ejecucion del agente

Desde la raiz del proyecto:

```powershell
poetry run adk run agente_ucv
```

Tambien se puede abrir la interfaz web:

```powershell
poetry run adk web --port 8000
```

Luego ingresar a `http://localhost:8000`.

## Pruebas

```powershell
poetry run pytest
```

## Calidad con SonarQube / SonarCloud

El proyecto incluye un workflow de GitHub Actions en
`.github/workflows/sonarqube.yml`. Para ejecutarlo en GitHub se debe configurar
el secreto `SONAR_TOKEN` en el repositorio.

Tambien se incluye `sonar-project.properties` con la clave y organizacion del
proyecto en SonarCloud.

## Agente

El agente `agente_ucv` responde en espanol con lenguaje simple y expone la tool
`explicar_concepto`, que reconoce los conceptos basicos `api`, `algoritmo` y
`base de datos`.
