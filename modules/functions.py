from modules.conector_mongo import Conexao
from modules.item import Item

class Function:    

    while True:
        def cadastrar_clientes():
            teste = Conexao()            
            lista = []
            while True:   
                try:     
                    selecao = input("Digite opção: ")
                    if selecao == "1":       
                        cliente1 = Item(input("nome: "), input("cpf: ")).trazer_dicionario()
                        lista.append(cliente1)
                except Exception as e:
                    print(str(e))
            
                if selecao == "2":
                    try:
                        teste.collection.insert_many(lista)
                        print("Clientes cadastrados com Sucesso: ")
                        break
                    except Exception as e:
                        print(str(e))

        def cadastrar_cliente():
            teste = Conexao()
            try:
                cliente1 = Item(input("nome: ").title(), input("cpf: ")).trazer_dicionario()
                teste.collection.insert_one(cliente1)
            except Exception as e:
                print(str(e))


        def buscar_cliente():
            teste = Conexao()
            try:
                cpf = input("cpf: ")
                filtro = { 'cpf': str(cpf) }
                excluir = teste.collection.find_one(filtro)
                print("Cliente encontrado", f"CLiente: {excluir['nome']}", f"CPF: {excluir['cpf']}", sep = "\n")

            except Exception as e:
                print(str(e))

        def buscar_clientes():
            teste = Conexao()
            try:
                clientes = []
                item_details = teste.collection.find()
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
            teste = Conexao()
            try:
                item_details = teste.collection.find()
                opção = input("Qual a informção vc deseja alterar: ").upper()
                if opção == "CPF":
                    nome = input("Nome do cliente: ").title()
                    for cliente in item_details:
                        if nome == cliente['nome']:
                            cpf = input("Informe o novo cpf: ")
                            filtro = { 'nome': str(nome) }
                            novo_cpf = { "$set": { 'cpf': str(cpf) } }
                            teste.collection.update_one(filtro, novo_cpf)
                            print("Alteração cadastrada com Sucesso!")
                            break
            
                            
                elif opção == "NOME":
                    try:
                        while True:
                            cpf = input("CPF do cliente: ")
                            for cliente in item_details:
                                if cpf == cliente['cpf']:                        
                                    nome = input("Informe o novo nome: ").title()
                                    filtro = { 'cpf': str(cpf) }
                                    novo_nome = { "$set": { 'nome': str(nome) } }
                                    teste.collection.update_one(filtro, novo_nome)
                                    print("Alteração cadastrada com Sucesso!")
                                    break
                                else:
                                    print("CPF não encontrado\n")                                
                    except Exception as e:
                        print(str(e))
            
            except Exception as e:
                print(str(e))

        def excluir_cliente():
            teste = Conexao()
            while True:
                try:                
                    cpf = input("CPF do cliente: ")
                    filtro = { 'cpf': str(cpf) }
                    excluir = teste.collection.find_one(filtro)
                    print("Tem certeza que deseja excluir o cliente", f"CLiente: {excluir['nome']}", f"CPF: {excluir['cpf']}", sep = "\n")
                    escolha = input("Y/N: ").upper()
                    if escolha == "Y":
                        teste.collection.delete_one(filtro)
                        print("Cadastro excluído com sucesso!")
                        break
                    elif escolha == "N":
                        print("Nenhum cadastro foi deletado!")                        
                        break
                    else:
                        print("Opção inválida, por segurança comece novamente.")
                        break
                except Exception as e:
                    print(str(e))
            
            