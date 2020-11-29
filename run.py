import gym
import agent_q_learning as agent
import numpy as np
import gym_maze
env = gym.make("maze-random-10x10-plus-v0")
agent = agent.Agent(env.action_space.n)
reward = 0
low = env.observation_space.low
high = env.observation_space.high


for i_episode in range(100000):
    state = tuple(env.reset())  # random or fix
    agent.reset()
    done = False

    while not done:
        action = agent.step(state, reward)
        state, reward, done, info = env.step(action)
        state = tuple(state)
        if i_episode % 100 == 0:
            env.render()
        if done:
            agent.done(state, reward)
            print("Done")
            break

    print("Episode done after {}".format(i_episode))

# evaluation.render()
env.close()
in1 = input("Script wird mit bel. Eingabe beendet !!!!!!!!!! ")
