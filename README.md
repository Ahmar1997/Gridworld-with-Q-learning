# Gridworld-with-Q-learning

Implentation of the Q learning algorithm in a Gridworld environent

![walls image](https://user-images.githubusercontent.com/116836999/210906371-1c7708c4-7087-4a2e-97f5-a7b70e80fb3c.png)

# Ojective
The goal of the game is for the agent to reach the endpoint in least amount of steps as possible

# Environment
The environment contains a 10x10 grid containing walls at different locations, a starting point at (1,1) and an end point at (10,10)

# Actions
The agent can take four actions: up, down, left and right, If the agent bumps into a wall it will return to its previous location with zero reward

# Rewards
+10 reward for reaching the goal\n
-1 for each step that does not hit a wall\n
-5 for each step that hits a wall

