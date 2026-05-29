from agente_ucv.agent import explicar_concepto


def test_explicar_concepto_existente() -> None:
    resultado = explicar_concepto(" API ")

    assert resultado == {
        "status": "success",
        "explicacion": "Una API permite comunicacion entre sistemas.",
    }


def test_explicar_concepto_no_registrado() -> None:
    resultado = explicar_concepto("red neuronal")

    assert resultado == {
        "status": "not_found",
        "explicacion": "Concepto no registrado.",
    }
