#Dependency Parser

def dep_parse(sentence):
	state = initial_state(sentence)
	while len(state["words"]) > 0:
		user_oracle(state)
		print state


def initial_state(sentence):
	state = {"stack":[],"words":[],"relations":[]}
	state["stack"].append("root")
	words = sentence.split(" ")
	for word in words:
		state["words"].append(word)

	return state

def user_oracle(state):
	com = raw_input("enter oracle action: ")

	isvalid = False

	if com == "S" or com == "s":
		shift(state)
		isvalid = True
	else:
		print "Not a valid oracle command"
		isvalid = False

	return isvalid

def shift(state):
	w = state["words"].pop(0)
	state["stack"].append(w)


def main():
	dep_parse("hi there dude!")

if __name__=="__main__":
	main()