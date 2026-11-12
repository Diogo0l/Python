from seguranca import gerar_hash_senha, verificar_senha

SENHA = "Senhaforte123"

def test_mesma_senha_gerando_hash_diferente():
    
    hash1 = salt_1 = gerar_hash_senha(SENHA)
    hash2 = salt_2 = gerar_hash_senha(SENHA)
    
    assert hash1 != hash2
    assert salt_1 != salt_2
    
def test_senha_correta_e_aceita():
    hash_salvo, salt_salvo = gerar_hash_senha(SENHA)
    
    assert verificar_senha(SENHA, hash_salvo, salt_salvo) is True
    
def test_senha_incorreta_e_rejeitada():
    hash_salvo, salt_salvo = gerar_hash_senha(SENHA)
    
    assert verificar_senha("SenhaErrada", hash_salvo, salt_salvo) is False