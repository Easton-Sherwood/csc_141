import sys
import pygame
from pygame import sprite

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.color = ai_game.bullet_color
        self.speed = ai_game.bullet_speed
        self.rect = pygame.Rect(0, 0, ai_game.bullet_width, ai_game.bullet_height)
        self.rect.midtop = ai_game.ship_rect.midtop
        self.y = float(self.rect.y)
        

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class AlienInvasion:
    # Overall class to manage game assets and behavior

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")

        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 200, 255)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        
        #Ship Settings
        self.ship_image = pygame.image.load('22raptor.png')
        original_width, original_height = self.ship_image.get_rect().size
        new_width = original_width // 3
        new_height = original_height // 3
        self.ship_image = pygame.transform.scale(self.ship_image, (new_width, new_height))
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.midbottom = self.screen.get_rect().midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.bullets = pygame.sprite.Group()

        self.burst_mode = False
        self.burst_active = False
        self.burst_count = 0
        self.burst_timer = 0 
    
    def run_game(self):
        while True:
            self._check_events()
            self.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_UP:
                    self.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.moving_down = True
                elif event.key == pygame.K_SPACE:
                    if self.burst_mode:
                        self.fire_burst()
                    else:
                        self.fire_single_bullet()
                elif event.key == pygame.K_b:
                    self.burst_mode = not self.burst_mode
                    print(f"Burst mode {'enabled' if self.burst_mode else 'disabled'}")

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_UP:
                    self.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.moving_down = False

    def fire_single_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def fire_burst(self):
        if not self.burst_active:
            self.burst_active = True
            self.burst_count = 0
            self.burst_timer = pygame.time.get_ticks()

    def update_burst_logic(self):
        if self.burst_active:
            current_time = pygame.time.get_ticks()
            if current_time - self.burst_timer >= 100:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
            
                self.burst_count += 1
                self.burst_timer = current_time
            
                if self.burst_count >= 3:
                    self.burst_active = False


    def update(self):

        if self.moving_right and self.ship_rect.right < self.screen_width:
            self.ship_rect.x += 1
        if self.moving_left and self.ship_rect.left > 0:
            self.ship_rect.x -= 1
        if self.moving_up and self.ship_rect.top > 0:
            self.ship_rect.y -= 1
        if self.moving_down and self.ship_rect.bottom < self.screen_height:
            self.ship_rect.y += 1

        self.bullets.update()
        self.update_burst_logic()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        #redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        self.screen.blit(self.ship_image, self.ship_rect)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    pygame.quit()
