import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np
import sys

pygame.init()
# Correctly load the font from the file with its extension.
font = pygame.font.Font('arial.ttf', 25)

class Direction(Enum):
    UP = 1
    DOWN = 2
    NONE = 3

width, height = 800, 600
paddle_width, paddle_height = 10, 100
PADDLE_SPEED = 10
OPPONENT_SPEED = 8  # New constant for the right paddle
BALL_RADIUS = 10
BALL_SPEED = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

class Pong:
    def __init__(self, w=800, h=600):
        self.w = w
        self.h = h

        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()

        # Load the font from the local file instead of system fonts.
        self.font = pygame.font.Font('arial.ttf', 30)

        self.left_score, self.right_score = 0, 0
        self.left_hits = 0 # Add hits counter
        self.frame_iteration = 0

        self.reset()

    def reset(self):
        self.ball_pos = np.array([self.w // 2, self.h // 2], dtype=float)

        # New logic to constrain the angle
        # 1. Get a random angle in a 50-degree arc (-25 to +25 degrees)
        angle = np.random.uniform(-25, 25)

        # 2. Randomly decide to send the ball left or right


        # 3. Convert angle to radians and create the direction vector
        angle_rad = np.deg2rad(angle)
        self.ball_dir = np.array([np.cos(angle_rad), np.sin(angle_rad)])

        self.left_player = pygame.Rect(10, self.h // 2 - paddle_height // 2, paddle_width, paddle_height + 25)
        self.right_player = pygame.Rect(self.w - 20, self.h // 2 - paddle_height // 2, paddle_width, paddle_height)

        self.left_hits = 0
        self.frame_iteration = 0

    def play_step(self, action):
        self.frame_iteration += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self._move_left(action)
        self._move_right()

        self.ball_pos += self.ball_dir * BALL_SPEED

        reward = self._collision()
        game_over = False

        if self.ball_pos[0] < 0:
            self.right_score += 1
            reward = -10
            game_over = True
        elif self.ball_pos[0] > self.w:
            self.left_score += 1
            reward = 20
            game_over = True

        if self.frame_iteration > 2000:
            game_over = True
            reward = -10

        self._update_ui()
        self.clock.tick(FPS)

        return reward, game_over, self.left_score, self.left_hits

    def _move_left(self, action):
        # action: [up, down, none]
        if np.array_equal(action, [1, 0, 0]):
            self.left_player.y -= (PADDLE_SPEED + 5)
        elif np.array_equal(action, [0, 1, 0]):
            self.left_player.y += (PADDLE_SPEED + 5)

        self.left_player.y = max(0, min(self.h - paddle_height, self.left_player.y))

    def _move_right(self):
        if self.right_player.centery < self.ball_pos[1]:
            self.right_player.y += OPPONENT_SPEED
        elif self.right_player.centery > self.ball_pos[1]:
            self.right_player.y -= OPPONENT_SPEED

        self.right_player.y = max(0, min(self.h - paddle_height, self.right_player.y))

    def _collision(self):
        reward = 0
        ball_rect = pygame.Rect(self.ball_pos[0] - BALL_RADIUS, self.ball_pos[1] - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

        if ball_rect.colliderect(self.left_player):
            self.ball_dir[0] = abs(self.ball_dir[0])
            self.left_hits += 1
            reward = 10
        elif ball_rect.colliderect(self.right_player):
            self.ball_dir[0] = -abs(self.ball_dir[0])

        if self.ball_pos[1] - BALL_RADIUS <= 0 or self.ball_pos[1] + BALL_RADIUS >= self.h:
            self.ball_dir[1] *= -1

        return reward

    def _update_ui(self):
        self.display.fill(BLACK)

        pygame.draw.ellipse(self.display, WHITE, (
            self.ball_pos[0] - BALL_RADIUS, self.ball_pos[1] - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2))
        pygame.draw.rect(self.display, WHITE, self.left_player)
        pygame.draw.rect(self.display, WHITE, self.right_player)

        left_text = self.font.render(f"Score: {self.left_score}", True, WHITE)
        right_text = self.font.render(f"Score: {self.right_score}", True, WHITE)
        hits_text = self.font.render(f"Hits: {self.left_hits}", True, WHITE)

        self.display.blit(left_text, (self.w // 4, 20))
        self.display.blit(right_text, (self.w * 3 // 4, 20))
        self.display.blit(hits_text, (10, 10))

        pygame.display.flip()