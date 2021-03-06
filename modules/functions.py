from modules.conector_mongo import Conexao
from modules.item import Item

class Function:    
    
    def cadastrar_clientes():
        teste_cliente = Conexao()           
        lista = []
        while True:   
            try:     
                selecao = input("Cadastrar outro cliente? Y/N ").upper()
                if selecao == "Y":       
                    cliente1 = Item(input("nome: ").title(), input("cpf: ")).trazer_dicionario()
                    lista.append(cliente1)
            except Exception as e:
                print(str(e))
        
            if selecao == "N":
                try:
                    teste_cliente.collection.insert_many(lista)
                    print("Clientes cadastrados com Sucesso: ")
                    break
                except Exception as e:
                    print(str(e))

    def cadastrar_cliente():
        teste_cliente = Conexao()
        try:
            cliente1 = Item(input("nome: ").title(), input("cpf: ")).trazer_dicionario()
            teste_cliente.collection.insert_one(cliente1)
        except Exception as e:
            print(str(e))


    def buscar_cliente():
        teste_cliente = Conexao()
        try:
            cpf = input("cpf: ")
            filtro = { 'cpf': str(cpf) }
            excluir = teste_cliente.collection.find_one(filtro)
            print("Cliente encontrado", f"CLiente: {excluir['nome']}", f"CPF: {excluir['cpf']}", sep = "\n")

        except Exception as e:
            print(str(e))

    def buscar_clientes():
        teste_cliente = Conexao()
        try:
            clientes = []
            item_details = teste_cliente.collection.find()
            for cliente in item_details:
                nome = cliente['nome']
                cpf = cliente['cpf']
                ind = Item(nome, cpf)
                clientes.append(ind)

            for cliente in clientes:        
                print(f"Nome: {cliente.get_nome()}   ||   CPF: {cliente.get_cpf()}")
                print("-----------------------------------------------------------------")
        except Exception as e:
            print(str(e))

    def atualizar_cliente():
        teste_cliente = Conexao()
        try:
            # item_details = teste_cliente.collection.find()
            # op????o = input("Qual a inform????o vc deseja alterar: ").upper()
            # if op????o == "CPF":
            #     nome = input("Nome do cliente: ").title()
            #     for cliente in item_details:
            #         if nome == cliente['nome']:
            #             cpf = input("Informe o novo cpf: ")
            #             filtro = { 'nome': str(nome) }
            #             novo_cpf = { "$set": { 'cpf': str(cpf) } }
            #             teste_cliente.collection.update_one(filtro, novo_cpf)
            #             print("Altera????o cadastrada com Sucesso!")
            #             break
        
            item_details = teste_cliente.collection.find()
            op????o = input("Qual a inform????o vc deseja alterar: ").upper()
            if op????o == "CPF":
                nome = input("Nome do cliente: ").title()
                for cliente in item_details:
                    if nome == cliente['nome']:
                        cpf = input("Informe o novo cpf: ")
                        filtro = { 'nome': str(nome) }
                        novo_cpf = { "$set": { 'cpf': str(cpf) } }
                        teste_cliente.collection.update_one(filtro, novo_cpf)
                        print("Altera????o cadastrada com Sucesso!")
                        break


                        
            elif op????o == "NOME":
                try:
                    nao_existe = True                                            
                    cpf = input("CPF do cliente: ")
                    for cliente in item_details:
                        if cpf == cliente['cpf']:                        
                            nome = input("Informe o novo nome: ").title()
                            filtro = { 'cpf': str(cpf) }
                            novo_nome = { "$set": { 'nome': str(nome) } }
                            teste_cliente.collection.update_one(filtro, novo_nome)
                            print("Altera????o cadastrada com Sucesso!\n")
                            nao_existe = False
                        elif cpf != cliente['cpf']:
                            continue
                    if nao_existe:
                        print("CPF n??o encontrado\n")
                        
                        # cpf = input("CPF do cliente: ")
                        # for cliente in item_details:
                        #     if cpf == cliente['cpf']:                        
                        #         nome = input("Informe o novo nome: ").title()
                        #         filtro = { 'cpf': str(cpf) }
                        #         novo_nome = { "$set": { 'nome': str(nome) } }
                        #         teste_cliente.collection.update_one(filtro, novo_nome)
                        #         print("Altera????o cadastrada com Sucesso!")
                        #         break
                        #     else:
                        #         print("CPF n??o encontrado\n")                                
                except Exception as e:
                    print(str(e))
        
        except Exception as e:
            print(str(e))

    def excluir_cliente():
        teste_cliente = Conexao()
        while True:
            try:                
                cpf = input("CPF do cliente: ")
                filtro = { 'cpf': str(cpf) }
                excluir = teste_cliente.collection.find_one(filtro)
                print("Tem certeza que deseja excluir o cliente", f"CLiente: {excluir['nome']}", f"CPF: {excluir['cpf']}", sep = "\n")
                escolha = input("Y/N: ").upper()
                if escolha == "Y":
                    teste_cliente.collection.delete_one(filtro)
                    print("Cadastro exclu??do com sucesso!")
                    break
                elif escolha == "N":
                    print("Nenhum cadastro foi deletado!")                        
                    break
                else:
                    print("Op????o inv??lida, por seguran??a comece novamente.")
                    break
            except Exception as e:
                print(str(e))
            
            