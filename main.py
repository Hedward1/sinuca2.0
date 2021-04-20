from models.Campeonato import Campeonato
from models.Times import Times

verification = True
campeonato = Campeonato()
time = Times()

while verification:
    value = input('-------------------------------------------------------\n'
                  'Digite "1" para cadastrar um campeonato.              -\n'
                  'Digite "2" para ter acesso a informações do torneio.  -\n'
                  'Digite "3" para visualizar times no torneio.          -\n'
                  'Digite "4" para cadastrar time no torneio.            -\n'
                  'Digite "5" para inserir a pontuação do time desejado. -\n'
                  'Digite "0" para sair do programa.                     -\n'
                  '-------------------------------------------------------\n')

    if value == '1':
        print('bem vindo ao cadastro do Campeonato')
        nome_torneio = input('Digite o nome do torneio: ')
        descricao_torneio = input('Digite uma descrição para o torneio: ')
        regras_torneio = input('Digite as regas do torneio: ')
        score_torneio = int(input('Digite o score para vencer: '))

        campeonato.criar_campeonato(nome=nome_torneio,
                                    descricao=descricao_torneio,
                                    regras=regras_torneio,
                                    score=score_torneio)

    elif value == '2':
        campeonato.mostrar_torneio()
    elif value == '3':
        time.mostrar_salao()
    elif value == '4':
        print('cadastro Time')
        time_nome = input('Digite o nome do time: \n')
        nome_jogador1 = input('Digite o nome do primeiro jogador \n')
        nome_jogador2 = input('Digite o nome do segundo jogador \n')

        time.cadastro_time(nome_time=time_nome,
                           jogador1=nome_jogador1,
                           jogador2=nome_jogador2)

    elif value == '5':
        time_insert = int(input('Sigite o "id" do time que seja alterar,'
                                'pode descobrir selecionando numero 3 na tela '
                                'anterior.'))
        score_insert = int(input('digite o score que dejesa adicionar'))
        time.incrementar_score(time_insert, score_insert)
    elif value == '0':
        verification = 0

    else:
        print('Valor digitado incoreto.')
