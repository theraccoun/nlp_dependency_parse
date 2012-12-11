#Dependency Parser

from random import randint
import copy

def dep_parse(sentence):
	state = initial_state(sentence)
	while not is_state_final(state):

		print "STACK: " , state["stack"]
		print "WORDS: " , state["words"]
		print "RELATS: " , state["relations"]
		print "-------------------------------------"
		rand_oracle(state)



def is_state_final(state):
	if len(state["words"]) == 0:
			return True
	else:
		return False


def initial_state(sentence):
	state = {"stack":[],"words":[],"relations":[]}
	state["stack"].append("root")
	words = sentence.split(" ")
	for word in words:
		state["words"].append(word)

	return state

def user_oracle(state):
	com = raw_input("enter oracle action: ")

	isvalid = True

	if com == "S" or com == "s":
		shift(state)
	elif com == "L" or com == "l":
		left(state)
	elif com == "R" or com == "r":
		right(state)
	else:
		print "Not a valid oracle command"
		isvalid = False

	return isvalid

def oracle_backtrack(state):
	start = Node("start", Node("NONE", "NONE"))
	cur_node = start
	cur_node.add_children()
	qstate = []

	while True:

		if len(state["words"]) == 0 and len(state["stack"]) == 1 and state["stack"][0] == "root":
			break

		print "---------------------------------------------"
		print "STACK: " , state["stack"]
		print "WORDS: " , state["words"]
		print "RELATS: " , state["relations"]
		print "~~~~~~~~~~~~~~~"
		print_node(cur_node)
		r = -1
		r = randint(0, len(cur_node.children)-1)
		# print r
		r = int(raw_input())
		cur_node = cur_node.children[r]
			
		
		print raw_input()
		# print "children: " , cur_node.children

		if change_state(state, cur_node.name):
			print "PERFORM: " , cur_node.name
			cur_node.add_children()
			qstate.append(copy.deepcopy(state))
			continue
		else:
			print "BACKTRACK"
			cur_node = cur_node.parent
			del cur_node.children[r]
			if not cur_node.children:
				qstate.pop()
				state = qstate[-1]
				print qstate
				print "prev state: " , state
				cur_node.parent.children.remove(cur_node)
				cur_node = cur_node.parent
				print "MEOW: " , print_node(cur_node)

def print_node(cur_node):
	print "NAME: " , cur_node.name
	print "PARENT: " , cur_node.parent.name
	children = []
	if len(cur_node.children) > 0:
		for child in cur_node.children:
			children.append(child.name)
		print "CHILDREN: " , children
	else:
		print "NO CHILDREN"
	print "\n"

def change_state(state, command):
	if command == "left":
		return left(state)
	elif command == "shift":
		return shift(state)
	elif command == "right":
		return right(state)
	else:
		raw_input()
		print "Please enter legit command instead of: " , command


def append_choices(queue):
	for c in choices:
		queue.append(c)

class Node:
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.children = []

	def add_children(self):
		left = Node("left", self)
		right = Node("right", self)
		shift = Node("shift", self)
		self.children = [left, shift, right]


class ChoiceRow:
	def __init__(self, parent):
		left = Node("left", parent)
		right = Node("right", parent)
		shift = Node("shift", parent)
		self.choices = [left, shift, right]


def rand_oracle(state):
	action = "";

	if len(state["stack"]) == 0:
		print "SHIFT\n"
		action = "shift"
		shift(state)
	elif state["stack"][-1] == "root":
		r = randint(0, 1)
		if r == 1:
			action = "shift"
			shift(state)
		elif r == 0:
			action = "right"
			right(state)
	else:
		r = randint(0,3)
		if r == 0:
			action = "shift"
			shift(state)
		elif r == 1:
			action = "left"
			left(state)
		elif r == 2:
			action = "right"
			right(state)

	return action

def shift(state):
	if len(state["words"]) == 0:
		return False

	w = state["words"].pop(0)
	state["stack"].append(w)

	return True

def left(state):
	if len(state["stack"]) == 0 or state["stack"][-1] == "root" or len(state["words"])==0:
		return False

	u = state["words"][0]
	v = state["stack"].pop()

	state["relations"].append([u,v])

	return True

def right(state):
	if len(state["stack"]) == 0 or len(state["words"])==0:
		return False

	u = state["words"][0]
	v = state["stack"].pop()

	state["relations"].append([v,u])
	state["words"][0] = v

	return True


def main():
	# sentence = raw_input("ENTER A SENTENCE")
	sentence = "I booked a flight"
	state = initial_state(sentence)
	oracle_backtrack(state)
	# dep_parse("I booked a morning flight")

if __name__=="__main__":
	main()