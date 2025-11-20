class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"Item {item.nome} adicionado ao inventário.")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"Item {item.nome} removido do inventário.")
        else:
            print(f"Item {item.nome} não está no inventário.")

    def listar_itens(self):
        if self.itens:
            print("Itens no inventário:")
            for item in self.itens:
                print(f"- {item.nome}")
        else:
            print("Inventário vazio.")

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self._vida = vida
        self.vida_maxima = vida  # Novo atributo
        self.ataque = ataque
        self.arma = None
        self.inventario = Inventario()

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        elif valor > self.vida_maxima:
            self._vida = self.vida_maxima
        else:
            self._vida = valor

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano! Vida restante: {self.vida}")

    def equipar_arma(self, arma):
        self.arma = arma
        print(f"{self.nome} equipou {arma.nome}.")

    def ataque_total(self):
        return self.ataque + (self.arma.poder if self.arma else 0)

    def status(self):
        arma_nome = self.arma.nome if self.arma else "Nenhuma"
        print(f"{self.nome} | Vida: {self.vida} | Ataque: {self.ataque} | Arma: {arma_nome}")

    def atacar(self, alvo):
        dano = self.ataque_total()
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        alvo.receber_dano(dano)
        
    def usar_pocao(self, pocao):
        if pocao in self.inventario.itens:
            vida_antes = self.vida
            cura_efetiva = min(pocao.cura, self.vida_maxima - self.vida)
            self.vida += cura_efetiva
            self.inventario.remover_item(pocao)
            print(f"{self.nome} usou {pocao.nome} e recuperou {cura_efetiva} de vida! ({vida_antes} -> {self.vida})")
        else:
            print(f"{pocao.nome} não está no inventário de {self.nome}.")

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
        print(f"{self.nome} | Vida: {self.vida} | Ataque: {self.ataque}")

    def receber_dano(self, dano):
        
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano! Vida restante: {self.vida}")


# Instanciando personagens
guerreiro = Guerreiro("Thorin")
mago = Mago("Merlin")
arqueiro = Arqueiro("Legolas")

# Instanciando itens
espada = Arma("Espada Longa", 12)
cajado = Arma("Cajado Mágico", 17)
pocao_vida = Pocao("Poção de Vida", 30)
pocao_precisao = Pocao("Poção de Precisão", 20)

# Monstro
goblin = Monstro("Goblin", 60, 15)

# Equipando armas
guerreiro.equipar_arma(espada)
mago.equipar_arma(cajado)

# Inventário
guerreiro.inventario.adicionar_item(espada)
guerreiro.inventario.adicionar_item(pocao_vida)
mago.inventario.adicionar_item(cajado)
arqueiro.inventario.adicionar_item(pocao_precisao)

# Simulando danos e cura
guerreiro.vida = 60
print("\nStatus antes de usar poção:")
guerreiro.status()
print("\nGuerreiro usa poção de vida:")
guerreiro.usar_pocao(pocao_vida)
guerreiro.status()

# Exemplo dos ataques e inventário
print("\nInventário do Guerreiro:")
guerreiro.inventario.listar_itens()

print('\nAtaques:')
guerreiro.atacar(goblin)
mago.atacar(goblin)
arqueiro.atacar(goblin)

print('\nStatus final do Goblin:')
goblin.status()
