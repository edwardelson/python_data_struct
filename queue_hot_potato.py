from queue import Queue

def hot_potato(name_list, num):
	y = Queue()

	for name in name_list:
		y.enqueue(name)

	while y.size() > 1:
		for i in range(num):
			y.enqueue(y.dequeue())
		y.dequeue()

	return y.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
