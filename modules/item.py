class Item:
    nome, cpf = "", ""

    def __init__(self, nome, cpf):
        try:
            self.nome = nome
            self.cpf = cpf
        except Exception as e:
            print(f"Error: {str(e)}")

    def set_nome(self, nome):
        self.nome = nome
    
    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def trazer_dicionario(self):
        return {"nome": self.get_nome(), "cpf": self.get_cpf()}