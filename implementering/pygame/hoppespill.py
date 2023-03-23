import pygame
import random

# Definer farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definer skjermstørrelse
WIDTH = 800
HEIGHT = 600

# Definer ball
class Ball:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT - 50
        self.radius = 20
        self.color = WHITE
        self.speed = 0
        self.gravity = 0.1
        
    def jump(self):
        self.speed = -3
        
    def update(self):
        self.speed += self.gravity
        self.y += self.speed
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.speed = 0
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Definer stolpe
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.width = 50
        self.color = WHITE
        self.speed = 5
        self.gap = 200
        self.top_height = random.randint(100, 400)
        self.bottom_height = HEIGHT - self.gap - self.top_height
        
    def update(self):
        self.x -= self.speed
        
    def offscreen(self):
        return self.x < -self.width
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (int(self.x), 0, self.width, self.top_height))
        pygame.draw.rect(screen, self.color, (int(self.x), HEIGHT - self.bottom_height, self.width, self.bottom_height))

# Definer spill
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.ball = Ball()
        self.pipes = []
        self.score = 0
        self.font = pygame.font.SysFont(None, 30)
        self.game_over = False
        
    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.jump()
                        
            self.screen.fill(BLACK)
            self.ball.update()
            self.ball.draw(self.screen)
            self.update_pipes()
            self.draw_pipes()
            self.draw_score()
            pygame.display.update()
            self.clock.tick(60)
            
        pygame.quit()
        
    def update_pipes(self):
        for pipe in self.pipes:
            pipe.update()
            if pipe.offscreen():
                self.pipes.remove(pipe)
                self.score += 1
        if len(self.pipes) < 4:
            self.pipes.append(Pipe())
        self.check_collision()
        
    def draw_pipes(self):
        for pipe in self.pipes:
            pipe.draw(self.screen)
            
    def draw_score(self):
        score_text = self.font.render("Score: {}".format(self.score), True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
   
