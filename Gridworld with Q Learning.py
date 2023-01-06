import random
import torch
import matplotlib.pyplot as plt
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


number_of_states = 100
steps_per_episode = 1000
episodes = 200
columns = 10
rows = 10
columns_Q_table = 6
Q_table_column = {'U':2,'D':3,'L':4,'R':5}


#Walls

walls = [[2,7],[3,7],[4,7],[4,4],[4,3],[4,2],[7,6],[7,5],[7,4],[7,3],[9,8],[9,7],  #inner walls
         [1,11],[2,11],[3,11],[4,11],[5,11],[6,11],[7,11],[8,11],[9,11],[10,11],    #upper walls
         [1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],    #donward walls
         [0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],     #left walls
         [11,1],[11,2],[11,3],[11,4],[11,5],[11,6],[11,7],[11,8],[11,9],[11,10]]     #right walls


#grid = torch.zeros(rows,columns)
Q_table = torch.zeros(number_of_states,columns_Q_table)



first_index = 1
second_index = 1 
counter = 0
for i in range(number_of_states):                    # indexing the first two colums in the Q_table which are the rows and colums of the state
    Q_table[i,1] = first_index
    Q_table[i,0] = second_index
    first_index = first_index + 1
    counter = counter + 1
    if counter == 10:
        first_index = 1
        second_index = second_index + 1
        counter = 0
    

#hyperparameters

Q_value = 0
alpha = 0.7
gamma = 0.9
epsilon = 1
decay_rate = 0.97

number_of_steps_per_episode = []
episode_counting_list = []
episode_counter = 0


for episode in range(episodes):                                         #episodes loop
    x = 1                                                               #initialize x and y to 0 at the start of each episode
    y = 1
    current_state = [x,y]   

    step_counter = 0
    
    for iterations in range(steps_per_episode):                              #steps loop
        
        if random.uniform(0, 1) < epsilon:                                   #exploration
            action = random.choice(['U','L','D','R'])
            
            
        else:                                                                #exploitation
           action = list(Q_table_column.keys())[list(Q_table_column.values()).index(torch.argmax(Q_table[Q_table_row,2:]).item()+2)]
           
       
        
        #getting Q_table coordinates for previous state
        
        Q_table_row = (x - 1) * 10 + y - 1                #formula to get Q table argument (row number) from rows and colums of the grid
        
        
       
        temporary_state = current_state                     #setting a temporary state incase we hit a wall
        print(current_state, action)    
        if action == 'U':
            y = y + 1
        elif action == 'D':
            y = y - 1
        elif action == 'R':
            x = x + 1
        elif action == 'L':
            x = x - 1
            
           
            
      
        #condition for the agent jumping into a wall and returning to its original state
        
        for wall in walls:                  
            if [x,y] == wall:
                hit_wall = True
                break
                
            else:
                hit_wall = False
                
        if hit_wall == True:
            current_state = temporary_state
            [x,y] = temporary_state
        else:
            current_state = x, y
            
        #print(current_state)
        
        
         #getting Q_table coordinates for new state
        
        Q_table_row_new = (x - 1) * 10 + y - 1               #formula to get Q table argument (row number) from rows and colums of the grid
        
        
        
        step_counter = step_counter + 1
        
        #Updating Q_table
        
        if current_state == (10,10):             #reward when reaching goal
            reward = 10
            Q_table[Q_table_row, Q_table_column[action]] = Q_table[Q_table_row, Q_table_column[action]].item() + alpha * (reward + gamma * torch.max(Q_table[Q_table_row_new,2:]).item() - Q_table[Q_table_row, Q_table_column[action]].item())
            break
            
        if hit_wall is not True:            #reward when not hitting a wall
            reward = -1
            Q_table[Q_table_row, Q_table_column[action]] = Q_table[Q_table_row, Q_table_column[action]].item() + alpha * (reward + gamma * torch.max(Q_table[Q_table_row_new,2:]).item() - Q_table[Q_table_row, Q_table_column[action]].item())
        
        elif hit_wall is True:                 #reward when hitting a wall
            reward = -5
            Q_table[Q_table_row, Q_table_column[action]] = Q_table[Q_table_row, Q_table_column[action]].item() + alpha * (reward + gamma * torch.max(Q_table[Q_table_row_new,2:]).item() - Q_table[Q_table_row, Q_table_column[action]].item())
        
        
        
        
    epsilon = epsilon * decay_rate
    number_of_steps_per_episode.append(step_counter)
    episode_counter = episode_counter + 1
    episode_counting_list.append(episode_counter)
    
    

plt.plot(episode_counting_list,number_of_steps_per_episode)
plt.xlabel('Episodes')
plt.ylabel('Number of steps')
plt.show()

    
    


    
