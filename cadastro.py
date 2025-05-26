import re

print('\nATIVIDADE CRUD\n')

def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Giovana Budri Oliveira           RA:25017683                |')
    print('| Matheus Barbosa                  RA:25001218                |')
    print('| Versão 2.0 de 24/maio/2025                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')


#Solicita entrada de texto até que seja válido
def umTexto (solicitacao, mensagem, valido):
    while True:
        txt=input(solicitacao)
        if txt not in valido:
            print(mensagem,' - Favor redigitar')
        else:
            break
    return txt

#Faz uma lista com as opções disponíveis --> Exibe menu numerado com as opções
def opcaoEscolhida(mnu):
    print()

    opcoesValidas = []
    for p, opcao in enumerate(mnu):
        print(f"{p+1}) {opcao}")
        opcoesValidas.append(str(p+1))

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

#Busca binária para encontrar o nome na agenda
def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1
    
    while inicio <= final:
        meio = (inicio + final) // 2
        if agd[meio] == nom:
            #True = Nome encontrado/Meio =  posição que ele está
            return [True, meio]
        elif agd[meio] < nom:
            inicio = meio + 1
        else:
            final = meio - 1

    #False = nome não encontrado/Inicio = posição que ele deveria estar
    return [False, inicio]

#Cadastro dos contatos
def cadastrar(agd):
    #Validação RegEx
    nome_regex = re.compile(r'^[A-Z][a-z]*(?: (?:[A-Z][a-z]*|de|da|do|dos|das))*$')
    telefone_regex = re.compile(r'^(?:\([1-9]{2}\) )?9?[0-9]{4}-[0-9]{4}$') 
    celular_regex = re.compile(r'^\(?(\d{2})\)?\s?9\d{4}-?\d{4}$')
    email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

    while True:
        nome = input('Digite nome (ou CANCELAR para desistir): ').strip()
        if nome.upper() == 'CANCELAR':
            print('\n\033[33mOpção cancelada!\033[m')
            return
        
        #Se dar match = aceita
        if not nome_regex.match(nome):
            print('Nome inválido. Por favor, digite um nome completo (apenas letras (iniciais maiúsculas) e espaços)')
            continue

        achou, posicao = ondeEsta(nome, [p[0] for p in agd])  
        if achou:
            print('Nome já cadastrado. Por favor, digite outro')
        else:
            break

    while True:    
        aniversario = input('Data de aniversário (formato DD/MM): ').strip()
    
        if len(aniversario) == 5 and aniversario[2] == '/':
            dia = aniversario[:2]
            mes = aniversario[3:]
        
            if dia.isdigit() and mes.isdigit():
                dia = int(dia)
                mes = int(mes)
            
                if mes < 1 or mes > 12:
                    print('Mês inválido.')
                    continue
                
                if mes == 2 and dia > 28:
                    print('Tente novamente, fevereiro vai até dia 28.')
                    continue
                elif mes in [4, 6, 9, 11] and dia > 30:
                    print('Tente novamente, o mês escolhido vai até dia 30.')
                    continue
                elif dia < 1 or dia > 31:
                    print('Dia inválido.')
                    continue
                break
            else:
                print('Dia ou mês não são números')
        else:
            print('Data inválida. Por favor, digite no formato DD/MM e com valores reais')

    while True:
        endereco = input('Endereço: ').strip()
        if any(c.isalpha() for c in endereco) and any(c.isdigit() for c in endereco):
            break
        else:
            print('Endereço inválido. Deve conter letras e números')

    while True:
        telefone = input('Telefone fixo: ').strip()
        match = telefone_regex.match(telefone)
        if match:
            break
        else:
            print('Número inválido. Utilieze --> () caso opte por colocar DDD e uso obrigatório de hífen --> -')

    while True:
        celular = input('Celular (com DDD obrigatório): ').strip()
        match = celular_regex.match(celular)
        if match:
            ddd = int(match.group(1))
            if 11 <= ddd <= 99:
                break
            else:
                print('DDD inválido.')
        else:
            print('Número inválido. Deve conter DDD e mais 9 dígitos (começando com 9).')
        
    while True:
        email = input('Email: ').strip()
        if email_regex.match(email):
            break
        else:
            print('Email inválido')

    #Criação da listinha 'contatos'
    contato = [nome, aniversario, endereco, telefone, celular, email]
    #Insere na agd (listona) o novo contato criado na posição 'posicao'
    agd.insert(posicao, contato)

    print('\n\033[32mCadastro realizado com sucesso!\033[m')

