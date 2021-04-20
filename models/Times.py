from models.Campeonato import Campeonato
from termcolor import colored


class Times:
    times = []
    time_id = 1

    def __init__(self):
        pass

    def cadastro_time(self, nome_time, jogador1, jogador2):
        if self.time_id <= 10:
            self.id = self.time_id
            self.__nome_time = nome_time
            self.__jogador1 = jogador1
            self.__jogador2 = jogador2
            self.score = 0

            self.time_id = self.id + 1
            # Salva o dicionario dentro d euma lista
            Times.times.append({'id': self.id,  # 0
                                'nome': self.__nome_time,
                                'jogador1': self.__jogador1,
                                'jogador2': self.__jogador2,
                                'score': self.score})

        # se caso insira mais de x times
        elif self.time_id > 10:
            print('Limite de times excedido')

    # Metodo criado para consultar a ordenação pelo dicionario 'score'
    def func_sort(self):
        return self['score']

    # Faz ordenação da lista times[]
    def mostrar_salao(self):
        self.times.sort(key=Times.func_sort, reverse=True)
        for n in self.times:
            print(n)

    # Seleciona o "time" com o numero procurado e então adiciona o score
    def incrementar_score(self, time, score):
        self.times[time-1]['score'] += score
        if self.times[time-1]['score'] >= Campeonato.score:
            print(colored(f' O TIME {self.times[time-1]["nome"]} É O VENCEDOR', 'green'))

