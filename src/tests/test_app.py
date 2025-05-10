import pytest # Traz a biblioteca de testes
import time # Manipular tempo
from src.model.colaborador_model import Colaborador
from src.app import create_app

#-------------------------CONFIGURAÇÕES PARA O TESTE--------------------------------

@pytest.fixture # Identificar funções de configurações para o teste
def app():
    app = create_app()
    yield app
    
@pytest.fixture
def client(app):
    return app.test_client()

#------------------------------------------------------------------------------------

def test_pegar_todos_colaboradores(client): # assim como o arquivo tem que começar com teste, as unçoes tem que começar com test.
    resposta = client.get('/colaborador/todos-colaboradores')

    assert resposta.status_code == 200
    assert  isinstance(resposta.json, list)

def test_desempenho_requisicao_get(client):
    comeco = time.time() # pega a hora atual e transforma em segundos

    for _ in range (100): # _ omitir a variavel auxiliar
        resposta = client.get('/colaborador/todos-colaboradores')

    fim = time.time() - comeco

    assert fim < 0.2 # segundos