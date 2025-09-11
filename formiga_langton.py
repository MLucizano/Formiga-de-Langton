import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import lil_matrix


class Formiga:
    direcoes = ['cima', 'direita', 'baixo', 'esquerda']              
    
    def __init__(self, posicao ,direcao, mundo):
        self.posicao = posicao
        self.direcao =  direcao
        self.mundo = mundo
        self.marker = 's'  # marcador inicial para 'cima' 
    
    def andar(self, orientacao_atual): # define as direcoes que irão andar retornando o vetor de deslocamento
        match orientacao_atual:
            case 'cima':
                x, y = 0, 1
                self.marker = '^'
            case 'direita':
                x, y = 1, 0
                self.marker = '>'
            case 'baixo':
                x, y = 0 , -1
                self.marker = 'v'
            case 'esquerda':
                x,y = -1,0
                self.marker = '<'    
        return(x, y)

    def vira_dir(self):
            self.direcao = (self.direcao + 1) % 4 # A formiga girou para a direita
            self.mundo.grid[self.posicao[0] + self.mundo.meio, self.posicao[1] + self.mundo.meio] = False  # atualiza o grid
    
    def vira_esq(self):
            self.direcao = (self.direcao - 1) % 4 # A formiga girou para a esquerda  
            self.mundo.grid[self.posicao[0] + self.mundo.meio, self.posicao[1] + self.mundo.meio] = True # atualiza o grid
    
    def mover(self): 
        self.mundo.crescer_mundo(self)
        self.direcao = self.direcao % 4  # Garante que a direção esteja entre 0 e 3
        if self.mundo.grid[self.posicao[0] + self.mundo.meio, self.posicao[1] + self.mundo.meio]: # verifica se a posição é preta ou branca
            self.vira_dir()

        else: # verifica se a posição é preta ou branca 
            self.vira_esq()
            
        deslocamento_x, deslocamento_y = self.andar(self.direcoes[self.direcao]) # Formula para atualizar a posição da formiga  
        self.posicao = self.posicao[0] + deslocamento_x , self.posicao[1] + deslocamento_y # Posicao formiga += vetor de onde ela vai andar
        self.mundo.crescer_mundo(self)

class Mundo:
    def __init__(self):
        self.tamanho_matriz = 7 # 17 Tamanho da matriz 
        self.grid = lil_matrix(((self.tamanho_matriz, self.tamanho_matriz)), dtype=bool) # armazena celulas pretas em uma matriz esparsa
        self.meio = self.calcular_meio()  # meio da matriz, será calculado dinamicamente
        self.borda = (-self.meio , self.meio )
        self.range_max = 101    

    def calcular_meio(self):   
        self.meio = self.tamanho_matriz // 2
        return (self.meio)
    
    def red_matrix(self):
        nova_matriz = lil_matrix((self.tamanho_matriz, self.tamanho_matriz), dtype=bool)
        deslocamento = 1 # deslocamento para centralizar o grid antigo
        linhas, colunas = self.grid.nonzero() # pega as posições ativas da matriz antiga
        for x, y in zip(linhas, colunas): # copia apenas células ativas
            nova_matriz[x + deslocamento, y + deslocamento] = True

        return(nova_matriz)
    
    def crescer_mundo(self, formiga ):
        if self.tamanho_matriz == self.range_max:
            x, y = formiga.posicao
            borda_min = -self.meio 
            borda_max = self.meio 

            if x < borda_min:  # Wrap horizontal
                formiga.posicao = (borda_max, y)
            elif x > borda_max:
                formiga.posicao = (borda_min, y)

            if y < borda_min: # Wrap vertical
                formiga.posicao = (x, borda_max)
            elif y > borda_max:
                formiga.posicao = (x, borda_min)
            return

        elif formiga.posicao[0] in self.borda or formiga.posicao[1] in self.borda:
            self.tamanho_matriz += 2
            self.meio = self.calcular_meio()
            self.borda = (-self.meio , self.meio )   
            self.grid = self.red_matrix()

    def display(self,formiga):  # Exibição dos graficos
        plt.clf()  # limpa figura
        matriz_densa = self.grid.toarray()# Converter para array denso de 0/1
        formiga_mundo = (formiga.posicao[0] + self.meio , formiga.posicao[1] + self.meio )  
        plt.imshow(matriz_densa, interpolation='none', cmap='gray_r') # exibe a matriz 
        plt.scatter(formiga_mundo[1] , formiga_mundo[0]  , c='red', s=100, marker= formiga.marker)  # Exibe a formiga na matriz
        plt.xticks([])  # remove os rótulos do eixo x
        plt.yticks([])  # remove os rótulos do eixo y
        plt.title("Mundo da Formiga de Langton")
        plt.draw()       # redesenha
        plt.pause(0.1)   #plt.pause(0.001) # plt.pause(0.1) # pausa curta para mostrar atualização
    def exibir_mundo(self, formiga):        
        self.meio = self.calcular_meio()  # Calcula o meio da matriz
        self.crescer_mundo(formiga)  # Verifica se é necessário crescer o mundo
        self.display(formiga)  # Exibe a matriz atualizada

# ---- Execução ----
novo_mundo = Mundo()  # Cria uma instância do mundo
formiga1 = Formiga((0, 0),0, novo_mundo)  # Cria uma instância da formiga com o mundo associado
movimentos = 100000
novo_mundo.exibir_mundo(formiga= formiga1)# starta o mundo antes de iniciar os movimentos

# -------- Controle de eventos --------
parar = False

def fechar(event):
    global parar
    parar = True  # quando fechar a janela

def tecla(event):
    global parar
    if event.key == 'escape':  # quando pressionar Esc
        parar = True

fig = plt.gcf()  # pega a figura atual
fig.canvas.mpl_connect('close_event', fechar)
fig.canvas.mpl_connect('key_press_event', tecla)

# -------- Loop --------
plt.ion() # Ativa o modo interativo do matplotlib
for passo in range(movimentos):
    if parar:  # se a janela for fechada ou Esc pressionado
        break
    formiga1.mover()
    novo_mundo.exibir_mundo(formiga= formiga1)

plt.ioff() # Desativa o modo interativo do matplotlib
plt.show() # Exibe o gráfico final