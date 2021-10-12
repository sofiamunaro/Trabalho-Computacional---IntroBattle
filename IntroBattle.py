#importar bibliotecas
import pygame
import time

#criar classes
class Janela:
    def __init__(self, altura, largura, cor = pygame.Color(0,0,0)): 
        self.__altura = altura
        self.__largura = largura
        self.__cor = cor
    def dim(self): #retorna as dimensões da janela
        return self.__largura, self.__altura
    def cor(self): #retorna a cor da janela
        return self.__cor

#criar funções

#criar listas
nomeimg = ['background', 'huntersprite', 'menu'] #nomes da variáveis das imagens
locimg = [r"imagens\background\teste 1.png", r"imagens\personagens\hunter sprite.png", r"imagens\UI\introcomp_menu.png"] #localização das imagens
#um nome em dada posição x remete a localizacao na posição x

#definindo cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#criando as imagens
for c in range(len(nomeimg)): #esse loop cria as variáveis das imagens com base nos nome e localização...
    globals()[nomeimg[c]] = pygame.image.load(locimg[c]) #colocados nas listas nomeimg e locimg

#ajustando o tamanho das imagens
huntersprite = pygame.transform.scale(huntersprite, (140, 140)) #um mero exemplo pra salvar o comando
menu = pygame.transform.scale(menu, (180, 180))

#cria tela
j = Janela(768,1024) #objeto que guarda e retorna as dimensões da tela
tela = pygame.display.set_mode(j.dim())
pygame.display.set_caption("IntroBattle") #estabelece o nome da janela
largura_janela = tela.get_width() #armazena a largura da janela
altura_janela = tela.get_height() #armazena a altura da janela

#cria o relógio que controla o fps
clock = pygame.time.Clock()

#criar váriaveis pré estabelecidas
run = True

#iniciar o pygame
pygame.init()

#game-loop
while run:
    #coloca o background
    tela.fill(j.cor())
    tela.blit(background,(0, 0))
    # tela.blit(menu, (100, 500)) #ainda vamos configurar certinho
    # tela.blit(huntersprite, (100, 500)) #ainda vamos configurar certinho

    #criando o título "INTROBATTLE!" na tela
    pygame.draw.rect(tela, BRANCO, pygame.Rect(largura_janela // 2 - 175, 35, 350, 80))
    pygame.draw.rect(tela, PRETO, pygame.Rect(largura_janela // 2 - 170, 40, 340, 70))

    titulo = 'INTROBATTLE!'
    pygame.font.init() 
    fonte = pygame.font.get_default_font() #pega fonte padrão do pygame
    fontesys = pygame.font.SysFont(fonte, 50) #usa fonte padrão
    titulotela = fontesys.render(titulo, 1, (255,255,255)) #define nome, tamanho, cor
    tela.blit(titulotela,(largura_janela // 2 - 130, 60)) # coloca na tela

    #coleta os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
        if evento.type == pygame.KEYDOWN: #ATENÇÃO: isso aqui é provisório
            if evento.key == pygame.K_x: #no pc da idade média da sofia, a tela cobre o x da janela
                run = False #e eu não consigo fechar kkkkkk então no final a gente tira isso

    #regula o fps
    clock.tick(30)

    #faz o update
    pygame.display.update()

pygame.quit()
