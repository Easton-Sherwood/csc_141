import sys
from time import sleep

import pygame

from ship import Ship
from ship import Bullet
from alien import Alien
from settings import Settings
from button import Button
from scoreboard import Statistics
from scoreboard import Scoreboard


class AlienInvasion:
    # Main class to oversee game functionality and resources

    def __init__(self):
        # Initialize the game and load its assets
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to track game stats and render the scoreboard
        self.stats = Statistics(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.burst_mode = False  # Indicates whether burst mode is on or off
        self.last_burst_time = 0  # Tracks the time elapsed between bursts
        self.burst_cooldown = 300  # Time in milliseconds before a new burst can begin
        self.bullet_burst_count = 0

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Background color of the game
        self.bg_color = (230, 230, 230)

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # Create the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        # Begin the main game loop
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

            # Refresh the screen with the latest drawings
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        # Monitor keyboard and mouse inputs
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        # Start a new game when the play button is clicked
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            
            # Reset the game settings
            self.settings.initialize_dynamic_settings()

            # Reset the game statistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Clear any remaining bullets and aliens from the screen
            self.bullets.empty()
            self.aliens.empty()

            # Generate a new alien fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event):                
        # Handle key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_b:
            # Activate or deactivate burst mode when 'B' is pressed
            self.burst_mode = not self.burst_mode
            if self.burst_mode:
                self.bullet_burst_count = 0  # Reset the burst shot counter
                print("Burst Mode Activated!")
        elif event.key == pygame.K_SPACE:
            # Fire bullets; fire three in rapid succession if burst mode is enabled
            if self.burst_mode and self.bullet_burst_count < 3:
                self._fire_bullet()
                self.bullet_burst_count += 1
            elif not self.burst_mode:
                self._fire_bullet()
    
    def _check_keyup_events(self, event):
        # Handle key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        # Refresh bullet positions
        self.bullets.update()

        # Remove bullets that have moved off-screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Eliminate bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets,
                                                self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # Clear bullets and create a new alien fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Advance to the next level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        # Refresh screen visuals and toggle to the updated screen
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Display the score and other statistics
        self.sb.show_score()

        # Show the play button if the game is not active
        if not self.game_active:
            self.play_button.draw_button()

    def _fire_bullet(self):
        # Generate a new bullet and add it to the group
        current_time = pygame.time.get_ticks()

        if self.burst_mode and current_time - self.last_burst_time >= self.burst_cooldown:
            # Shoot three bullets in quick succession and reset the timer
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
            self.last_burst_time = current_time  # Mark the start of the burst
            
            if self.bullet_burst_count == 0:
                # Shoot the second bullet immediately
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
            
            if self.bullet_burst_count == 1:
                # Shoot the third bullet immediately
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
            
            # Disable burst mode after firing three bullets
            if self.bullet_burst_count == 2:
                self.burst_mode = False
        else:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        # Build a fleet of aliens
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Reset the x-position for the next row and increase the y-position
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
            # Generate an alien and add it to the fleet
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    def _update_aliens(self):
        # Refresh alien positions within the fleet
        self._check_fleet_edges()
        self.aliens.update()

        # Check for collisions between the ship and aliens
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Check if any aliens have reached the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        # Take action if any aliens have reached the screen's edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # Move the fleet downward and reverse its direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        # Handle the ship being struck by an alien
        if self.stats.ships_left > 0:
            # Reduce the number of ships left and update the scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Clear any remaining bullets and aliens from the screen
            self.bullets.empty()
            self.aliens.empty()

            # Generate a new alien fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        # Detect if any aliens have reached the screen's bottom
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
   
if __name__ == '__main__':
    # Create an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()