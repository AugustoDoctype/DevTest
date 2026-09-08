import pytest
from seguranca import validar_senha

def test_senha_valida():
    assert validar_senha("senha123") == True

@pytest.mark.parametrize("senha_invalida", [
    "sh1",             
    "senhasemnumero",  
    "",                
    12345678           
])
def test_senhas_invalidas_lancam_excecao(senha_invalida):
    print(f"\n[Testando senha com erro esperada]: {senha_invalida}")
    
    with pytest.raises(ValueError):
        validar_senha(senha_invalida)