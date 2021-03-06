import pygame
import math

#set up
pygame.init()
WIDTH, HEIGHT = 900,600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

RAD = 35                      
points = "HANGMAN"
z = " "
correctguesses = 0
incorrectguesses = 0
alreadyguessed = []
words = ["ARDENT","YOGURT","LIVING","ABSURD"]

RADIUS = 20
GAP = 20
letters=[]
startx = round((WIDTH - (RADIUS * 2 +GAP)*13)/2)
starty = 20
A = 65

#numwords = 0
myword = 0
for r in range(26):
    x = startx + GAP +((RADIUS*2 + GAP) *(r%13))
    y = (( r // 13)*(GAP + RADIUS*2)) + starty
    letters.append([x,y, chr(A+r), True])

#makinh the hangman appear
images = []
for i in range(8):
    image = pygame.image.load("img" + str(i) + ".png")
    images.append(image)
    i = i+1


#setting up thing to make it easier on you :)
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 15)
WORDS_FONT = pygame.font.SysFont('comicsans', 50)
hangman_status = incorrectguesses
black = (0,0,0)

FPS = 60
#clock = pygame.time.Clock(FPS)
run = True

#drawfunction
def draw():
    win.fill((250,250,250))
    display_word = " "
    for letter in word:
        if letter in alreadyguessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORDS_FONT.render(display_word, 1, black)
    win.blit(text, (8,300))
    pygame.draw.circle(win, (50,90, 70), (50,440), RAD, 3)
    writing = WORD_FONT.render("Play again?", 1, black)
    win.blit(writing,(23,440))
    
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, black, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, black)
            win.blit(text,( x - text.get_width()/2, y - text.get_height()/2))



    win.blit(images[incorrectguesses], (210,100))
    pygame.display.update()

#where the logic comes in
##while run:
   # clock.tick(FPS)
    ##draw()

##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            run = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            m_x, m_y = pygame.mouse.get_pos()
##            for letter in letters:
##                x, y, ltr, visible = letter
##                if visible:
##                    dis = math.sqrt((x-m_x)**2 +(y- m_y)**2)
##                    if dis < RADIUS:
##                        print("Letter is " + letter[2])

numwords = len(words)
word = words[myword]
        
while run:
        draw()
    
        #for word in words:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                 m_x, m_y = pygame.mouse.get_pos()
                 dist = math.sqrt((50-m_x)**2 +(400- m_y)**2)
                 if dist < RAD:
                     print("PLAY AGAIN")
                     myword+=1
                     if myword < numwords:    
                         word = words[1]
                         correctguesses = 0
                         incorrectguesses = 0
                         alreadyguessed = []
                     else:
                        print("You have completed all levels!")
                     #continue
                     #print(word)

            
                 for letter in letters:
                     x, y, ltr, visible = letter
                     if visible:
                        dis = math.sqrt((x-m_x)**2 +(y- m_y)**2)
                        if dis < RADIUS:
                            print("Letter is " + letter[2])

                            guess_letter =letter[2]
                            print(guess_letter)
                            if letter[2] in alreadyguessed:
                                print("You have already guessed this")
                                incorrectguesses+=1
                            elif letter[2] in word:
                                    print("Correct")
                                    correctguesses+=1
                                    alreadyguessed.append(letter[2])
                            else:
                                    print("Try again")
                                    incorrectguesses+=1
                            if correctguesses == 6:
                                    print("YOU WIN")
                                    break
                            if incorrectguesses == 7:
                                    win.blit(images[incorrectguesses], (150,100))
                                    pygame.display.update()
                                    print("You lose! :(")
                                    run = False
                                    break
                                    
    ##    Play_again = input("Want another word? Yes or No?")
    ##    print(play_again)
    ##
    ##    if (play_again == "Yes"):
    ##        continue
    ##    else:
    ##        print("Game Over")
    ##        break
pygame.quit()
    
