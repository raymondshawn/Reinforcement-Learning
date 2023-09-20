import gymnasium as gym
import numpy as np
env=gym.make("CliffWalking-v0")
actions=env.action_space.n
states=env.observation_space




def initialise_Qtable(states,actions):
    q_table=np.zeros(states,actions)
    return q_table


