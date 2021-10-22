#importar bibliotecas
import pygame
import time
from botao import Botao

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
def desenha_botao(tela, botao, highlighted = False): #função que desenha os botões na tela
    if highlighted:
        pygame.draw.rect(tela, botao.cor_secundaria, botao.rect) #se o cursor estiver no botão (highlighted = true), ele fica cinza
        tela.blit(seta, (posicoes_seta[cursor]))

    else:
        pygame.draw.rect(tela, botao.cor_principal, botao.rect) #se o cursor não estiver no botão (highlighted = false), ele fica branco

#definindo cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#criar listas
#um nome em dada posição x remete a localizacao na posição x
nomeimg = ['background', 'huntersprite', 'menu', 'seta'] #nomes da variáveis das imagens
locimg = [r"imagens\background\teste 1.png", r"imagens\personagens\hunter sprite.png", r"imagens\UI\introcomp_menu.png", r"imagens\UI\introcomp_seta.png"] #localização das imagens

#criando as imagens
for c in range(len(nomeimg)): #esse loop cria as variáveis das imagens com base nos nome e localização...
    globals()[nomeimg[c]] = pygame.image.load(locimg[c]) #colocados nas listas nomeimg e locimg

#ajustando o tamanho das imagens
huntersprite = pygame.transform.scale(huntersprite, (140, 140)) #um mero exemplo pra salvar o comando
menu = pygame.transform.scale(menu, (180, 180))
seta = pygame.transform.scale(seta, (50, 50))

