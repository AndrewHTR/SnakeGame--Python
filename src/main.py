import random
import pygame
import time

def Main():

    #! Importante:
    pygame.init()

    display_width = 800
    display_height = 600
    display = pygame.display.set_mode((display_width,display_height))

    pygame.display.set_caption("Joguinho da Cobrinha")

    game_over = False
    game_close = False

    clock = pygame.time.Clock()

    #! Funções:
    fonte = pygame.font.SysFont(None, 50)
    def mensagem(msg, cor):
        mesg = fonte.render(msg, True, cor)
        display.blit(mesg, [display_width/3 -245, display_height/3 + 50])

    ponto = pygame.font.SysFont(None, 35)
    def score(pontuacao, cor):
        value = ponto.render(f"Pontuação: {str(pontuacao)}", True, cor)
        display.blit(value, [0, 0])
    
    def cobra(corpo_cobra):
        for x in corpo_cobra:
            pygame.draw.rect(display, green, [x[0], x[1], 20, 20])

    #! Dados do jogo:
    # Cores
    white = (255,255,255)
    black = (0,0,0)
    blue = (0, 0, 225)
    red = (213, 50, 80)
    green = (0, 255, 0)

    x1 = display_width/2
    y1 = display_height/2

    x1_change = 0
    y1_change = 0

    velocidade = 10
    pontos = 0

    corpo_cobra = []
    tamanho_cobra = 1

    foodx = round(random.randrange(0, display_width - velocidade) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - velocidade) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(black)
            mensagem("Você perdeu :( Aperte S-Sair ou C-Continuar", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        time.sleep(1)
                        Main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -velocidade
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = velocidade
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -velocidade
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = velocidade
                print(event)
        display.fill(black)

        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        corpo_cobra.append(cabeca_cobra)
        if len(corpo_cobra) > tamanho_cobra:
            del corpo_cobra[0]

        for x in corpo_cobra[:-1]:
            if x == corpo_cobra:
                game_close = True


        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - velocidade) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - velocidade) / 10.0) * 10.0
            print("aa") 
            pontos += 1
            tamanho_cobra += 1
            

        x1 += x1_change 
        y1 += y1_change       

        #! Update da tela:
        score(pontos,blue)
        pygame.draw.rect(display, red, [foodx, foody, 10, 10])
        cobra(corpo_cobra)
        pygame.display.update()

        clock.tick(15)

    pygame.quit()
    quit()
Main()
