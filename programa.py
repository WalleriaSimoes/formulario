def formulario():
    while True:
        nome = idade = genero = telefone = ""
        
        print("Insira as informações abaixo, digine 0 em Nome para encerrar o programa")

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

def imprimeDados():
    with open ("respostas.txt", "r") as respostas:
        dados = respostas.read()
        lista_dados = []
        lista_respostas = dados.split("\n")
        for n in range(0, len(lista_respostas)):
            lista_dados.append(lista_respostas[n].split('|'))
        for x in range(0, len(lista_dados)):
            print(f"\nNome: {lista_dados[x][0]}")
            print(f"Idade: {lista_dados[x][1]} anos")
            if lista_dados[x][2] == 'M':
                print(f"Gênero: Masculino")
            else:
                print(f"Gênero: Feminino")
            print(f"Telefone: {lista_dados[x][3]}\n")

formulario()    
imprimeDados()  