#cria tela
j = Janela(768,1024) #objeto que guarda e retorna as dimensões da tela
tela = pygame.display.set_mode(j.dim())
pygame.display.set_caption("IntroBattle") #estabelece o nome da janela
largura_janela = tela.get_width() #armazena a largura da janela
altura_janela = tela.get_height() #armazena a altura da janela
origem = (largura_janela // 2, altura_janela // 2) #centro da tela

#cria o relógio que controla o fps
clock = pygame.time.Clock()

#criar váriaveis pré estabelecidas
run = True

#iniciar o pygame
pygame.init()

#configurações globais de um botão
cores = ((255, 255, 255), (105,105,105)) #cor principal e secundária dos botões (n selecionado e selecionado)
dim_botao = (180, 180)

#criando botões de escolha dos personagens (todos os botões seguem a mesma estrutura, só modificando os valores)
#criando botão 1 (paladin)
posicao_botao1 = ((largura_janela // 2 - 90) - 300, 230) #posição do botão
posicao_seta1 = (posicao_botao1[0] + 65, 190) #posição da seta
label1 = "PALADIN" #etiqueta do botão
botao1 = Botao(label1, dim_botao, posicao_botao1, cores, posicao_seta1) #instanciando a classe botão

#criando botão 2 (rogue)
posicao_botao2 = (largura_janela // 2 - 90, 230)
posicao_seta2 = (posicao_botao2[0] + 65, 190)
label2 = "ROGUE"
botao2 = Botao(label2, dim_botao, posicao_botao2, cores, posicao_seta2)

#criando botão 3 (wizard)
posicao_botao3 = ((largura_janela // 2 - 90) + 300, 230)
posicao_seta3 = (posicao_botao3[0] + 65, 190)
label3 = "WIZARD"
botao3 = Botao(label3, dim_botao, posicao_botao3, cores, posicao_seta3)

#criando botão 4 (hunter)
posicao_botao4 = ((largura_janela // 2 - 90) - 150, 510)
posicao_seta4 = (posicao_botao4[0] + 65, 470)
label4 = "HUNTER"
botao4 = Botao(label4, dim_botao, posicao_botao4, cores, posicao_seta4)

#criando botão 5 (priest)
posicao_botao5 = ((largura_janela // 2 - 90) + 150, 510)
posicao_seta5 = (posicao_botao5[0] + 65, 470)
label5 = "PRIEST"
botao5 = Botao(label5, dim_botao, posicao_botao5, cores, posicao_seta5)

#informações para navegação nos botões de escolha do personagem
botoes = [botao1, botao2, botao3, botao4, botao5]
posicoes_botoes = [posicao_botao1, posicao_botao2, posicao_botao3, posicao_botao4, posicao_botao5]
posicoes_seta = [posicao_seta1, posicao_seta2, posicao_seta3, posicao_seta4, posicao_seta5]
cursor = 0

#game-loop
while run:

    #definindo a posição do cursor
    posicao_cursor_shifted = posicoes_botoes[cursor]
    posicao_cursor = (
        posicao_cursor_shifted[0] + dim_botao[0] // 10,
        posicao_cursor_shifted[1] + dim_botao[1] // 2 #para dar uma margem e evitar que 2 botões fiquem marcados ao mesmo tempo
    )

    tela.fill(j.cor())
    tela.blit(background,(0, 0)) #coloca o background   

    #desenha os botões "escondidos" na tela
    #OBS: esses botões estão escondidos atrás dos 'menus'. para ver eles é só colocar o loop (linhas 120 a 124) depois de colocar os menus (linhas 127 a 131)
    for botao in botoes:
        if posicao_cursor in botao: #se o cursor estiver dentro do botão
            desenha_botao(tela, botao, True) #highlight é verdadeiro
        else: #se não
            desenha_botao(tela, botao) #highlight é falso

    #coloca as caixinhas de menu atrás dos personagens
    tela.blit(menu, (largura_janela // 2 - 90, 230)) #bloco rogue (cima, meio)
    tela.blit(menu, ((largura_janela // 2 - 90) - 300, 230)) #bloco paladin (cima, esquerda)
    tela.blit(menu, ((largura_janela // 2 - 90) + 300, 230)) #bloco wizard (cima, direita)
    tela.blit(menu, ((largura_janela // 2 - 90) + 150, 510)) #bloco priest (baixo, direita)
    tela.blit(menu, ((largura_janela // 2 - 90) - 150, 510)) #bloco hunter (baixo, esquerda) 

    # tela.blit(huntersprite, (100, 500)) #ainda vamos configurar certinho

    #criando o título "INTROBATTLE!" na tela
    pygame.draw.rect(tela, BRANCO, pygame.Rect(largura_janela // 2 - 175, 35, 350, 80)) # retângulo preto
    pygame.draw.rect(tela, PRETO, pygame.Rect(largura_janela // 2 - 170, 40, 340, 70)) #margem

    titulo = 'INTROBATTLE!'
    pygame.font.init() 
    fonte = pygame.font.get_default_font() #pega fonte padrão do pygame
    fontesys = pygame.font.SysFont(fonte, 50) #usa fonte padrão
    titulotela = fontesys.render(titulo, 1, (255,255,255)) #define nome, tamanho, cor
    tela.blit(titulotela,(largura_janela // 2 - 130, 60)) # coloca na tela

    #setinha de seleção dos jogadores

    #coleta os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
        if evento.type == pygame.KEYDOWN: #ATENÇÃO: isso aqui é provisório
            if evento.key == pygame.K_x: #no pc da idade média da sofia, a tela cobre o x da janela
                run = False #e eu não consigo fechar kkkkkk então no final a gente tira isso

        # navega para a seleção dos personagens
        if evento.type == pygame.KEYDOWN: 
            if evento.key == pygame.K_RIGHT:
                cursor += 1 if cursor < len(posicoes_botoes) - 1 else 0 #se for para direita aumenta 1
            elif evento.key == pygame.K_LEFT:
                cursor -= 1 if cursor > 0 else 0 #se for para esquerda diminui 1

            #posicionando a setinha sobre os botões de seleção quando o cursor estiver sobre ele

    #regula o fps
    clock.tick(30)

    #faz o update
    pygame.display.update()

pygame.quit()