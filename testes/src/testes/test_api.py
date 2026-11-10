# tests/test_api.py
 
def test_rota_saudacao_deve_retornar_sucesso_e_mensagem_correta(client):
    # Executa uma requisição GET simulada
    resposta = client.get('/api/saudacao')
    
    # Validações (Asserts puros do Pytest)
    assert resposta.status_code == 200
    assert resposta.json == {"mensagem": "Olá, Mundo!"}
 
def test_rota_soma_deve_calcular_valores_corretamente(client):
    # Executa uma requisição POST simulada enviando JSON
    payload = {"a": 5, "b": 10}
    resposta = client.post('/api/soma', json=payload)
    
    assert resposta.status_code == 200
    assert resposta.json == {"resultado": 15}