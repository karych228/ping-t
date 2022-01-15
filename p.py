from pygame import *
window = display.set_mode((700,500))
display.set_caption('ping-pong')
background = transform.scale(image.load('venti.jpg'),(700,500))
window.blit(background,(0,0))
game = True
clock = time.Clock()
FPS = 120
class GameSprite(sprite.Sprite):
    def __init__(self,player_image1,player_image2,ballx,bally,size_x,size_y,ball_speed,):
        super().__init__()
        self.image1 = transform.scale(image.load(player_image1),(65,65))
        self.image2 = transform.scale(image.load(player_image2),(65,65))
        self.speed = ball_speed
        self.rect = self.image.get_rect()
        self.rect.x = ballx
        self.rect.y = bally
    def reset(self):
        window.blit(self.image1,(self.rect.x,self.rect.y))
        window.blit(self.image2,(self.rect.x,self.rect.y))
ball = GameSprite()

    
finish = False
while game:
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1






class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700-80:
            self.rect.x += self.speed
    def fire(self):
        bullet= Bullet("korshun.png",self.rect.centerx,self.rect.top,15,20,15)
        bullets.add(bullet)
player = Player("korshun.png",350,450,80,100,10)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(50,650)
            self.rect.y = 0
            global lost
            lost = lost + 1
enemeis = sprite.Group()
for i in range(4):
    enemy = Enemy(".png",randint(50,650),0,100,0,randint(1,3))
    enemeis.add(enemy)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
bullets = sprite.Group()

score = 0
lost = 0 
win = font.render('YOU LOSE!',True,(255,215,0))





speed_x = 3
speed_y = 3
finish = False
game = True 
while game:
    window.blit(background,(0,0))
    if lost > 9:
        window.blit(win,(200,200))
        text_win = font.render("Пропущено:"+ str(lost),1,(255,215,0))
        finish = True
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect > win_height -50 or ball.rect.y < 0:
        speed_y *= -1
    window.blit()
    player.reset()
    player.update()
    enemeis.draw(window)
    enemeis.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    bullets.draw(window)
    bullets.update()
    display.update()
    sprites_list = sprite.groupcollide(enemeis,bullets,True,True)
    for i in sprites_list:
        enemy = Enemy("ufo.png",randint(50,650),0,100,0,randint(1,3))
        enemeis.add(enemy)
    clock.tick(FSP)