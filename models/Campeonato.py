
class Campeonato:
    campeonato = []

    def __init__(self):
        pass

    def criar_campeonato(self, nome, descricao, regras):
        self.nome = nome
        self.descricao = descricao
        self.regras = regras
        self.score = 0

        Campeonato.campeonato.extend([self.nome,
                                      self.descricao,
                                      self.regras,
                                      self.score])

    def mostrar_torneio(self):
        return print(f'Nome do Torneio : {self.campeonato[0]} \n'
                     f'Descrição do torneio: {self.campeonato[1]} \n'
                     f'Regras do Torneio: {self.campeonato[2]} \n'
                     f'Score do Torneio: {self.campeonato[3]} \n')

    def score_vencedor(self, score):
        self.score = score

