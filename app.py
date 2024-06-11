import os 
lista_atualizada = []
def main():
    Menu()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

def opcao_invalida():
    os.system('cls')
    main()

def cadastrar_clientes(lista_atualizada):
    nome = input("Digite o Nome do Restaurante: \n")
    categoria = input(f"Digite a Categoria do {nome}: \n")
    dados_restaurante = {'nome':nome,'categoria':categoria,'ativo': False}
    lista_atualizada.append(dados_restaurante) 
    print(f"{nome} foi Cadastrado com sucesso!")
    main()

def listar(lista_atualizada):
    for restaurante in lista_atualizada:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f"{nome_restaurante} | {categoria_restaurante} | {ativo}")
        main()
def estado(lista_atualizada):
    nome = input("Digite o Nome do Restaurante: \n")
    for restaurante in lista_atualizada:
        nome_restaurante = restaurante['nome']
        if nome == nome_restaurante:
            restaurante['ativo'] = not restaurante['ativo']
            print("o restaurante foi atividado com sucesso!" if restaurante['ativo'] else "O restaurante foi desativado com sucesso!"  )
            main()
        else:
            print("o restaurante não foi encontrado!")
def Menu():
    print("Sabor Express\n")
    print("1. Cadastro")
    print("2. Listar")
    print("3. Ativar Restaurante ")
    print("4. Sair \n")
    for escolha in range(1):
        try:
            escolha = int(input("Digite sua escolha: "))
            if escolha == 1:
                print("Cadastrar Restaurantes")
                cadastrar_clientes(lista_atualizada)
        
            elif escolha == 2:
                print("Listar Restaurantes")
                listar(lista_atualizada)
        
            elif escolha == 3:
                print("Ativar Restaurantes")
                estado(lista_atualizada)
        
            elif escolha == 4:
                finalizar_app()
            else:
                print("Numero Errado")
                input("Digite uma tecla para voltar ao menu principal: ")
                opcao_invalida()
        except:
            opcao_invalida()
if __name__ == '__main__':
    main()

