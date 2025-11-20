# Classe base para personagens
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.arma = None

    def equipar_arma(self, arma):
        self.arma = arma
        print(f"{self.nome} equipou {arma.nome}.")

    def ataque_total(self):
        return self.ataque + (self.arma.poder if self.arma else 0)

    def status(self):
        arma_nome = self.arma.nome if self.arma else "Nenhuma"
        print(f"{self.nome} | Vida: {self.vida} | Ataque: {self.ataque} | Arma: {arma_nome}")

# Classes específicas de heróis
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

# Classe para armas
class Arma:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

# Classe para poções
class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

# Classe Monstro
class Monstro:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def status(self):
        print(f"{self.nome} | Vida: {self.vida} | Ataque: {self.ataque}")

# Instâncias de personagens
guerreiro = Guerreiro("Thorin")
mago = Mago("Merlin")
arqueiro = Arqueiro("Legolas")

# Instanciando armas e poções
espada = Arma("Espada Longa", 12)
cajado = Arma("Cajado Mágico", 17)
pocao_vida = Pocao("Poção de Vida", 30)

# Instância do monstro
goblin = Monstro("Goblin", 60, 15)

# Equipando armas
guerreiro.equipar_arma(espada)
mago.equipar_arma(cajado)

# Exibindo status
guerreiro.status()
mago.status()
arqueiro.status()
goblin.status()

# Demonstrando ataques (força total = ataque base + arma)
print(f"{guerreiro.nome} ataca com força total: {guerreiro.ataque_total()}")
print(f"{mago.nome} ataca com força total: {mago.ataque_total()}")
print(f"{arqueiro.nome} ataca com força total: {arqueiro.ataque_total()}")



