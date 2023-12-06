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


formulario()    
with open("respostas.txt", "r") as respostas:
    print(respostas.read())   
