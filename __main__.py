from modules.conetor_mongo import Conexao
from modules.functions import Functions

if __name__ == "__main__":
        
    while True:
        print("[1] - Cadastrar multiplos clientes", "[2] - Cadastrar Cliente Individual", "[3] - Buscar Cliente por CPF", "[4] - Buscar Lista de clientes cadastrados", "[5] - Atualizar dados de cliente", "[6] - Excluir cadastro", "[0] - Fechar", sep = "\n")
        menu = input("Opção: ")

        if menu == "1":
            Functions.cadastrar_clientes()
        
        elif menu == "2":
            Functions.cadastrar_cliente()
        
        elif menu == "3":
            Functions.buscar_cliente()
        
        elif menu == "4":
            Functions.buscar_clientes()
        
        elif menu == "5":
            Functions.atualizar_cliente()
        
        elif menu == "6":
            Functions.excluir_cliente()
        
        elif menu == "0":
            break

        else:
            print("Opção Inválida")