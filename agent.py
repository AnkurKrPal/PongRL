import torch
import random
import numpy as np
from collections import deque
from game import Pong
from model import Linear_Qnet, QTrainer, device
from helper import plot

MAX_MEMORY = 100_000
BATCH_SIZE = 1024  # Recommendation: 1024
LR = 0.00025       # Recommendation: 0.00025

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01 
        self.gamma = 0.99
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_Qnet(6, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)
    
    def get_state(self, game):
        state = [
            game.ball_pos[0],
            game.ball_pos[1],
            game.ball_dir[0],
            game.ball_dir[1],
            game.left_player.y,
            game.right_player.y
        ]
        return np.array(state, dtype=float)
    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        final_move = [0, 0, 0]
        if random.random() < self.epsilon:
            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float).to(device)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move

def train():
    plot_hits_list = []
    plot_mean_hits = []
    total_hits = 0
    record = 0
    agent = Agent()
    game = Pong()
    while True:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)

        reward, done, score, hits = game.play_step(final_move)
        state_new = agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            # Decay epsilon
            if agent.epsilon > agent.epsilon_min:
                agent.epsilon *= agent.epsilon_decay

            if hits > record:
                record = hits
                agent.model.save()

            print(f'Game {agent.n_games}, Hits: {hits}, Record: {record}, Epsilon: {agent.epsilon:.4f}')

            plot_hits_list.append(hits)
            total_hits += hits
            mean_hits = total_hits / agent.n_games
            plot_mean_hits.append(mean_hits)
            plot(plot_hits_list, plot_mean_hits)

if __name__ == '__main__':
    train()