#Procurar contato -- Usa função ondeEsta
def procurar(agd):
    if not agd:
        print('\n\033[33mAgenda vazia --> Nenhum contato cadastrado para procurar\033[m')
        return
    
    nome = input('Digite o nome do contato a ser procurado (ou CANCELAR para desistir): ').strip()
    if nome.upper() == 'CANCELAR':
        print('\n\033[33mOpção cancelada!\033[m')
        return
   
    #Achou = True/False
    #Posicao = Meio/Início
    #ondeEsta --> Nome é a primeira informação de contato (contato[0])
    #Busca nos contatos o nome dado pelo usuário
    achou, posicao = ondeEsta(nome, [contato[0] for contato in agd])  
    if achou:
        contato = agd[posicao]
        print(f'\n\033[32mContato encontrado!\033[m')
        print(f'Nome: {contato[0]}')
        print(f'Aniversário: {contato[1]}')
        print(f'Endereço: {contato[2]}')
        print(f'Telefone: {contato[3]}')
        print(f'Celular: {contato[4]}')
        print(f'E-mail: {contato[5]}')
    else:
        print('\n\033[33mContato não encontrado, retornando ao menu\033[m')

    #Usamos umTexto para perguntar se o usuário quer fazer nova busca
        nova_busca = umTexto('\nDeseja procurar outro contato? [S/N]: ', 'Digite S ou N', ['S', 'N'])
        if nova_busca == 'N':
            print('\n\033[33mEncerrando procura\033[m')
            return


#Atualizar contato -- Usa função ondeEsta
def atualizar(agd):
    #Agenda vazia = lista vazia = False
    if not agd:
        print('\n\033[33mAgenda vazia --> Nenhum cadastro para atualizar\033[m')
        return
    
    nome = input('Digite o nome do contato a ser atualizado (ou CANCELAR para desistir): ').strip()
    if nome.upper() == 'CANCELAR':
        print('\n\033[33mOpção cancelada!\033[m')
        return
    
    #Busca o contato pelo nome na agenda usando busca binária
    achou, posicao = ondeEsta(nome, [contato[0] for contato in agd])
    #If not achou = False
    if not achou:
        print('\n\033[33mContato não encontrado, retornando ao menu\033[m')
        return

    #A variável contato recebe a listinha com os dados do contato que está na posição 'posicao' dentro da listona principal 'agd'
    contato = agd[posicao]
    print(f"\n\033[32mContato encontrado!\033[m --> {contato[0]}\n")

    #Validação RegEx
    telefone_regex = re.compile(r'^(?:\([1-9]{2}\) )?9?[0-9]{4}-[0-9]{4}$')
    celular_regex = re.compile(r'^\(?(\d{2})\)?\s?9\d{4}-?\d{4}$')
    email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

    opcoes = [
        "Atualizar aniversário",
        "Atualizar endereço",
        "Atualizar telefone",
        "Atualizar celular",
        "Atualizar email",
        "Finalizar atualização"
    ]

    while True:
        #Garante que seja uma opção válida
        escolha = opcaoEscolhida(opcoes)

        #Todas as validações feitas em 'cadastro' foram reutilizadas aqui:
        if escolha == "1": 
            while True:
                print('Aniversário cadastrado:', contato[1])
                novo = input("Novo aniversário (DD/MM) ou CANCELAR: ").strip()
                if novo.upper() == 'CANCELAR':
                    break
                if len(novo) == 5 and novo[2] == '/':
                    dia, mes = novo[:2], novo[3:]
                    if dia.isdigit() and mes.isdigit():
                        dia, mes = int(dia), int(mes)
                        if 1 <= dia <= 31 and 1 <= mes <= 12:
                            if mes == 2 and dia > 28:
                                print('Fevereiro vai até o dia 28.')
                            elif mes in [4, 6, 9, 11] and dia > 30:
                                print('Esse mês vai até dia 30.')
                            else:
                                contato[1] = novo
                                print('\n\033[32mAniversário atualizado\033[m')
                                break
                        else:
                            print('Dia ou mês fora do intervalo válido.')
                    else:
                        print('Digite números válidos para dia e mês.')
                else:
                    print('Formato inválido. Use DD/MM.')

        elif escolha == "2":
            while True:
                print('Endereço cadastrado:', contato[2])
                novo = input("Novo endereço (ou CANCELAR): ").strip()
                if novo.upper() == 'CANCELAR':
                    break
                if any(c.isalpha() for c in novo) and any(c.isdigit() for c in novo):
                    contato[2] = novo
                    print('\n\033[32mEndereço atualizado\033[m')
                    break
                else:
                    print('Endereço deve conter letras e números')

        elif escolha == "3":
            while True:
                print('Telefone cadastrado:', contato[3])
                novo = input("Novo telefone fixo ou CANCELAR: ").strip()
                if novo.upper() == 'CANCELAR':
                    break
                match = telefone_regex.match(novo)
                if match:
                    contato[3] = novo
                    print('\n\033[32mTelefone atualizado\033[m')
                    break
                else:
                    print('Número inválido. Utilieze --> () caso opte por colocar DDD e uso obrigatório de hífen --> - ')

        elif escolha == "4":
            while True:
                print('Celular cadastrado:', contato[4])
                novo = input("Novo celular (com DDD) ou CANCELAR: ").strip()
                if novo.upper() == 'CANCELAR':
                    break
                match = celular_regex.match(novo)
                if match and 11 <= int(match.group(1)) <= 99:
                    contato[4] = novo
                    print('\n\033[32mCelular atualizado\033[m')
                    break
                else:
                    print('Número inválido. Use DDD e 9 dígitos iniciando com 9.')

        elif escolha == "5":
            while True:
                print('E-mail cadastrado:', contato[5])
                novo = input("Novo e-mail ou CANCELAR: ").strip()
                if novo.upper() == 'CANCELAR':
                    break
                if email_regex.match(novo):
                    contato[5] = novo
                    print('\n\033[32mEmail atualizado\033[m')
                    break
                else:
                    print('E-mail inválido.')

        elif escolha == "6":
            print('\n\033[32mAtualização finalizada\033[m')
            break


