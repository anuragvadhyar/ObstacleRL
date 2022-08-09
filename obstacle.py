import random
env_matrix=[[None,None,None,10],[None,None,0,10],[None,10,0,None],[0,100,None,None],[0,None,None,None],[None,None,None,10],[None,10,0,0],[None,None,10,None],[0,100,None,None],[0,None,None,None],[None,10,None,0],[None,None,10,0],[None,None,10,None],[0,100,None,None],[0,None,None,None]]
discount=0.9
learning_rate=0.1
q_table=[]

for i in range(0,15):
    q_table.append([0,0,0,0])

def getactions(current_state):
    components=[x!=None for x in env_matrix[current_state]]
    actions=[]
    if components[0]:
        actions.append(0)
    if components[1]:
        actions.append(1)
    if components[2]:
        actions.append(2)
    if components[3]:
        actions.append(3)

    return actions
def getnextstate(current_state,action):
    if current_state<=4:
        if action==0:
            return current_state-1
        if action==1:
            return current_state+1
        if action==2:
            return current_state-1
        if action==3:
            return current_state+1


    if (current_state>=5 and current_state<=9 and current_state!=8 and current_state!=9):
        if action==0:
            return current_state-2
        if action==1:
            return current_state+2
        if action==2:
            return current_state-1
        if action==3:
            return current_state+1
    if current_state==8:
        if action==0:
            return current_state-2
        if action==1:
            return current_state+1
    if current_state==9:
        if action==0:
            return current_state-1

    if (current_state>=10 and current_state<=14 and current_state!=13 and current_state!=14):
        if action==0:
            return current_state-3
        if action==1:
            return current_state+3
        if action==2:
            return current_state-1
        if action==3:
            return current_state+1
    if current_state==13:
        if action==0:
            return current_state-3
        if action==1:
            return current_state+1

    if current_state==14:
        if action==0:
            return current_state-1


def isgoalreached(current_state):
    return current_state in [4,9,14]



for _ in range(1000):
    current_position=random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])

    while not isgoalreached(current_position):
        actio = getactions(current_position)
        z = random.choice(actio)
        next_state = getnextstate(current_position, z)
        print(current_position)
        print(z)
        print(next_state)

        q_table[current_position][z] = q_table[current_position][z] + learning_rate * (
                        env_matrix[current_position][z] +
                        discount * max(q_table[next_state]) - q_table[current_position][z])

        current_position = next_state
        print('Episode done')


print(q_table)


