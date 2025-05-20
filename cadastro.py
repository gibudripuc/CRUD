print('\033[34mAtividade CRUD\033[m')


def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Giovana Budri Oliveira           RA:25017683                |')
    print('| Matheus Barbosa                  RA:                        |')
    print('| Versão 2.0 de 20/maio/2025                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')



def umTexto (solicitacao, mensagem, valido):
    while True:
        txt=input(solicitacao)
        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
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
    while True:
        nome = input('Digite seu nome (ou CANCELAR para desistir): ').strip()
        if nome.upper() == 'CANCELAR':
            return

        if len(nome.split()) < 3 or not all(palavra.isalpha() for palavra in nome.replace('áéíóúâêôãõçÁÉÍÓÚÂÊÔÃÕÇ', '').split()):
            print("Nome inválido. Digite nome completo com apenas letras.")
            continue

        achou, posicao = ondeEsta(nome, [p[0] for p in agd])
        if achou:
            print("Nome já cadastrado - digite outro.")
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
                print('Tente novamente, fevereiro vai até 28.')
                continue
            elif mes in [4, 6, 9, 11] and dia > 30:
                print('Tente novamente, esse mês vai até 30.')
                continue
            elif dia < 1 or dia > 31:
                print('Dia inválido.')
                continue
            break

        else:
            print("Data inválida. Digite no formato DD/MM e com valores reais.")
   
    while True:
        endereco = input('Endereço: ').strip()
        if any(c.isalpha() for c in endereco) and any(c.isdigit() for c in endereco):
            break
        else:
            print("Endereço inválido. Deve conter letras e números.")

    while True:
        telefone = input('Telefone fixo (somente números, com 10 ou 8 dígitos): ').strip()
        if telefone.isdigit() and len(telefone) in [8, 10]:
            break
        else:
            print('Número inválido. Tente novamente.')

    while True:
        celular = input('Celular (com DDD obrigatório): ').strip()
        if celular.isdigit() and len(celular) == 11 and celular[2] == '9':
            break
        else:
            print('Número inválido. Deve ter 11 dígitos e começar com 9 após o DDD.')

    while True:
        email = input('Email: ').strip()
        if "@" in email and "." in email and email.index("@") < email.rindex("."):
            break
        else:
            print("Email inválido. Verifique o formato.")

    contato = [nome, aniversario, endereco, telefone, celular, email]
    agd.insert(posicao, contato)

    print("Cadastro realizado com sucesso!")