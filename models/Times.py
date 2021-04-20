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
            self.__score = 0

            self.time_id = self.id + 1

            Times.times.append({'id': self.id,            #0
                                'Time': self.__nome_time,
                                'jogador1': self.__jogador1,
                                'jogador2': self.__jogador2,
                                'score': self.__score})
        elif self.time_id > 10:
            print('Limite de times excedido')

    def mostrar_salao(self):
        for n in Times.times:
            print(n)

    def incrementar_score(self, time, score):
        self.times[time][4] += score
