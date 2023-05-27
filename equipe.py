from pessoa import Pessoa
from jogador import Jogador


class Equipe():
    def __init__(self, pais: str, tecnico: Pessoa):
        self.__pais = pais
        self.__tecnico = tecnico
        self.__jogadores = []
        self.__pontos = 0

    # implementar getters e setters
    @property
    def pais(self) -> str:
        return self.__pais

    @pais.setter
    def pais(self, pais: str):
        self.__pais = pais

    @property
    def tecnico(self) -> Pessoa:
        return self.__tecnico

    @tecnico.setter
    def tecnico(self, tecnico: Pessoa):
        self.__tecnico = tecnico

    @property
    def jogadores(self) -> list:
        return self.__jogadores

    @property
    def pontos(self) -> int:
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos: int):
        self.__pontos = pontos

    '''
        Adiciona um novo jogador a lista de jogadores da equipe
        Tratar casos de instancias incorretas
        Nao deve ser possivel adicionar duas vezes o mesmo jogador
        Caso o jogador ja exista, retornar None
    '''

    def add_jogador(self, jogador: Jogador):
        if not isinstance(jogador, Jogador):
            raise "O parâmetro da chamada de função deve apontar para um objeto da classe Jogador"
        elif jogador in self.jogadores:
            return None
        else:
            self.jogadores.append(jogador)
            return True

    '''
        Remove um jogador da lista de jogadores da equipe
        Retorna o jogador que foi removido da lista
        Caso o jogador nao exista na lista, retorna None
    '''

    def remove_jogador(self, jogador: Jogador):
        if jogador not in self.jogadores:
            return None
        else:
            self.jogadores.pop(self.jogadores.index(jogador))
            return True

    '''
        Retorna um numero inteiro com a quantidade total
        de cartoes amarelos da equipe
    '''

    def total_cartoes_time(self) -> int:
        total_cartoes = 0
        for jogador in self.jogadores:
            total_cartoes += jogador.numero_cartoes_amarelos
        return total_cartoes
