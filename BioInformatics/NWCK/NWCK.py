import time

class Newick(object):
	def __init__(self, data):
		self.nodes = []  
		self.node_index = 0
		self.edges = []  
		self.construct_tree(data)  
		self.name_index = {node.name:node.number for node in self.nodes}


	class node(object):
		def __init__(self, number, parent, name = None):
			self.number = number 
			self.parent = parent 
			self.children = [] 
			self.name = [name, 'node_'+str(self.number)][name==None] # puts a name to this based on input
		def add_child(self, child): 
			self.children.append(child)


	def construct_tree(self, data):
		'''Constructs the Newick Tree.'''
		data = data.replace(',', ' ').replace('(', '( ').replace(')', ' )').strip(';').split()
		current_node = self.node(-1,None)
		for item in data:
			if item[0] == '(':
				
				current_node = self.node(len(self.nodes), current_node.number)
				self.nodes.append(current_node)
				if len(self.nodes) > 1:
					self.nodes[current_node.parent].add_child(current_node.number)
					self.edges.append((current_node.parent,current_node.number))
			elif item[0] == ')': 
				if len(item) > 1:
					current_node.name = item[1:] 
				current_node = self.nodes[current_node.parent] 
			else:
				self.nodes[current_node.number].add_child(len(self.nodes))
				self.edges.append((current_node.number, len(self.nodes)))
				self.nodes.append(self.node(len(self.nodes), current_node.number, item))
	def distance(self, name1, name2):
		if name1 == name2:  
			return 0


		branch1 = [self.name_index[name1]]
		branch2 = [self.name_index[name2]]
		while self.nodes[branch1[-1]].parent != -1: 
			branch1.append(self.nodes[branch1[-1]].parent)
		while self.nodes[branch2[-1]].parent != -1:
			branch2.append(self.nodes[branch2[-1]].parent)

		return len(branch1) + len(branch2) - 2*len(set(branch1)&set(branch2))
         
ip=open('rosalind_nwck.txt',"r")
trees = [line.split('\n') for line in ip.read().strip().split('\n\n')]
tim=time.time()
dists = [str(Newick(tree[0]).distance(*tree[1].split())) for tree in trees]
tim2=time.time()
ip.close()
op=open("output_nwck.txt","w")
op.write(' '.join(dists))
op.close()




f=open("time.txt","w")
f.write("Execution Time: "+str(tim2-tim))
f.close()
