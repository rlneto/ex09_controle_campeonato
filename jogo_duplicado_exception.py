

class JogoDuplicadoException(Exception):
    def __init__(self):
        print("O jogo já consta na lista.")