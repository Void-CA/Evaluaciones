import sys
import os

# Asegura que la carpeta "evaluaciones" esté en el path de Python
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from ejercicios.ordenar import ordenar_lista


def test_ordenar_lista():
    assert ordenar_lista([3, 1, 2]) == [1, 2, 3]
    assert ordenar_lista([]) == []
    assert ordenar_lista([5, -1, 4]) == [-1, 4, 5]
