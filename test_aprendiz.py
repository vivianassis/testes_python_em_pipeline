from unittest import TestCase

import personagens

class AprendizTest(TestCase):

    def setUp(self):
        self.viviana = personagens.Aprendiz(nome='Viviana')
    
    def test_criar_aprendiz(self):
        assert self.viviana.nome == 'Matheus'
        assert self.viviana.habilidades_aprendidas == {}

    def test_upar_habilidade(self):
        self.viviana.upar_habilidade('Primeiros Socorros')
    
        assert self.viviana.habilidades_aprendidas == { 'Primeiros Socorros': 1 }

        self.viviana.upar_habilidade('Primeiros Socorros')
    
        assert self.viviana.habilidades_aprendidas == { 'Primeiros Socorros': 2 }

    def test_upar_habilidade_errada(self):
        self.assertRaises(Exception, self.viviana.upar_habilidade, 'Dança Cigana')
