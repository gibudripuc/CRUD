import re
print()
print('Atividade CRUD')
print()

def apresenteSe ():
    print('\033[34m+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Giovana Budri Oliveira           RA:25017683                |')
    print('| Matheus Barbosa                  RA:                        |')
    print('| Versão 2.0 de 20/maio/2025                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+\033[m')



def umTexto (solicitacao, mensagem, valido):
    while True:
        txt=input(solicitacao)
        if txt not in valido:
            print(mensagem,' - Favor redigitar.')
        else:
            break
    return txt


def opcaoEscolhida(mnu):
    print()

    opcoesValidas = []
    for p, opcao in enumerate(mnu):
        print(f"{p+1}) {opcao}")
        opcoesValidas.append(str(p+1))

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)


def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1
    
    while inicio <= final:
        meio = (inicio + final) // 2
        if agd[meio] == nom:
            return [True, meio]
        elif agd[meio] < nom:
            inicio = meio + 1
        else:
            final = meio - 1

    return [False, inicio]

def cadastrar(agd):
    nome_regex = re.compile(r'^[A-Za-zÀ-ÿ]+(?:\s[A-Za-zÀ-ÿ]+)+$')
    telefone_regex = re.compile(r'^\(?(\d{2})\)?\s?\d{4}-?\d{4}$') 
    celular_regex = re.compile(r'^\(?(\d{2})\)?\s?9\d{4}-?\d{4}$')
    email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

    while True:
        nome = input('Digite nome (ou CANCELAR para desistir): ').strip()
        if nome.upper() == 'CANCELAR':
            print('Opção cancelada!')
            return
        
        if not nome_regex.match(nome):
            print('Nome inválido. Por favor, digite um nome completo (apenas letras e espaços)')
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
        telefone = input('Telefone fixo (com DDD obrigatório): ').strip()
        match = telefone_regex.match(telefone)
        if match:
            ddd = int(match.group(1))
            if 11 <= ddd <= 99:
                break
            else:
                print('DDD inválido')
        else:
            print('Número inválido. Deve conter DDD e 8 dígitos')

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
            print('Número inválido. Deve conter DDD e 9 dígitos (começando com 9).')
        
    while True:
        email = input('Email: ').strip()
        if email_regex.match(email):
            break
        else:
            print('Email inválido')

    contato = [nome, aniversario, endereco, telefone, celular, email]
    agd.insert(posicao, contato)

    print()
    print('\033[33mCadastro realizado com sucesso!\033[m')



def listar(agd):
    if not agd:
        print('Nenhum contato cadastrado')
    else:
        print()
        print('Contatos cadastrados:')
        for contato in agd:
            print("-" * 30)
            print(f"Nome: {contato[0]}")
            print(f"Aniversário: {contato[1]}")
            print(f"Endereço: {contato[2]}")
            print(f"Telefone fixo: {contato[3]}")
            print(f"Celular: {contato[4]}")
            print(f"Email: {contato[5]}")
            print("-" * 30)


def excluir(agd):
    if not agd:
        print('Agenda vazia --> Nenhum contato para excluir')
        return

    nomes = [contato[0] for contato in agd]

    while True:
        print(nomes)
        nome = input('Digite o nome a ser excluído (ou digite CANCELA para desistir): ').strip()

        if nome.upper() == "CANCELA":
            print('Exclusão cancelada pelo usuário')
            return

        achou, posicao = ondeEsta(nome, nomes)

        if achou:
            contato = agd[posicao]
            print("\nContato encontrado:")
            print("Nome:", contato[0])
            print("Aniversário:", contato[1])
            print("Endereço:", contato[2])
            print("Telefone:", contato[3])
            print("Celular:", contato[4])
            print("Email:", contato[5])

            confirmar = input('Tem certeza que deseja excluir este contato? [S/N]: ').strip().upper()
            if confirmar == 'S':
                del agd[posicao]
                print('Contato excluído com sucesso')
            elif confirmar == 'N':
                print('Exclusão cancelada')
            else:
                print('Usuário não digitou "S" e não digitou "N", o programa entendeu como exclusão cancelada')
            return
        else:
            print('Contato não encontrado. Por favor, tente novamente')


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
        opcao = int(opcaoEscolhida(menu))
    except ValueError:
        print('Por favor, digite um número válido')
        continue

    if opcao == 1:
        cadastrar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)
    elif opcao == 6:
        break
    else:
        print('Opção inválida. Por favor, tente novamente')

    print()

print('\033[34mPrograma encerrado com sucesso! Até mais :)')










