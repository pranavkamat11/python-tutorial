# this will be imported

print("Imported my_module")

test = 'Test String'

def find_index(to_search,target):
	# to find index of a value in sequence
	for i , value in enumerate(to_search):
		if value == target :
			return i

	return -1
