def responder_formulario():
    while True:
        nome = idade = genero = telefone = ""
        
        print("Insira as informações abaixo, digine 0 em Nome para voltar ao menu")

        try:
            nome = input("Nome: ").strip()

            while nome == "":
                nome = input("Por favor, insira um nome: ")

            if nome == "0":
                print("Encerrando o formulário")
                break

            idade = input("Idade: ").strip()

            while idade == "" or idade.isnumeric() == False:
                idade = input("Por favor, insira uma idade válida: ")

            genero = input("Gênero (M ou F): ").strip().upper()

            while genero not in ("M" , "F"):
                genero = input("Opção inválida, digite o gênero (M ou F): ").strip().upper()

            telefone = input("Telefone: ").strip()

            while telefone == "" or telefone.isnumeric() == False:
                telefone = input("Por favor, insira um telefone válido: ")

            with open("respostas.txt", "a") as respostas:
                respostas.write(f"{nome}|{idade}|{genero}|{telefone}\n")

        except:
            print("Ocorreu um erro, reiniciando formulário")

def imprime_dados(lista):

    for x in range(0, len(lista)):   
        print(f"\nNome: {lista[x][0]}")
        print(f"Idade: {lista[x][1]} anos")
        if lista[x][2] == 'M':
            print(f"Gênero: Masculino")
        else:
            print(f"Gênero: Feminino")
        print(f"Telefone: {lista[x][3]}\n")

def imprime_todas_respostas():
    with open ("respostas.txt", "r") as respostas:
        dados = respostas.read()
        lista_dados = []
        lista_respostas = dados.split("\n")
        if dados.strip() != "":
            for n in range(0, len(lista_respostas) - 1):
                lista_dados.append(lista_respostas[n].split('|'))

            imprime_dados(lista_dados)
        else:
            print("Ainda não houve respostas")
        

def busca_usuario_pelo_genero():
    try:
        genero = input("Digite o gênero que você quer pesquisar (M ou F): ").upper().strip()
        while genero not in ('M', 'F'):
            genero = input("Opção inválida, digite o gênero (M ou F): ")
    except:
        print("Ocorreu um erro")
    else:
        with open ("respostas.txt", "r") as respostas:
            dados = respostas.read()
            lista_genero = []
            lista_dados = []
            lista_respostas = dados.split("\n")

            if dados.strip() != "":    
                for n in range(0, len(lista_respostas) - 1):
                    lista_dados.append(lista_respostas[n].split('|'))
  
                for x in range(0, len(lista_dados)):
                    if lista_dados[x][2] == genero:
                        lista_genero.append(lista_dados[x])

                if len(lista_genero) > 0:               
                    imprime_dados(lista_genero)
                else:
                    print(f"Não há ninguém cadastrado com o gênero {genero}")
            else:
                print("Ainda não houve respostas")

def busca_usuario_pelo_nome():
    nome_procurado = input("Digite o nome que deseja procurar: ")
    while nome_procurado.strip() == "":
        nome_procurado = input("Por favor, digite um nome para iniciar a busca")        

    with open("respostas.txt", "r") as respostas:
        dados = respostas.read()
        lista_nomes = []
        lista_dados = []
        lista_respostas = dados.split("\n")

        if dados.strip() != "":
            for n in range(0, len(lista_respostas) - 1):
                lista_dados.append(lista_respostas[n].split('|'))

            for x in range(0, len(lista_dados)):
                if nome_procurado.upper() in lista_dados[x][0].upper():
                    lista_nomes.append(lista_dados[x])

            if len(lista_nomes) > 0:
                imprime_dados(lista_nomes)
            else:
                print(f"Não há ninguém cadastrado com esse nome")
        else:
            print("Ainda não houveram respostas")

def interface():
    while True:
        selecao = 0

        try:
            print("Bem vindo ao programa! Escolha uma das seguintes opções:")
            selecao = int(input("1 - Responder formulário\n2 - Imprimir usuários cadastrados\n3 - Buscar usuário pelo gênero\n4 - Buscar usuário pelo nome\n5 - Fechar programa\n"))
            
            while selecao not in (1, 2, 3, 4, 5):
                selecao = int(input("Por favor, selecione uma das opções abaixo:\n1 - Responder formulário\n2 - Imprimir usuários cadastrados\n3 - Buscar usuário pelo gênero\n4 - Buscar usuário pelo nome\n5 - Fechar programa\n"))
            
        except:
            print("Ocorreu um erro")

        else:
            if selecao == 1:
                responder_formulario()
            elif selecao == 2:
                imprime_todas_respostas()
            elif selecao == 3:
                busca_usuario_pelo_genero()
            elif selecao == 4:
                busca_usuario_pelo_nome()
            elif selecao == 5:
                print("Fechando o programa")
                break

interface()