#Lista todos os contatos em agenda
def listar(agd):
    #Se estiver vazia = False
    if not agd:
        print('\n\033[33mAgenda vazia --> Nenhum contato para listar\033[m')
        return
    
    else:
        print('\n\033[35mContatos cadastrados:\033[m')
        #For percorre cada contato da lista agd e mostra cada um deles
        for contato in agd:
            print('-'*30)
            print(f"Nome: {contato[0]}")
            print(f"Aniversário: {contato[1]}")
            print(f"Endereço: {contato[2]}")
            print(f"Telefone fixo: {contato[3]}")
            print(f"Celular: {contato[4]}")
            print(f"Email: {contato[5]}")
            print('-'*30)


#Exclui um contato através do nome -- Usa função ondeEsta
def excluir(agd):
    if not agd:
        print('\n\033[33mAgenda vazia --> Nenhum contato para excluir\033[m')
        return

    #Todos os nomes estão na posição 0 em 'contatos'
    nomes = [contato[0] for contato in agd]

    while True:
        print(nomes)
        nome = input('Digite o nome a ser excluído (ou digite CANCELAR para desistir): ').strip()

        if nome.upper() == "CANCELAR":
            print('\n\033[33mOpção cancelada!\033[m')
            return

        achou, posicao = ondeEsta(nome, nomes)

        #Mostra informações do contato
        if achou:
            contato = agd[posicao]
            print('\n\033[32mContato encontrado:\033[m\n')
            print('Nome:', contato[0])
            print('Aniversário:', contato[1])
            print('Endereço:', contato[2])
            print('Telefone:', contato[3])
            print('Celular:', contato[4])
            print('Email:', contato[5])

            #Pede confirmação antes de excluir -- Utiliza umTexto
            confirmar = umTexto('Tem certeza que deseja excluir este contato? [S/N]: ', 'Digite S ou N', ['S', 'N'])
            if confirmar == 'S':
                del agd[posicao]
                print('\n\033[33mContato excluído com sucesso\033[m')
            else:
                print('\033[33mExclusão cancelada!\033[m\n')
        else:
            print('\n\033[33mContato não encontrado. Por favor, tente novamente\033[m')


apresenteSe()

agenda = []
menu = ['Cadastrar Contato',
        'Procurar Contato',
        'Atualizar Contato',
        'Listar Contatos',
        'Excluir Contato',
        'Sair do Programa']

while True:
    try:
        #A função opcaoEscolhida utiliza a lista 'menu' criada acima
        #Valida as escolhas do usuário
        opcao = int(opcaoEscolhida(menu))
    except ValueError:
        print('Por favor, digite um número válido')
        continue

    if opcao == 1:
        cadastrar(agenda)
    elif opcao == 2:
        procurar(agenda)
    elif opcao == 3:
        atualizar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)
    elif opcao == 6:
        break
    else:
        print('Opção inválida. Por favor, tente novamente')



print('\n\033[34mPrograma encerrado com sucesso! Até mais :)\033[m\n')










