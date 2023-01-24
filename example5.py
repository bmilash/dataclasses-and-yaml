# example5.py - recursive data class (i.e. an object that contains instances 
# of the same type)

from dataclasses import dataclass
import yaml

# Define our programs configuration data class.
@dataclass
class Node:
	"Node of a binary tree of strings."
	value: str
	left: 'Node'=None
	right: 'Node'=None

	# The "=None" is specifying a default value for the left and 
	# right children of the node.

	# Without putting Node in quotes here we will get a 
	# NameError: name 'Node' is not defined exception.
	# Interesting discussion about that here:
	# https://stackoverflow.com/questions/69802491/create-recursive-dataclass-with-self-referential-type-hints
	# This is called a forward reference - its a reference to a type
	# that hasn't been defined yet.
	
	def display(self):
		"""
		Executes an in-order traversal of tree, printing the
		values as it goes.
		"""
		if self.left is not None:
			self.left.display()
		print(self.value)
		if self.right is not None:
			self.right.display()

# Let's define this binary tree with dragonfuit as the root node:
#		apple
#	banana
#		cherry
# dragonfruit
#		grape
#	mango
#		(empty)

binary_fruit_tree = Node( "dragonfuit",
	left = Node( "banana",
		left=Node( "apple" ),
		right=Node("cherry")),
	right=Node("mango",
		left=Node("grape")))

# Write the binary tree of fruits to a file.
yaml.dump( binary_fruit_tree, open("fruit.yaml","w") )

# Read the tree back in and print it.
copy_of_tree = yaml.load( open("fruit.yaml","r"), Loader=yaml.Loader )
print(copy_of_tree)
copy_of_tree.display()
