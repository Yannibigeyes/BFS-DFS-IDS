'''
Authors:    Yongyang Liu <liuyongyang@gatech.edu>
            
Date:       26 Aug 2020
'''


graph  = {
    'AL': ['FL', 'GA', 'MS', 'TN'],
    'AZ': ['CA', 'NM', 'NV', 'UT'],
    'AR': ['LA', 'MO', 'MS', 'OK', 'TN', 'TX'],
    'CA': ['AZ', 'NV', 'OR'],
    'CO': ['KS', 'NE', 'NM', 'OK', 'UT', 'WY'],
    'CT': ['MA', 'NY', 'RI'],
    'DE': ['MD', 'NJ', 'PA'],
    'DC': ['MD', 'VA'],
    'FL': ['AL', 'GA'],
    'GA': ['AL', 'FL', 'NC', 'SC', 'TN'],
    'ID': ['MT', 'NV', 'OR', 'UT', 'WA', 'WY'],
    'IL': ['IA', 'IN', 'KY', 'MO', 'WI'],
    'IN': ['IL', 'KY', 'MI', 'OH'],
    'IA': ['IL', 'MN', 'MO', 'NE', 'SD', 'WI'],
    'KS': ['CO', 'MO', 'NE', 'OK'],
    'KY': ['IL', 'IN', 'MO', 'OH', 'TN', 'VA', 'WV'],
    'LA': ['AR', 'MS', 'TX'],
    'ME': ['NH'],
    'MD': ['DC', 'DE', 'PA', 'VA', 'WV'],
    'MA': ['CT', 'NH', 'NY', 'RI', 'VT'],
    'MI': ['IN', 'OH', 'WI'],
    'MN': ['IA', 'ND', 'SD', 'WI'],
    'MS': ['AL', 'AR', 'LA', 'TN'],
    'MO': ['AR', 'IA', 'IL', 'KS', 'KY', 'NE', 'OK', 'TN'],
    'MT': ['ID', 'ND', 'SD', 'WY'],
    'NE': ['CO', 'IA', 'KS', 'MO', 'SD', 'WY'],
    'NV': ['AZ', 'CA', 'ID', 'OR', 'UT'],
    'NH': ['MA', 'ME', 'VT'],
    'NJ': ['DE', 'NY', 'PA'],
    'NM': ['AZ', 'CO', 'OK', 'TX'],
    'NY': ['CT', 'MA', 'NJ', 'PA', 'VT'],
    'NC': ['GA', 'SC', 'TN', 'VA'],
    'ND': ['MN', 'MT', 'SD'],
    'OH': ['IN', 'KY', 'MI', 'PA', 'WV'],
    'OK': ['AR', 'CO', 'KS', 'MO', 'NM', 'TX'],
    'OR': ['CA', 'ID', 'NV', 'WA'],
    'PA': ['DE', 'MD', 'NJ', 'NY', 'OH', 'WV'],
    'RI': ['CT', 'MA'], 
    'SC': ['GA', 'NC'],
    'SD': ['IA', 'MN', 'MT', 'ND', 'NE', 'WY'],
    'TN': ['AL', 'AR', 'GA', 'KY', 'MO', 'MS', 'NC', 'VA'],
    'TX': ['AR', 'LA', 'NM', 'OK'],
    'UT': ['AZ', 'CO', 'ID', 'NV', 'WY'],
    'VT': ['MA', 'NH', 'NY'],
    'VA': ['DC', 'KY', 'MD', 'NC', 'TN', 'WV'],
    'WA': ['ID', 'OR'],
    'WV': ['KY', 'MD', 'OH', 'PA', 'VA'],
    'WI': ['IA', 'IL', 'MI', 'MN'],
    'WY': ['CO', 'ID', 'MT', 'NE', 'SD', 'UT']
}


# ## Iterative-Deepening Search (IDS) with visit list (Yes)


import time


def IDS_Yes_paths(graph, start, goal, depth_max):
    
    for depth in range(1, depth_max+1):
        path, Num_pop, Q_len_max = DLS_Yes_paths(graph, start, goal, depth)
        if path is None:
            continue
        return path, Num_pop, Q_len_max
    
    raise ValueError('goal not in graph with depth {}'.format(depth_max))


def DLS_Yes_paths(graph, start, goal, depth):  
    Visited=[start]
    Num_pop = 0
    Queue = [(start, [start])]
    Q_len_max = len(Queue)
    
    while Queue:
        (vertex, path) = Queue.pop() # pop the last - LIFO
        if vertex == goal:
            return path, Num_pop, Q_len_max
        else:
            Num_pop +=1
            temp = [item for item in graph[vertex] if item not in Visited] #remove visited
            if (len(path) - 1) < depth:
                #for j in reversed(temp):  # pop in alphabetical order 
                for j in temp:  # in alphabetical order 
                    Queue.append((j, path + [j]))
                    Visited.append(j)
                    if len(Queue) > Q_len_max:
                        Q_len_max = len(Queue)
    return None, None, None

start_time = time.time()
path, num_pop, queue_length_max = IDS_Yes_paths(graph, 'WA', 'GA', 100) #find the path when depth = 9
elapsed_time = time.time()-start_time
path_length = len(path)-1
print('Returned Path: %s' % (path))
print('Time (s): %1.12f' % (elapsed_time))
print('Num of Paths Popped from Queue: %d' % (num_pop))
print('Max queue size - # Paths: %d' % (queue_length_max))
print('Returned Path Length - # Edges: %d' % (path_length))

