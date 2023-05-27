from arbitro import Arbitro
from equipe import Equipe


class Jogo():
    def __init__(self, numero: int, local: str, arbitro: Arbitro,
                 equipe_1: Equipe, equipe_2: Equipe):
        self.__numero = numero
        self.__local = local
        self.__arbitro = arbitro
        self.__equipe_1 = equipe_1
        self.__equipe_2 = equipe_2
        self.__gols_equipe_1 = 0
        self.__gols_equipe_2 = 0
        self.__finalizado = False


    # implementar getters e setters

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @property
    def local(self) -> str:
        return self.__local

    @local.setter
    def local(self, local):
        self.__local = local

    @property
    def arbitro(self) -> Arbitro:
        return self.__arbitro

    @arbitro.setter
    def arbitro(self, arbitro: Arbitro):
        self.__arbitro = arbitro

    @property
    def equipe_1(self) -> Equipe:
        return self.__equipe_1

    @property
    def equipe_2(self) -> Equipe:
        return self.__equipe_2

    @property
    def gols_equipe_1(self) -> int:
        return self.__gols_equipe_1

    @gols_equipe_1.setter
    def gols_equipe_1(self, gols: int):
        self.__gols_equipe_1 = gols

    @property
    def gols_equipe_2(self) -> int:
        return self.__gols_equipe_2

    @gols_equipe_2.setter
    def gols_equipe_2(self, gols: int):
        self.__gols_equipe_2 = gols

    @property
    def finalizado(self) -> bool:
        return self.__finalizado

    @finalizado.setter
    def finalizado(self, estado: bool):
        self.__finalizado = estado




    '''
        Finalizar um jogo consiste em:
        - Alterar o atributo finalizado para True;
        - Atribuir 3 pontos para a equipe que possuir mais gols;
        - Caso haja empate, cada equipe recebe 1 ponto.
    '''
    def finaliza_jogo(self):
        self.finalizado = True
        if self.gols_equipe_1 > self.gols_equipe_2:
            self.equipe_1.pontos += 3
        elif self.gols_equipe_2 > self.__gols_equipe_1:
            self.equipe_2.pontos += 3
        else:
            self.equipe_1.pontos += 1
            self.equipe_2.pontos += 1

    '''
        Calcula a equipe vencedora do jogo,
        com base nos gols das equipes
        Retorna a equipe vencedora do jogo
        ou retorna None em caso de empate
    '''
    def vencedor(self):
        if self.gols_equipe_1 > self.gols_equipe_2:
            return self.equipe_1
        elif self.gols_equipe_2 > self.__gols_equipe_1:
            return self.equipe_2
        else:
            return None

