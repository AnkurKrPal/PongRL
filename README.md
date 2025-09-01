<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PongRL</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .section-card {
            background-color: #1a202c; /* A slightly lighter shade of gray-900 */
            border: 1px solid #2d3748; /* gray-800 */
        }
    </style>
</head>
<body class="bg-gray-900 text-gray-200">

    <div class="container mx-auto p-4 md:p-8 max-w-4xl">

        <header class="text-center mb-10">
            <h1 class="text-4xl md:text-5xl font-bold text-white mb-2">PongRL</h1>
            <p class="text-xl md:text-2xl text-cyan-400">AI Learns to Play Pong with Deep Q-Learning</p>
        </header>

        <!-- Overview Section -->
        <section id="overview" class="mb-8 p-6 rounded-lg section-card">
            <h2 class="text-3xl font-semibold border-b-2 border-cyan-500 pb-2 mb-4 text-white">1. Overview</h2>
            <div class="flex flex-col md:flex-row gap-6 items-center">
                 <div class="flex-grow">
                    <p class="text-lg leading-relaxed">
                        PongRL is a Python project that implements a Reinforcement Learning agent to play the classic game of Pong. The agent uses a Deep Q-Network (DQN) to learn the optimal strategy for controlling the left paddle. The primary goal is not just to score but to maximize the number of successful ball returns ("hits").
                    </p>
                    <p class="text-lg leading-relaxed mt-4">The project is built using:</p>
                    <ul class="list-disc list-inside mt-2 space-y-1 text-lg">
                        <li><strong class="text-cyan-400">Pygame:</strong> For creating the Pong game environment, handling graphics, and game logic.</li>
                        <li><strong class="text-cyan-400">PyTorch:</strong> For building and training the neural network that serves as the agent's brain.</li>
                        <li><strong class="text-cyan-400">Matplotlib:</strong> For visualizing the agent's learning progress in real-time.</li>
                    </ul>
                </div>
                <div class="md:w-1/3 w-2/3 flex-shrink-0">
                    <img src="https://placehold.co/400x300/000000/FFFFFF?text=Pong+Game" alt="Classic Pong Game Screen" class="rounded-lg shadow-2xl border-2 border-gray-700">
                </div>
            </div>
        </section>

        <!-- Project Structure Section -->
        <section id="structure" class="mb-8 p-6 rounded-lg section-card">
            <h2 class="text-3xl font-semibold border-b-2 border-cyan-500 pb-2 mb-4 text-white">2. Project Structure</h2>
            <p class="mb-4 text-lg">The project is organized into four main Python files, each with a specific responsibility:</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="bg-gray-800 p-4 rounded-lg border border-gray-700">
                    <h3 class="text-xl font-bold text-cyan-400">`game.py`</h3>
                    <p class="mt-2">Manages the game environment, graphics, game logic, and reward system using Pygame.</p>
                </div>
                <div class="bg-gray-800 p-4 rounded-lg border border-gray-700">
                    <h3 class="text-xl font-bold text-cyan-400">`model.py`</h3>
                    <p class="mt-2">Defines the `Linear_Qnet` neural network architecture and the `QTrainer` class for handling the training steps.</p>
                </div>
                <div class="bg-gray-800 p-4 rounded-lg border border-gray-700">
                    <h3 class="text-xl font-bold text-cyan-400">`agent.py`</h3>
                    <p class="mt-2">The core AI logic. The `Agent` class connects the game and the model, manages memory, and runs the main training loop.</p>
                </div>
                <div class="bg-gray-800 p-4 rounded-lg border border-gray-700">
                    <h3 class="text-xl font-bold text-cyan-400">`helper.py`</h3>
                    <p class="mt-2">A utility script for plotting the agent's performance live with Matplotlib.</p>
                </div>
            </div>
        </section>

        <!-- How It Works Section -->
        <section id="how-it-works" class="mb-8 p-6 rounded-lg section-card">
            <h2 class="text-3xl font-semibold border-b-2 border-cyan-500 pb-2 mb-4 text-white">3. How It Works: The Reinforcement Learning Approach</h2>
            <p class="text-lg mb-4">The agent learns through a process of trial and error, guided by a reward system. This is a classic Deep Q-Learning (DQN) implementation.</p>
            
            <h3 class="text-2xl font-semibold text-cyan-400 mt-6 mb-2">State</h3>
            <p class="mb-2">The agent observes a state represented by a NumPy array of 6 values:</p>
            <ol class="list-decimal list-inside space-y-1">
                <li>Ball's X-coordinate</li>
                <li>Ball's Y-coordinate</li>
                <li>Ball's X-direction (velocity)</li>
                <li>Ball's Y-direction (velocity)</li>
                <li>Agent's (left) paddle's Y-coordinate</li>
                <li>Opponent's (right) paddle's Y-coordinate</li>
            </ol>

            <h3 class="text-2xl font-semibold text-cyan-400 mt-6 mb-2">Actions</h3>
            <p class="mb-2">The agent can perform one of three actions:</p>
            <ul class="list-disc list-inside space-y-1">
                <li>Move Up</li>
                <li>Move Down</li>
                <li>Stay Still</li>
            </ul>

            <h3 class="text-2xl font-semibold text-cyan-400 mt-6 mb-2">Reward System</h3>
            <ul class="list-disc list-inside space-y-1">
                <li><span class="font-bold text-green-400">+10:</span> For successfully hitting the ball.</li>
                <li><span class="font-bold text-green-400">+20:</span> For scoring a point.</li>
                <li><span class="font-bold text-red-400">-10:</span> For missing the ball.</li>
                <li><span class="font-bold text-red-400">-10:</span> A penalty if the game takes too long.</li>
            </ul>

            <h3 class="text-2xl font-semibold text-cyan-400 mt-6 mb-2">Training Loop</h3>
             <ol class="list-decimal list-inside space-y-2">
                <li><b>Observe:</b> The agent gets the current state from the game.</li>
                <li><b>Act:</b> It uses its neural network to predict the best action, balancing exploration (random moves) and exploitation (learned moves).</li>
                <li><b>Remember:</b> The experience (state, action, reward, next state) is stored in a memory buffer.</li>
                <li><b>Learn (Short-Term):</b> The network is trained on the most recent experience.</li>
                <li><b>Learn (Long-Term):</b> The network is trained on a random batch of past experiences from memory (Experience Replay).</li>
                <li><b>Repeat:</b> The process repeats, improving performance over thousands of games.</li>
            </ol>
        </section>

        <!-- Getting Started Section -->
        <section id="getting-started" class="mb-8 p-6 rounded-lg section-card">
            <h2 class="text-3xl font-semibold border-b-2 border-cyan-500 pb-2 mb-4 text-white">4. Getting Started</h2>
            
            <h3 class="text-2xl font-semibold text-cyan-400 mb-2">Prerequisites</h3>
            <p class="mb-3">You need Python and the following libraries installed:</p>
            <pre class="bg-gray-800 p-4 rounded-md text-white border border-gray-700"><code class="language-bash">pip install pygame torch numpy matplotlib ipython</code></pre>
            <p class="mt-3">You will also need an <code class="bg-gray-700 px-2 py-1 rounded">arial.ttf</code> font file in the same directory for the score display to work correctly.</p>

            <h3 class="text-2xl font-semibold text-cyan-400 mt-6 mb-2">How to Run</h3>
            <p class="mb-3">To start the training process, run the `agent.py` file from your terminal:</p>
            <pre class="bg-gray-800 p-4 rounded-md text-white border border-gray-700"><code class="language-bash">python agent.py</code></pre>
        </section>

        <!-- Expected Output Section -->
        <section id="output" class="p-6 rounded-lg section-card">
            <h2 class="text-3xl font-semibold border-b-2 border-cyan-500 pb-2 mb-4 text-white">5. Expected Output</h2>
            <p class="mb-4 text-lg">When you run the script, two windows will appear: the Pygame window showing the game and a Matplotlib window plotting the agent's learning progress.</p>
            <p class="mb-3">You will also see progress printed to the console:</p>
            <pre class="bg-gray-800 p-4 rounded-md text-white border border-gray-700"><code class="language-bash">Game 1, Hits: 2, Record: 2, Epsilon: 0.9950
Game 2, Hits: 1, Record: 2, Epsilon: 0.9900
...
Game 500, Hits: 45, Record: 45, Epsilon: 0.0778</code></pre>
             <p class="mt-4 text-lg">Over time, you should observe the agent transitioning from frantic, random movements to smoother, more intelligent behavior, consistently hitting the ball more often.</p>
        </section>

    </div>

</body>
</html>
