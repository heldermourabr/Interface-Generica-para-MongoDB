from modules.functions import Function

if __name__ == "__main__":   

    while True:
        
        print("[1] - Cadastrar multiplos clientes", "[2] - Cadastrar Cliente Individual", "[3] - Buscar Cliente por CPF", "[4] - Buscar Lista de clientes cadastrados", "[5] - Atualizar dados de cliente", "[6] - Excluir cadastro", "[0] - Fechar", sep = "\n")
        menu = input("Opção: ")

        if menu == "1":
            Function.cadastrar_clientes()
        
        elif menu == "2":
            Function.cadastrar_cliente()
        
        elif menu == "3":
            Function.buscar_cliente()
        
        elif menu == "4":
            Function.buscar_clientes()
        
        elif menu == "5":
            Function.atualizar_cliente()
        
        elif menu == "6":
            Function.excluir_cliente()
        
        elif menu == "0":
            break

        else:
            print("Opção Inválida")