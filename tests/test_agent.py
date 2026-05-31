from agente_ucv.agent import calcular_promedio, explicar_concepto

# Pruebas para la herramienta explicar_concepto.
def test_explicar_concepto_existente() -> None:
    resultado = explicar_concepto(" API ")
    assert resultado == {
        "status": "success",
        "explicacion": "Una API permite comunicacion entre sistemas.",
    }

def test_explicar_concepto_nuevo() -> None:
    resultado = explicar_concepto(" IDempotencia ")
    assert resultado == {
        "status": "success",
        "explicacion": "La idempotencia permite repetir una operacion sin cambiar el resultado final.",
    }

def test_explicar_concepto_no_registrado() -> None:
    resultado = explicar_concepto("red neuronal")
    assert resultado == {
        "status": "not_found",
        "explicacion": "Concepto no registrado.",
    }

def test_explicar_concepto_vacio() -> None:
    resultado = explicar_concepto("   ")
    assert resultado == {
        "status": "error",
        "explicacion": "El concepto no puede estar vacio.",
    }

def test_explicar_concepto_tipo_incorrecto() -> None:
    resultado = explicar_concepto(123)
    assert resultado == {
        "status": "error",
        "explicacion": "El concepto debe ser un texto.",
    }

# Pruebas para la herramienta calcular_promedio.
def test_calcular_promedio_correcto() -> None:
    resultado = calcular_promedio([18, 16, 15])
    assert resultado == {
        "status": "success",
        "promedio": 16.33,
        "mensaje": "Promedio calculado correctamente.",
    }

def test_calcular_promedio_lista_vacia() -> None:
    resultado = calcular_promedio([])
    assert resultado == {
        "status": "error",
        "promedio": None,
        "mensaje": "La lista de notas no puede estar vacia.",
    }

def test_calcular_promedio_tipo_incorrecto() -> None:
    resultado = calcular_promedio("18,16,15")
    assert resultado == {
        "status": "error",
        "promedio": None,
        "mensaje": "Las notas deben enviarse en una lista.",
    }

def test_calcular_promedio_nota_no_numerica() -> None:
    resultado = calcular_promedio([18, "dieciseis", 15])
    assert resultado == {
        "status": "error",
        "promedio": None,
        "mensaje": "Todas las notas deben ser numeros.",
    }

def test_calcular_promedio_booleano_no_valido() -> None:
    resultado = calcular_promedio([18, True, 15])
    assert resultado == {
        "status": "error",
        "promedio": None,
        "mensaje": "Todas las notas deben ser numeros.",
    }

def test_calcular_promedio_fuera_de_rango() -> None:
    resultado = calcular_promedio([12, 25])
    assert resultado == {
        "status": "error",
        "promedio": None,
        "mensaje": "Las notas deben estar entre 0 y 20.",
    }
