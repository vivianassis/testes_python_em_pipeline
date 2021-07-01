class Aprendiz:

    habilidades_possiveis = [
        'Habilidades Básicas',
        'Primeiros Socorros',
        'Fingir de Morto'
    ]

    def __init__(self, nome):
        self.nome = nome
        self.habilidades_aprendidas = {}
    
    def __repr__(self):
        return f'Aprendiz(nome={self.nome}, habilidades_aprendidas={self.habilidades_aprendidas})'

    def upar_habilidade(self, nome):
        if nome in Aprendiz.habilidades_possiveis:
            if nome in self.habilidades_aprendidas:
                self.habilidades_aprendidas[nome] += 1
            else:
                self.habilidades_aprendidas[nome] = 1
            print(f'{self.nome}: Você melhorou {nome} para o nível {self.habilidades_aprendidas[nome]}')
        else:
            raise Exception(f'Você não pode aprender essa habilidade: {nome}')

class Espachim(Aprendiz):
    habilidades_possiveis = [
        'Golpe Fulminante',
        'Impacto Explosivo',
        'Aumentar Recuperação de HP',
        'Vigor',
        'Perícia com Espada',
        'Perícia com Espada de Duas Mãos'
    ]

