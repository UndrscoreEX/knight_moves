import numpy as np
def minStepToReachTarget(KnightPos, TargetPos, N):
  if KnightPos == TargetPos:
    return 0
  knight = Knight(KnightPos, TargetPos, N )
  all_paths, final_target_pos, knight_origin  = knight.search_path_from_node(KnightPos,0)
  knight.findnext(all_paths, final_target_pos, knight_origin, [])



class Knight:
  current_shortest_path = False
  visited = []
  paths = []
  temp_queue = []
  count = []


  def __init__(self,start,fin,space):
    self.start = start
    self.fin = fin
    self.space = space


  # Given a node, find all potential nodes.
  def find_nodes(self,pos):
      # valid moves of the knight.
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
      self.visited.append(pos)
      # includes only nodes that are within the bounds of the board:
      potential_nodes=[x for x in nodes if x[0] >=0 and x[0] <=self.space-1 and x[1] <= self.space-1 and x[1] >= 0 and x not in self.visited]
      print(f'nodes from: {pos} are: ',potential_nodes)
      return potential_nodes

  # explore the path of each node
  def search_path_from_node(self,curr,cnt):
    # begin counter and start retrieving valid nodes from the current position.
      this_attempts_count = cnt + 1
      potential = self.find_nodes(curr)

      if potential == []:
        # out of valid nodes to test, meaning it is not possible to find the goal.
          print('cant find a path \nfunction has ended')
          return 

      if self.fin not in potential:
        # Checking if its still possible to be a new record or if it is the first try
          if this_attempts_count < self.current_shortest_path or self.current_shortest_path == False:
              for x in potential:
                  self.paths.append({'count':this_attempts_count,'origin':curr, 'curr': x})
                  self.search_path_from_node(x,this_attempts_count)
          else:
              # The path will not be a new winner (shortest), so give up now.
              print('found another path but it was too long')
              count = 0 
              return
             
      else:
          print('\nfound a path', this_attempts_count)
          self.paths.append({'count' : this_attempts_count,'origin':curr, 'curr': self.fin})
          self.current_shortest_path = this_attempts_count
          this_attempts_count = 0 

      # refresh the visited cache
      self.visited = []

      return self.paths, self.fin, self.start

  # once all the paths are found, this will retrace the steps to find the shortest path from end to start:
  def findnext(self, dic, curr, tar, path):
      if tar != [x.get('origin') for x in dic if x.get('curr') == curr][0]:
          option = [x for x in dic if x.get('curr') == curr and x.get('count') == min([x.get('count') for x in dic if x.get('curr') == curr])]
          path.append(option[0].get('curr'))

          self.findnext(dic, option[0].get('origin'), tar, path)  
      else:
          option = [x for x in dic if x.get('curr') == curr and x.get('count') == min([x.get('count') for x in dic if x.get('curr') == curr])]
          path.append(option[0].get('curr'))

          #Add the knights original position.    
          path.append(tar)
          grid = np.array([['#' for _ in range(self.space)] for _ in range(self.space)])
          for x in path:
              grid[x[0]][x[1]] = "^"
          grid[self.start[0]][self.start[1]] = 'K'
          grid[self.fin[0]][self.fin[1]] = 'O'
          print("path :\n",path,f"in {len(path)} moves\n", "\n", grid)


minStepToReachTarget([1,1],[2,6],7)
