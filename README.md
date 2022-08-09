# ObstacleRL
Using Reinforcement Learning as an AI/ML tool to simulate an obstacle course for an agent in a 2D world
This project aims to simulate an obstacle course for an agent in a 2D world using Reinforcement Learning as an AI/ML tool.
The environment observables(env_matrix) is used to define rewards for actions performed by the agent dependant on whether it takes it one step closer to solving the problem or one step further away.
The 2 obstacles are spawned in the second column of the 3x3 grid,and the obstacles can be positioned in one of three possible combinations for a given episode.
The agent starts out in the first column in one of the three boxes.The objective of the agent is to avoid the obstacle points in the second column and make it's way to one of the three boxes in the third column.
The reward for avoiding an obstacle is 10;The reward for hitting an obstacle or performing an illegal action is 0(ex: If the agent is in the [0,0]th position,it is rewarded zero for trying to go left or up because they are illegal positions);The reward for reaching the third column is 100.
All the elements of the Q table(q_table) is initialized to zero.
Functions:
getactions(current_state):
This function is used to get all posibble legal actions that can be performed by the agent in the current state.
getnextstate(current_state,action):
This function is used to get the next state after performing a certain action in the current state.
isgoalreached(current_state):
Returns True if the agent is in one of the three boxes in the third column.
Number of episodes is 1000.
The Q table keeps getting updated in every iteration of the for loop.
Output:
Updated Q_table.
