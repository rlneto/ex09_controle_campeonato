from jogo import Jogo
from jogo_duplicado_exception import JogoDuplicadoException


class ControladorCampeonato():
    def __init__(self):
        self.__jogos = []

    @property
    def jogos(self) -> list:
        return self.__jogos

    '''
        Busca jogo pelo numero na lista de jogos.
        Se o jogo nao existir, o metodo deve retornar None
        Caso contrario, retorna o jogo.
    '''
    def busca_jogo_por_numero(self, numero):
        for jogo in self.jogos:
            if jogo.numero == numero:
                return jogo
        return None


    '''
        Incluir jogo na lista.
        Tratar os casos de instancias incorretas e jogo duplicado.
        Caso o jogo ja exista na lista, lancar uma excecão
        JogoDuplicadoException
    '''
    def add_jogo(self, jogo: Jogo):
        if not isinstance(jogo, Jogo):
            raise "O parâmetro deve apontar para um objeto do tipo Jogo."
        elif jogo in self.jogos:
            raise JogoDuplicadoException
        else:
            self.jogos.append(jogo)


    '''
        Remove um jogo da lista de jogos do controlador.
        Recebe como parametro o numero de um jogo a ser removido.
        Retorna o objeto jogo que foi removido
        Se o jogo não existir na lista, retorna None.
    '''
    def remove_jogo(self, numero: int):
        retorno = None
        for jogo in self.jogos:
            if jogo.numero == numero:
                retorno = jogo
                self.jogos.pop(self.jogos.index(retorno))
                break
        return retorno

    '''
        Retorna uma lista das equipes em ordem decrescente de pontuacao
        Nao deve retornar equipes duplicadas na mesma lista
        Caso duas equipes possuam a mesma pontuacao,
        a ordem entre elas na lista nao eh relevante
    '''
    def classificacao_campeonato(self) -> list:
        tabela = []
        for jogo in self.jogos:
            if jogo.equipe_1 not in tabela:
                tabela.append(jogo.equipe_1)
            if jogo.equipe_2 not in tabela:
                tabela.append(jogo.equipe_2)
        tabela.sort(key=lambda equipe: equipe.pontos, reverse=True)
        return tabela


