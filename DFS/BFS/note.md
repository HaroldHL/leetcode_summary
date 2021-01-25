DFS template

```python
#Python Recusion
visited = set() 
def dfs(node, visited):    
  if node in visited: # terminator    	
    # already visited     	
    return 	
  visited.add(node) 	
  # process current node here. 	
  ...	
  for next_node in node.children(): 		
    if next_node not in visited: 			
      dfs(next_node, visited)
      
      
 def DFS(self, tree): 	
    if tree.root is None: 		
      return [] 
    
    visited, stack = [], [tree.root]	
    
    while stack: 		
      node = stack.pop() 		
      visited.add(node)		
      
      process (node) 		
      nodes = generate_related_nodes(node) 		
      stack.push(nodes) 	# other processing work 	...
```

BFS template



```python
# Python
def BFS(graph, start, end):    
  visited = set()	
  queue = [] 	queue.append([start]) 	
  while queue: 		
    node = queue.pop() 		
    visited.add(node)	
    
    process(node) 		
    nodes = generate_related_nodes(node) 		
    queue.push(nodes)	# other processing work 	...
```

