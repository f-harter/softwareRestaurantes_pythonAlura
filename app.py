import os
restaurantes = [{'nome':'Pizzaria','categoria':'pizza', 'ativo':False},{'nome':'Hamburgueria','categoria':'hamburguer', 'ativo':True},{'nome':'Sorveteria','categoria':'sorvete', 'ativo':False}]

def exibir_nome_do_programa_():
    '''Essa função exibe o nome do programa'''
    print("""[̲̅q̲̅][̲̅u̲̅][̲̅i̲̅][̲̅c̲̅][̲̅k̲̅] [̲̅d̲̅][̲̅e̲̅][̲̅l̲̅][̲̅i̲̅][̲̅v̲̅][̲̅e̲̅][̲̅r̲̅][̲̅y̲̅] [̲̅a̲̅][̲̅p̲̅][̲̅p̲̅]
    """)

def exibir_opcoes():
    '''Essa função exibe o menu de opções'''
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurante')
    print ('3. Alternar Estado do Restaurante')
    print ('4. Sair\n')

def finalizar_app():
    '''Essa função finaliza o app'''
    os.system('clear')
    exibir_subtitulo('Finalizando aplicação...')

def opcao_invalida():
    '''Essa função indica uma opção invalida'''
    print('Opção inválida. Tente novamente.\n')
    voltar_menu()

def exibir_subtitulo(texto):
    '''Essa função exibe o subtítulo'''
    os.system('cls')
    linha = '*'*(len(texto))
    print(linha)
    print(texto)
    print(f'{linha} \n')

def voltar_menu():
    '''Essa função volta ao menu'''
    input('Pressione enter para voltar ao menu...')
    main()

def cadastrar_restaurante():
    '''Essa função é responsável a cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastrando Restaurante\n')
    restaurante = (input('Digite o nome do restaurante que deseja cadastrar: '))
    categoria = input(f'Digite a categoria do {restaurante}: ')
    dados_do_restaurante = {'nome': restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)

    print('Restaurante cadastrado com sucesso.')
    voltar_menu()

def listar_restaurantes():
    '''Essa função lista os restaurantes cadastrados'''
    exibir_subtitulo('Listando Restaurantes')
    print(f'{"Nome do restaurante".ljust(21)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        atividade_restaurante = 'Ativado' if restaurante['ativo'] else 'Inativo'
        print(f'-{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {atividade_restaurante}')
    voltar_menu()

def alternar_estado_restaurante():
    '''Essa função alterna o estado do restaurante'''
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_menu()

def escolher_opcao():
    '''Essa função escolhe a opção desejada'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida ==  1:
            cadastrar_restaurante()
        elif opcao_escolhida ==  2:
            listar_restaurantes()
        elif opcao_escolhida ==  3:
            alternar_estado_restaurante()
        elif opcao_escolhida ==  4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é o menu principal'''
    os.system('cls')
    exibir_nome_do_programa_()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()