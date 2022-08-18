from base_model.model_exemple import ModelExemple
from repository.RepositoryFromTask import RepositoryFromTask

repository = RepositoryFromTask()
RepositoryFromTask.create_table(repository.database, ModelExemple)
