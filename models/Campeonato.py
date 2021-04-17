
class Campeonato:

    def __init__(self):
        pass

    def criar_campeonato(self, nome, descricao, regras, score):
        self.__nome = nome
        self.__descricao = descricao
        self.__regras = regras
        self.__score = score

    def mostrar_torneio(self):
        return (f'Torneio de nome: {self.__nome} \n'
                f'Descrição: {self.__descricao} \n'
                f'Regras: {self.__regras} \n'
                f'Score: {self.__score} \n')


