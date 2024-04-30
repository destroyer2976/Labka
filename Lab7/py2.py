import pygame
pygame.init()

samaya= "/Users/zasulan/Downloads/fornastrgit/Lab7/egor-krid-samaya-samaya-mp3.mp3"
pyala = "/Users/zasulan/Downloads/fornastrgit/Lab7/aigel-pyyala-mp3.mp3"
menkazakpyn = "/Users/zasulan/Downloads/fornastrgit/Lab7/1706164617_erbolat-kudajbergen-men-kazakpyn.mp3"

sc = pygame.display.set_mode((700, 700))
pygame.display.set_caption("musi-zuzi")
clock = pygame.time.Clock()      
index=0

musiccaa = [samaya, pyala, menkazakpyn]
pygame.mixer.music.load(musiccaa[index])
pygame.mixer.music.play(0)
puhlya = pygame.image.load("/Users/zasulan/Downloads/fornastrgit/Lab7/puhlya.png")

sc.blit(puhlya, (0, 0))
play = False
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = not play
                if play:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_RIGHT:
                index += 1
                if index == len(musiccaa):
                    index = 0
                pygame.mixer.music.load(musiccaa[index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musiccaa)-1
                pygame.mixer.music.load(musiccaa[index])
                pygame.mixer.music.play()


    pygame.display.flip()
    clock.tick(60)