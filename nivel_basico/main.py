# Classes de personagem e itens para RPG simples

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.arma = None

    def equipar_arma(self, arma):
        self.arma = arma
        print(f"{self.nome} agora está armado com {arma.nome}")

    def ataque_total(self):
        return self.ataque + (self.arma.poder if self.arma else 0)

    def status(self):
        arma_usada = self.arma.nome if self.arma else "Nenhuma"
        print(f"{self.nome} - Vida: {self.vida}, Ataque: {self.ataque}, Arma: {arma_usada}")

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=120, ataque=25)
        self.armadura = 10

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=30)
        self.poder_magico = 50

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=90, ataque=22)
        self.precisao = 15

class Arma:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

class Monstro:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def status(self):
        print(f"{self.nome}: Vida = {self.vida}, Ataque = {self.ataque}")

# --- Código principal: criando personagens, itens e fazendo testes ---

guerreiro = Guerreiro("Thorin")
mago = Mago("Merlin")
arqueiro = Arqueiro("Legolas")

espada = Arma("Espada Longa", 12)
cajado = Arma("Cajado Mágico", 17)
pocao_vida = Pocao("Poção de Vida", 30)

goblin = Monstro("Goblin", 60, 15)

guerreiro.equipar_arma(espada)
mago.equipar_arma(cajado)

print('\nStatus dos personagens:')
guerreiro.status()
mago.status()
arqueiro.status()
goblin.status()

print(f"\n{guerreiro.nome} vai atacar: força total = {guerreiro.ataque_total()}")
print(f"{mago.nome} vai atacar: força total = {mago.ataque_total()}")
print(f"{arqueiro.nome} vai atacar: força total = {arqueiro.ataque_total()}")




