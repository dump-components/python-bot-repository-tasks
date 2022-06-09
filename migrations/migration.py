class Migration:
    
    @staticmethod
    def make(database, model):
        database.create_tables(models=[model])