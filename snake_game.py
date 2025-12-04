"""
Simple Snake Game in Python
============================
A classic snake game built with pygame.

Controls:
- Arrow keys or WASD to move
- Press SPACE to restart after game over
- Press ESC to quit

Requirements:
- pip install pygame

Author: AI Generated for Learning
"""

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
CELL_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    """Represents the snake in the game."""

    def __init__(self):
        """Initialize the snake at the center of the screen."""
        start_x = WINDOW_WIDTH // 2
        start_y = WINDOW_HEIGHT // 2
        self.body = [
            (start_x, start_y),
            (start_x - CELL_SIZE, start_y),
            (start_x - 2 * CELL_SIZE, start_y)
        ]
        self.direction = RIGHT
        self.grow = False

    def move(self):
        """Move the snake in the current direction."""
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x * CELL_SIZE, head_y + dir_y * CELL_SIZE)

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        """Change direction if not reversing."""
        # Prevent 180-degree turns
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def check_collision(self):
        """Check if snake collides with walls or itself."""
        head = self.body[0]

        # Check wall collision
        if (head[0] < 0 or head[0] >= WINDOW_WIDTH or
            head[1] < 0 or head[1] >= WINDOW_HEIGHT):
            return True

        # Check self collision
        if head in self.body[1:]:
            return True

        return False

    def draw(self, screen):
        """Draw the snake on the screen."""
        for i, segment in enumerate(self.body):
            # Head is brighter green
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(screen, color,
                           (segment[0], segment[1], CELL_SIZE - 1, CELL_SIZE - 1))


class Food:
    """Represents the food in the game."""

    def __init__(self):
        """Initialize food at a random position."""
        self.position = (0, 0)
        self.spawn()

    def spawn(self, snake_body=None):
        """Spawn food at a random position not occupied by the snake."""
        if snake_body is None:
            snake_body = []

        while True:
            x = random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            self.position = (x, y)

            if self.position not in snake_body:
                break

    def draw(self, screen):
        """Draw the food on the screen."""
        pygame.draw.rect(screen, RED,
                        (self.position[0], self.position[1], CELL_SIZE - 1, CELL_SIZE - 1))


class Game:
    """Main game class that manages the game loop."""

    def __init__(self):
        """Initialize the game."""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.reset_game()

    def reset_game(self):
        """Reset the game to initial state."""
        self.snake = Snake()
        self.food = Food()
        self.food.spawn(self.snake.body)
        self.score = 0
        self.game_over = False

    def handle_events(self):
        """Handle keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                else:
                    # Arrow keys
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.snake.change_direction(UP)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.snake.change_direction(DOWN)
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.snake.change_direction(LEFT)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.snake.change_direction(RIGHT)

        return True

    def update(self):
        """Update game state."""
        if self.game_over:
            return

        self.snake.move()

        # Check for food collision
        if self.snake.body[0] == self.food.position:
            self.snake.grow = True
            self.score += 10
            self.food.spawn(self.snake.body)

        # Check for game over
        if self.snake.check_collision():
            self.game_over = True

    def draw(self):
        """Draw all game elements."""
        self.screen.fill(BLACK)

        # Draw grid (optional, for visual reference)
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, WINDOW_HEIGHT), 1)
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (WINDOW_WIDTH, y), 1)

        # Draw game elements
        self.food.draw(self.screen)
        self.snake.draw(self.screen)

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Draw game over screen
        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    def draw_game_over(self):
        """Draw the game over overlay."""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        # Game over text
        game_over_text = self.font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30))
        self.screen.blit(game_over_text, text_rect)

        # Final score
        final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10))
        self.screen.blit(final_score_text, score_rect)

        # Restart instruction
        restart_text = self.small_font.render("Press SPACE to restart or ESC to quit", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)

    def run(self):
        """Main game loop."""
        running = True

        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


def main():
    """Entry point for the game."""
    print("=" * 50)
    print("        SNAKE GAME")
    print("=" * 50)
    print("\nControls:")
    print("  - Arrow keys or WASD to move")
    print("  - SPACE to restart after game over")
    print("  - ESC to quit")
    print("\nStarting game...")
    print("=" * 50)

    game = Game()
    game.run()


if __name__ == "__main__":
    main()
