from termcolor import colored


class Campeonato:
    campeonato = []
    score = 0
    def __init__(self):
        pass

    def criar_campeonato(self, nome, descricao, regras, score):
        self.nome = nome
        self.descricao = descricao
        self.regras = regras
        Campeonato.score = score

        Campeonato.campeonato.extend([self.nome,
                                      self.descricao,
                                      self.regras,
                                      self.score])
        print(colored('*-------------------*', 'green'))
        print(colored('* Campeonato criado *', 'green'))
        print(colored('*-------------------* \n', 'green'))

    def mostrar_torneio(self):
        return print(f'Nome do Torneio : {self.campeonato[0]} \n'
                     f'Descrição do torneio: {self.campeonato[1]} \n'
                     f'Regras do Torneio: {self.campeonato[2]} \n'
                     f'Score do Torneio: {self.campeonato[3]} \n')

