"""Módulo de mock de dados para os testes unitários."""

import random
import secrets
import string
from datetime import datetime

from dateutil.parser import parse


def gerar_float_aleatorio(min: float, max: float, casas_decimais: int = 3) -> float:
    """
    Gera um float CSPRNG (Pseudo Aleatório)

    Parameters
    ----------
    min : float
        Valor mínimo a ser gerado.
    max : float
        Valor máximo a ser gerado.

    Returns
    -------
    float
        Valor aleatório gerado.
    """
    generateSecrets = secrets.SystemRandom()
    f = generateSecrets.uniform(min, max)
    f = round(f, casas_decimais)

    return f


def gerar_inteiro_aleatorio(max: int) -> int:
    """
    Gera um inteiro CSPRNG (Pseudo Aleatório)

    Parameters
    ----------
    max : int
        Valor Máximo a ser gerado.

    Returns
    -------
    int
        Valor aleatório gerado.
    """
    i = secrets.randbelow(max)

    return i


def gerar_booleano_aleatorio() -> bool:
    """
    Gera um bool CSPRNG (Pseudo Aleatório).

    Returns
    -------
    bool
       Valor aleatório gerado.
    """
    b = secrets.choice([True, False])

    return b
