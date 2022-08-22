import numpy as np
current_shortest_path = False
visited = []
paths = []
temp_queue = []
counts =[]
def minStepToReachTarget(KnightPos, TargetPos, N):

    if KnightPos == TargetPos:
        return 0

    # Given a node, find all potential nodes. Used by the 
    def find_nodes(pos):

        nodes = [
            [pos[0]-2,pos[1]-1],
            [pos[0]-1,pos[1]-2],
            [pos[0]+1,pos[1]+2],
            [pos[0]+2,pos[1]+1],
            [pos[0]-2,pos[1]+1],
            [pos[0]-1,pos[1]+2],
            [pos[0]+1,pos[1]-2],
            [pos[0]+2,pos[1]-1],
            ]
        visited.append(pos)
        # includes only nodes that are within the bounds of the board:
        potential_nodes=[x for x in nodes if x[0] >=0 and x[0] <=N-1 and x[1] <= N-1 and x[1] >= 0 and x not in visited]
        print(f'nodes from: {pos} are: ',potential_nodes)
        return potential_nodes

    # explore the path of each node
    def search_path_from_node(curr,cnt):
        count = cnt + 1
        global current_shortest_path
        potential = find_nodes(curr)
        print(f'potential nodes from {curr} are:',potential)

        if potential == []:
            print('cant find a path \nfunction has ended')
            return 

        if TargetPos not in potential:
            if count < current_shortest_path or current_shortest_path == False:
                for x in potential:
                    paths.append({'count':count,'origin':curr, 'curr': x})
                    search_path_from_node(x,count)
            else:
                print('found another path but it was too long')
                count = 0 
                return
                
        else:
            print('\nfound a path', count)
            counts.append(count)
            paths.append({'count' : count,'origin':curr, 'curr': TargetPos})
            current_shortest_path = count
            count = 0 


        # min(counts)
        global visited
        visited = []
        return paths, TargetPos, KnightPos

    # once all the paths are found, this will retrace the steps to find the shortest path from end to start:
    def findnext(dic, curr, tar, path):
        if tar != [x.get('origin') for x in dic if x.get('curr') == curr][0]:
            option = [x for x in dic if x.get('curr') == curr and x.get('count') == min([x.get('count') for x in dic if x.get('curr') == curr])]
            path.append(option[0].get('curr'))

            findnext(dic, option[0].get('origin'), tar, path)  
        else:
            option = [x for x in dic if x.get('curr') == curr and x.get('count') == min([x.get('count') for x in dic if x.get('curr') == curr])]
            path.append(option[0].get('curr'))

            #Add the knights original position.    
            path.append(tar)
            grid = np.array([['#' for _ in range(N)] for _ in range(N)])
            for x in path:
                grid[x[0]][x[1]] = "^"
            grid[KnightPos[0]][KnightPos[1]] = 'K'
            grid[TargetPos[0]][TargetPos[1]] = 'O'
            print("path :\n",path,f"in {len(path)} moves\n", "\n", grid)

    
    all_paths, final_target_pos, knight_origin  = search_path_from_node(KnightPos,0)
    # print(all_paths   )

    return findnext(all_paths, final_target_pos, knight_origin, [])


minStepToReachTarget([4,1],[3,4],7)