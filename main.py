from models.Campeonato import Campeonato
verification = True
campeonato = Campeonato()

while verification:
    value = input('Digite "1" para cadastrar um campeonato. \n'
                  'Digite "2" para ter acesso a informações do torneio. \n'
                  'Digite "0" para sair do programa. \n')

    if value == '1':
        print('bem vindo ao cadastro do Campeonato')
        nome_torneio = input('Digite o nome do torneio: ')
        descricao_torneio = input('Digite uma descrição para o torneio: ')
        regras_torneio = input('Digite as regas do torneio: ')
        score_torneio = input('Digite o score para vencer: ')

        campeonato.criar_campeonato(nome=nome_torneio,
                                    descricao=descricao_torneio,
                                    score=score_torneio,
                                    regras=regras_torneio)

    elif value == '2':
        campeonato.mostrar_torneio()
    elif value == '0':
        verification = 0

    else:
        print('Valor digitado incoreto.')


