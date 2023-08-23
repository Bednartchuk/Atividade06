# A composição é um conceito importante na programação orientada a objetos (POO), 
# que se refere à construção de objetos complexos através da combinação de objetos mais simples.
#  Em vez de herdar funcionalidades diretamente, como na herança,
#  a composição envolve a criação de objetos contendo outros objetos como partes componentes,
#  permitindo uma maior flexibilidade e reutilização de código.

                                        # EXEMPLO 1

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print(f"Motor {self.tipo} ligado")

    def desligar(self):
        print(f"Motor {self.tipo} desligado")

class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

    def ligar(self):
        print(f"Carro da marca {self.marca} ligado")
        self.motor.ligar()

    def desligar(self):
        print(f"Carro da marca {self.marca} desligado")
        self.motor.desligar()

motor_do_carro = Motor("V8")
meu_carro = Carro("Ferrari", motor_do_carro)

meu_carro.ligar()
meu_carro.desligar()

                                        # EXEMPLO 2

class Habilidade:
    def __init__(self, nome, tipo, dano):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano

class Personagem:
    def __init__(self, nome, habilidades):
        self.nome = nome
        self.habilidades = habilidades

    def atacar(self, alvo, habilidade):
        print(f"{self.nome} atacou {alvo.nome} com {habilidade.nome} causando {habilidade.dano} de dano.")

fogo = Habilidade("Bola de Fogo", "Fogo", 30)
golpe_espada = Habilidade("Golpe de Espada", "Físico", 20)

mago = Personagem("Mago", [fogo])
guerreiro = Personagem("Guerreiro", [golpe_espada])

mago.atacar(guerreiro, fogo)
guerreiro.atacar(mago, golpe_espada)


