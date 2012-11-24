#Dependency Parser

from random import randint

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

def rand_oracle(state):
	if len(state["stack"]) == 0:
		print "SHIFT\n"
		shift(state)
	elif state["stack"][-1] == "root":
		r = randint(0, 1)
		if r == 1:
			print "SHIFT\n"
			shift(state)
		elif r == 0:
			print "RIGHT\n"
			right(state)
	else:
		r = randint(0,3)
		if r == 0:
			print "SHIFT \n"
			shift(state)
		elif r == 1:
			print "LEFT \n"
			left(state)
		elif r == 2:
			print "RIGHT \n"
			right(state)

def shift(state):
	w = state["words"].pop(0)
	state["stack"].append(w)

def left(state):
	if len(state["stack"]) == 0 or state["stack"][-1] == "root":
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
	dep_parse("I booked a morning flight")

if __name__=="__main__":
	main()