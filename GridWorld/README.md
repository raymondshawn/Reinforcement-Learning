Environment Name: "GridWorld"

Description:
The GridWorld environment is a classic grid-based environment where an agent navigates through a grid, collecting rewards and avoiding obstacles. The grid is a 2D square grid with cells represented as coordinates (x, y). The agent starts at a random cell in the grid and can move in four directions: up, down, left, and right. The agent's goal is to reach a specific goal cell while avoiding obstacles and maximizing the cumulative reward.

Environment Setup:

    Grid Size: Determine the size of the grid (e.g., 5x5, 10x10, etc.).
    Start Cell: Randomly select a cell as the agent's starting position.
    Goal Cell: Randomly select a cell as the goal position.
    Obstacles: Randomly place obstacles in some cells of the grid to create barriers that the agent must navigate around.
    Rewards: Assign positive or negative rewards to certain cells to encourage or discourage the agent's movement towards those cells.

State Space:
The state space is represented by the agent's current cell in the grid (x, y).

Action Space:
The action space consists of four discrete actions:

    Move Up
    Move Down
    Move Left
    Move Right

Reward System:

    +10 reward for reaching the goal cell.
    -10 penalty for colliding with an obstacle.
    -1 penalty for each step taken.

Episode Termination:
The episode terminates when the agent reaches the goal cell or collides with an obstacle. The agent receives the corresponding reward or penalty, and a new episode begins with the agent placed in a new random starting position.

This simple GridWorld environment can serve as a starting point for testing and implementing basic reinforcement learning algorithms like Q-learning or policy gradients. You can further extend the environment by introducing additional complexities such as variable rewards, stochastic movement, or multiple goals.