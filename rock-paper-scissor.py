print("JOGO CLÁSSICO PEDRA PAPEL E TESOURA")
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.escolha = ""
    def escolher(self):
        self.escolha = input("{nome}, escolha pedra, papel ou tesoura: ".format(nome = self.nome))
        print("{nome} escolheu fez sua escolha".format(nome = self.nome))

    def escolhaNumero(self):
        switcher = {
            "pedra": 0,
            "papel": 1,
            "tesoura": 2
        }
        return switcher[self.escolha]
    def acrescentaPonto(self):
        self.pontos +=1

class Rodadas:
    def __init__(self, j1, j2):
        self.regras = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
            ]
        j1.escolher()
        j2.escolher()
        resultado = self.compareEscolhas(j1, j2)
        
        print("O RESULTADO FOI...")
        
        if resultado > 0:
            j1.acrescentaPonto()
        elif resultado < 0:
            j2.acrescentaPonto()
        else:
            print("Ninguém pontuou.")

    def compareEscolhas(self, j1, j2):
        return self.regras[j1.escolhaNumero()][j2.escolhaNumero()]

class Game:
    def __init__(self):
        self.fimDeJogo = False
        self.jogador = Jogador("Jogador1")
        self.segundoJogador = Jogador("Jogador2")
    
    def start(self):
        while not self.fimDeJogo:
            Rodadas(self.jogador, self.segundoJogador)
            self.checarResultados()

    def checarResultados(self):
        pergunta = input("Quer continuar a jogar y/n: ")
        if pergunta == 'y':
            Rodadas(self.jogador, self.segundoJogador)
            self.checarResultados()
        else:
            print("FIM DE JOGO, {j1nome} está com {j1pontos}, e {j2nome} está com {j2pontos}".format(j1nome = self.jogador.nome, j1pontos = self.jogador.pontos, j2nome = self.segundoJogador.nome, j2pontos = self.segundoJogador.pontos))
            self.vencedor()
            self.fimDeJogo = True

    def vencedor(self):
        resultString = "EMPATE"
        if self.jogador.pontos > self.segundoJogador.pontos:
            resultString = "{nome} VENCEU!!".format(nome = self.jogador.nome)
        elif self.jogador.pontos < self.segundoJogador.pontos:
            resultString = "{nome} VENCEU!!".format(nome = self.segundoJogador.nome)
        print(resultString)

game = Game()
game.start()