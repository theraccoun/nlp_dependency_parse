#Dependency Parser

def dep_parse(sentence):
	state = initial_state(sentence)
	while len(state["words"]) > 0:
		user_oracle(state)
		print "STACK: " , state["stack"]
		print "WORDS: " , state["words"]
		print "RELATS: " , state["relations"]


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

def shift(state):
	w = state["words"].pop(0)
	state["stack"].append(w)

def left(state):
	print "end of stack: " , state["stack"][-1]
	if len(state["stack"]) == 0 or state["stack"][-1] == "root":
		return False

	u = state["words"][0]
	v = state["stack"].pop()

	state["relations"].append([u,v])

	return True

def right(state):
	if len(state["stack"]) == 0:
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