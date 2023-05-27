from pessoa import Pessoa


class Jogador(Pessoa):
    def __init__(self, nome: str, telefone: str, numero_camisa: int, numero_cartoes_amarelos: int):
        super().__init__(nome, telefone)
        self.__numero_camisa = numero_camisa
        self.__numero_cartoes_amarelos = numero_cartoes_amarelos

    @property
    def numero_camisa(self) -> int:
        return self.__numero_camisa

    @numero_camisa.setter
    def numero_camisa(self, numero_camisa: int):
        self.__numero_camisa = numero_camisa

    @property
    def numero_cartoes_amarelos(self) -> int:
        return self.__numero_cartoes_amarelos

    @numero_cartoes_amarelos.setter
    def numero_cartoes_amarelos(self, numero_cartoes_amarelos: int):
        self.__numero_cartoes_amarelos = numero_cartoes_amarelos

