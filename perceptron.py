
import random
import copy
from csv import (DictReader, )

class Perceptron:

    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas=1000, limiar=-1):

        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado    # taxa de aprendizado (entre 0 e 1)
        self.epocas = epocas
        self.limiar = limiar
        self.num_amostras = len(amostras)
        self.num_amostra = len(amostras[0])
        self.pesos = []

    # função que recebe as amostras de oleo e as treinas

    def treinar(self):

        # adiciona -1 para cada uma das amostras
        for amostra in self.amostras:
            amostra.insert(0, -1)

        # inicia o vetor de pesos com valores aleatórios
        for i in range(self.num_amostra):
            self.pesos.append(random.random())

        self.pesos.insert(0, self.limiar)

        num_epocas = 0

        while True:

            erro = False  # o erro inicialmente inexiste

            # para todas as amostras de treinamento
            for i in range(self.num_amostras):

                u = 0
                for j in range(self.num_amostra + 1):
                    u += self.pesos[j] * self.amostras[i][j]

                y = self.sinal(u)
                if y != self.saidas[i]:

                    erro_aux = self.saidas[i] - y

                    # faz o ajuste dos pesos
                    for j in range(self.num_amostra + 1):
                        self.pesos[j] = self.pesos[j] + \
                            self.taxa_aprendizado * \
                            erro_aux * self.amostras[i][j]

                    erro = True

            # aumenta numero de epocas
            num_epocas += 1

            # se o numero de epocas bater ou não haver erro
            if num_epocas > self.epocas or not erro:
                break

    # função utilizada para testar a rede
    # ela classifica as amostra tanto em P1 como P2
    # sendo p1 valor -1 e p2 1

    def testar(self, amostra, classe1, classe2):

        amostra.insert(0, -1)
        u = 0
        for i in range(self.num_amostra + 1):
            u += self.pesos[i] * amostra[i]

        y = self.sinal(u)
        
        print(f'A amostra de óleo pertence a classe de pureza P1') if y == -1 else print(f'A amostra de óleo pertence a classe de pureza P2')

    # função de ativação: degrau bipolar (sinal)

    def sinal(self, u):
        return 1 if u >= 0 else -1


print('\n A Amostra de óleo pertence a qual classe de pureza?P1 ou P2?\n')

# começo do da implementação com as amostras e saidas
amostras = []
saidas = []

with open('./content/dataset.csv', 'r') as dados:
    dados = DictReader(dados)
    for dado in dados:
        amostras.append([float(dado['x1']), float(dado['x2']), float(dado['x3'])])
        saidas.append(float(dado['d']))

testes = copy.deepcopy(amostras)

# aqui aonde e rede do percptron e criada com entradas, saidas e a taxa de aprendizagem
redePerceptron = Perceptron(amostras=amostras, saidas=saidas,
                  taxa_aprendizado=0.1, epocas=1000)

redePerceptron.treinar()

for teste in testes:
    redePerceptron.testar(teste, 'P1', 'P2')
