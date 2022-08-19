# python-bot-repository-tasks
python package responsible for storing and providing database services related to tasks that need persistence

```
from base_model.model_exemple import ModelExemple
from repository.RepositoryFromTask import RepositoryFromTask
from uuid import uuid4

""" Repositorío inicia uma conexão com o banco de dados e ja cria as tabelas baseado na model passada por parametro"""

repository = RepositoryFromTask(task_model=ModelExemple)

'''Salvando dados na tabela representada pela Model, os dados sempre devem ser um dicionario'''

data = {"token": "1517961|LEzkvaA09ACGzFSQAy1Vc3JGOcFXH6aiYVfm07cs", "id": uuid4(), "type": "TESTE"}
repository.save_data_task(data)


'''Buscando tarefa do banco de dados, caso não exista tarefa get_task retorna None para uma validação, caso uma exceção occora,
significará que a tarefa buscada não possui mais tentativas a serem feitas'''

try:
    task = repository.get_task()
    if not task:
        task = "deverá buscar uma tarefa da api"
except:
    retorno = "deverá retronar um erro de limite excedido para a api"

'''veja a representação da tarefa buscando os atributos dela'''

print(task.type)

'''Exclui instancia do banco de dados'''
repository.destroy_instance(task)

```