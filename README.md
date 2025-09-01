# 🏓 Reinforcement Learning Pong Agent

This project implements a **Deep Q-Learning Agent** to play a custom-built Pong game using **PyTorch** and **Pygame**.  
The agent learns to control the left paddle while the right paddle follows a simple hardcoded logic.

---

## 🚀 Features
- Custom **Pong game environment** built with `pygame`.
- Deep Q-Network (**DQN**) with PyTorch (`Linear_Qnet`).
- Experience Replay for stable training.
- ε-greedy policy for exploration vs. exploitation.
- Training visualization using Matplotlib.

---

## 📂 Project Structure
├── agent.py # RL agent & training loop
├── game.py # Pong environment (pygame)
├── model.py # Neural network + Q-learning trainer
├── helper.py # Plotting training progress

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/AnkurKrPal/PongRL.git
cd PongRL

### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

### 3. Install dependencies
pip install torch torchvision pygame matplotlib ipython

### 4. Run
python agent.py