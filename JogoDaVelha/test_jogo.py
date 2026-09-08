import pytest
from jogo import avaliar_jogo_da_velha

@pytest.mark.parametrize("tabuleiro, status_esperado", [
    
    pytest.param(
        [["X", "X", "X"],
         ["O", None, "O"],
         [None, None, None]], 
        "Vitória de X", 
        id="Vitoria_do_X_na_primeira_linha"
    ),
    
    pytest.param(
        [["O", "X", None],
         ["O", "X", None],
         ["O", None, "X"]], 
        "Vitória de O", 
        id="Vitoria_do_O_na_primeira_coluna"
    ),
      
    pytest.param(
        [["X", "O", "O"],
         [None, "X", None],
         [None, None, "X"]], 
        "Vitória de X", 
        id="Vitoria_do_X_na_diagonal_principal"
    ),
      
    pytest.param(
        [["X", "O", "X"],
         ["X", "O", "O"],
         ["O", "X", "X"]], 
        "Empate", 
        id="Empate_deu_velha_sem_vencedor"
    ),
      
    pytest.param(
        [["X", "O", None],
         [None, "X", None],
         [None, None, "O"]], 
        "Em andamento", 
        id="Jogo_no_meio_do_caminho"
    ),

])
def test_status_do_tabuleiro(tabuleiro, status_esperado):
    assert avaliar_jogo_da_velha(tabuleiro) == status_esperado

def test_tabuleiro_tamanho_invalido():
    with pytest.raises(ValueError, match="O tabuleiro deve ser uma matriz 3x3"):
        avaliar_jogo_da_velha([["X", "O"], ["O", "X"]])