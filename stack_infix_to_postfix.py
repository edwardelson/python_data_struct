# Problem Solving with Algorithms and Data Structure p.78-81

from stack import LIFO_Stack as Stack

# convert "(A + (B * C))" -> "A B C * +"
def infix_to_postfix(infix_expr):
	# define precedence
	prec = {}
	prec["*"]=3
	prec["/"]=3
	prec["+"]=2
	prec["-"]=2
	prec["("]=1
	op_stack = Stack()
	postfix_list = []
	token_list = infix_expr.split()

	for token in token_list:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfix_list.append(token)
		elif token == "(":
			op_stack.push(token)
		elif token == ")":
			while op_stack.peek() != "(":
				postfix_list.append(op_stack.pop())
			op_stack.pop() #remove "("
		else:
			while not op_stack.is_empty() and prec[op_stack.peek()] >= prec[token]:
				postfix_list.append(op_stack.pop())
			op_stack.push(token)

	# when no more token
	while not op_stack.is_empty():
		postfix_list.append(op_stack.pop())

	# convert infix_expr to string
	return " ".join(postfix_list)

print(infix_to_postfix("1 + 2 * 3 + 5"))

# postfix evaluation. convert "4 5 6 * +" -> "34"
def postfix_eval(postfix_expr):
	eval_stack = Stack()
	token_list = postfix_expr.split()

	for token in token_list:
		if token in "0123456789":
			eval_stack.push(int(token))
		else:
			if token == "*":
				update = eval_stack.pop() * eval_stack.pop()
			elif token == "/":
				update = eval_stack.pop() / eval_stack.pop()
			elif token == "+":
				update = eval_stack.pop() + eval_stack.pop()
			elif token == "-":
				update = eval_stack.pop() - eval_stack.pop()
			eval_stack.push(update)

	return eval_stack.pop()	

print(postfix_eval(infix_to_postfix("1 * 2 - 3 * 5")))