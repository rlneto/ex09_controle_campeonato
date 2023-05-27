from pessoa import *


class Arbitro(Pessoa):
    def __init__(self, nome: str, telefone: str, nacionalidade: str,
                 numero_jogos: int):
        super().__init__(nome, telefone)
        self.__nacionalidade = nacionalidade
        self.__numero_jogos = numero_jogos

    @property
    def nacionalidade(self) -> str:
        return self.__nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str):
        self.__nacionalidade = nacionalidade

    @property
    def numero_jogos(self) -> int:
        return self.__numero_jogos

    @numero_jogos.setter
    def numero_jogos(self, numero_jogos: int):
        self.__numero_jogos = numero_jogos
    ...