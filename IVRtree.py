class Tree(object): 
    def __init__(self): 
        self.left = None 
        self.right = None 
        self.data = None 
        self.frequency = 0  
 
def printTree(tree): 
	if (tree!=None): 
		print "Task: ", tree.data, "  ", 
		print "Frequency: ", tree.frequency  
		printTree(tree.left) 
		printTree(tree.right) 
		
#if __name__ == "main":
root = Tree() 
root.data = "1" 
left = Tree() 
left.data = "2" 
right = Tree() 
right.data = "3" 

leftleft = Tree() 
leftleft.data = "4" 
rightright = Tree() 
rightright.data = "7" 

leftright = Tree() 
leftright.data = "5" 
rightleft = Tree() 
rightleft.data = "6" 

leftleft.left = None 
leftright.left = None 
rightleft.left = None 
rightright.left = None 

leftleft.right = None 
leftright.right = None 
rightleft.right = None 
rightright.right = None 

left.left = leftleft 
left.right = leftright 

right.left = rightleft 
right.right = rightright 

root.left = left
root.right = right 

root.frequency = 0 
printTree(root) 
